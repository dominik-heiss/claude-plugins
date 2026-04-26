"""IMAP reader — list, fetch, search, mark, move, delete."""
from __future__ import annotations

import email
import imaplib
from dataclasses import dataclass, field
from email.header import decode_header, make_header
from email.message import Message
from email.utils import parsedate_to_datetime
from datetime import datetime
from typing import Iterator


@dataclass
class EmailMessage:
    uid: str
    subject: str
    from_: str
    to: str
    date: datetime | None
    body_text: str
    body_html: str
    flags: list[str] = field(default_factory=list)
    attachments: list[str] = field(default_factory=list)

    @property
    def is_unread(self) -> bool:
        return "\\Seen" not in self.flags


def _decode(value: str | None) -> str:
    if not value:
        return ""
    try:
        return str(make_header(decode_header(value)))
    except Exception:
        return value


def _extract_bodies(msg: Message) -> tuple[str, str, list[str]]:
    text, html, attachments = "", "", []
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            disp = str(part.get("Content-Disposition", ""))
            if "attachment" in disp:
                fname = _decode(part.get_filename())
                if fname:
                    attachments.append(fname)
                continue
            if ctype == "text/plain" and not text:
                text = _part_text(part)
            elif ctype == "text/html" and not html:
                html = _part_text(part)
    else:
        payload = _part_text(msg)
        if msg.get_content_type() == "text/html":
            html = payload
        else:
            text = payload
    return text, html, attachments


def _part_text(part: Message) -> str:
    try:
        payload = part.get_payload(decode=True)
        if payload is None:
            return ""
        charset = part.get_content_charset() or "utf-8"
        return payload.decode(charset, errors="replace")
    except Exception:
        return ""


class IMAPReader:
    def __init__(self, host: str, port: int, username: str, password: str, use_ssl: bool = True):
        self.host, self.port = host, port
        self.username, self.password = username, password
        self.use_ssl = use_ssl
        self.conn: imaplib.IMAP4 | None = None

    def __enter__(self) -> "IMAPReader":
        cls = imaplib.IMAP4_SSL if self.use_ssl else imaplib.IMAP4
        self.conn = cls(self.host, self.port)
        self.conn.login(self.username, self.password)
        return self

    def __exit__(self, *exc) -> None:
        if self.conn is not None:
            try:
                self.conn.logout()
            except Exception:
                pass
            self.conn = None

    def list_folders(self) -> list[str]:
        assert self.conn
        status, data = self.conn.list()
        if status != "OK":
            return []
        out = []
        for raw in data:
            if not raw:
                continue
            line = raw.decode(errors="replace") if isinstance(raw, bytes) else raw
            name = line.split(' "/" ')[-1].strip().strip('"')
            out.append(name)
        return out

    def select(self, folder: str = "INBOX", readonly: bool = True) -> int:
        assert self.conn
        status, data = self.conn.select(folder, readonly=readonly)
        if status != "OK":
            raise RuntimeError(f"Select failed: {data}")
        return int(data[0])

    def search_uids(self, criteria: str = "ALL") -> list[str]:
        assert self.conn
        status, data = self.conn.uid("SEARCH", None, criteria)
        if status != "OK" or not data or not data[0]:
            return []
        return data[0].decode().split()

    def fetch(self, uid: str) -> EmailMessage:
        assert self.conn
        status, data = self.conn.uid("FETCH", uid, "(RFC822 FLAGS)")
        if status != "OK" or not data or not data[0]:
            raise RuntimeError(f"Fetch failed for uid {uid}")
        raw_bytes = None
        flags: list[str] = []
        for item in data:
            if isinstance(item, tuple) and len(item) == 2:
                raw_bytes = item[1]
                meta = item[0].decode(errors="replace") if isinstance(item[0], bytes) else str(item[0])
                flags = imaplib.ParseFlags(meta.encode()) if "FLAGS" in meta else ()
                flags = [f.decode() if isinstance(f, bytes) else f for f in flags]
        if raw_bytes is None:
            raise RuntimeError(f"No body for uid {uid}")
        msg = email.message_from_bytes(raw_bytes)
        text, html, attachments = _extract_bodies(msg)
        date_hdr = msg.get("Date")
        try:
            dt = parsedate_to_datetime(date_hdr) if date_hdr else None
        except Exception:
            dt = None
        return EmailMessage(
            uid=uid,
            subject=_decode(msg.get("Subject")),
            from_=_decode(msg.get("From")),
            to=_decode(msg.get("To")),
            date=dt,
            body_text=text,
            body_html=html,
            flags=list(flags),
            attachments=attachments,
        )

    def iter_recent(self, limit: int = 20, folder: str = "INBOX", criteria: str = "ALL") -> Iterator[EmailMessage]:
        self.select(folder)
        uids = self.search_uids(criteria)
        for uid in reversed(uids[-limit:]):
            yield self.fetch(uid)

    def mark_seen(self, uid: str) -> None:
        assert self.conn
        self.conn.uid("STORE", uid, "+FLAGS", "(\\Seen)")

    def move(self, uid: str, dest_folder: str) -> None:
        assert self.conn
        try:
            self.conn.uid("MOVE", uid, dest_folder)
        except Exception:
            self.conn.uid("COPY", uid, dest_folder)
            self.conn.uid("STORE", uid, "+FLAGS", "(\\Deleted)")
            self.conn.expunge()

    def append(self, folder: str, raw_message: bytes, flags: str = "\\Draft \\Seen") -> None:
        """Append a raw RFC822 message to an IMAP folder (used for drafts)."""
        assert self.conn
        import time
        status, data = self.conn.append(folder, f"({flags})", imaplib.Time2Internaldate(time.time()), raw_message)
        if status != "OK":
            raise RuntimeError(f"APPEND to {folder!r} failed: {data}")

    def delete(self, uid: str) -> None:
        assert self.conn
        self.conn.uid("STORE", uid, "+FLAGS", "(\\Deleted)")
        self.conn.expunge()
