"""SMTP sender with STARTTLS or implicit TLS, plain text + HTML + attachments."""
from __future__ import annotations

import html as _html
import mimetypes
import re
import smtplib
from email.message import EmailMessage
from email.utils import formataddr, make_msgid
from pathlib import Path
from typing import Sequence


_URL_RE = re.compile(r"(https?://[^\s<>\"']+)")


def text_to_html(body: str) -> str:
    """Turn plain text into a simple, natural-looking HTML body.

    - Escapes HTML entities
    - Auto-links http(s) URLs
    - Paragraphs on blank lines, <br> on single line breaks
    - Basic email-client typography
    """
    escaped = _html.escape(body)
    linked = _URL_RE.sub(r'<a href="\1">\1</a>', escaped)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", linked) if p.strip()]
    rendered = "".join(
        "<p>" + p.replace("\n", "<br>\n") + "</p>\n"
        for p in paragraphs
    )
    return (
        '<!DOCTYPE html><html><body style="font-family: -apple-system, Segoe UI, '
        'Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1.5; color: #222;">\n'
        f"{rendered}</body></html>"
    )


class SMTPSender:
    def __init__(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        use_starttls: bool = True,
        from_name: str | None = None,
        auto_html: bool = True,
    ):
        self.host, self.port = host, port
        self.username, self.password = username, password
        self.use_starttls = use_starttls
        self.from_name = from_name
        self.auto_html = auto_html

    def _from_header(self) -> str:
        return formataddr((self.from_name, self.username)) if self.from_name else self.username

    def build(
        self,
        to: str | Sequence[str],
        subject: str,
        body: str,
        html: str | None = None,
        cc: Sequence[str] | None = None,
        bcc: Sequence[str] | None = None,
        reply_to: str | None = None,
        attachments: Sequence[str | Path] | None = None,
    ) -> EmailMessage:
        msg = EmailMessage()
        msg["From"] = self._from_header()
        msg["To"] = ", ".join([to] if isinstance(to, str) else list(to))
        if cc:
            msg["Cc"] = ", ".join(cc)
        if reply_to:
            msg["Reply-To"] = reply_to
        msg["Subject"] = subject
        msg["Message-ID"] = make_msgid()
        msg.set_content(body)
        if html is None and self.auto_html and body.strip():
            html = text_to_html(body)
        if html:
            msg.add_alternative(html, subtype="html")
        for path in attachments or []:
            p = Path(path)
            if not p.is_file():
                raise FileNotFoundError(p)
            ctype, _ = mimetypes.guess_type(str(p))
            maintype, subtype = (ctype or "application/octet-stream").split("/", 1)
            msg.add_attachment(p.read_bytes(), maintype=maintype, subtype=subtype, filename=p.name)
        # Store BCC out-of-band for envelope-only delivery
        msg._bcc_list = list(bcc) if bcc else []  # type: ignore[attr-defined]
        return msg

    def send(self, msg: EmailMessage) -> None:
        bcc = getattr(msg, "_bcc_list", [])
        recipients = []
        for hdr in ("To", "Cc"):
            v = msg.get(hdr)
            if v:
                recipients.extend([a.strip() for a in v.split(",") if a.strip()])
        recipients.extend(bcc)

        if self.use_starttls:
            with smtplib.SMTP(self.host, self.port, timeout=30) as s:
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(self.username, self.password)
                s.send_message(msg, from_addr=self.username, to_addrs=recipients)
        else:
            with smtplib.SMTP_SSL(self.host, self.port, timeout=30) as s:
                s.login(self.username, self.password)
                s.send_message(msg, from_addr=self.username, to_addrs=recipients)

    def send_simple(
        self,
        to: str | Sequence[str],
        subject: str,
        body: str,
        html: str | None = None,
        **kwargs,
    ) -> None:
        self.send(self.build(to=to, subject=subject, body=body, html=html, **kwargs))
