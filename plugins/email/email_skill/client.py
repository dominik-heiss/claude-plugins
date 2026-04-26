"""High-level EmailClient combining IMAP + SMTP."""
from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

from email_skill.config import EmailConfig
from email_skill.credentials import get_password
from email_skill.imap_reader import IMAPReader, EmailMessage
from email_skill.smtp_sender import SMTPSender


class EmailClient:
    """One-stop client. Loads config + password, exposes reader and sender."""

    def __init__(self, config: EmailConfig | None = None, password: str | None = None):
        self.config = config or EmailConfig.load()
        self._password = password or get_password(self.config.username)

    @contextmanager
    def reader(self) -> Iterator[IMAPReader]:
        r = IMAPReader(
            host=self.config.imap_host,
            port=self.config.imap_port,
            username=self.config.username,
            password=self._password,
            use_ssl=self.config.use_ssl_imap,
        )
        with r as opened:
            yield opened

    @property
    def sender(self) -> SMTPSender:
        return SMTPSender(
            host=self.config.smtp_host,
            port=self.config.smtp_port,
            username=self.config.username,
            password=self._password,
            use_starttls=self.config.use_starttls_smtp,
            from_name=self.config.from_name,
            auto_html=self.config.auto_html,
        )

    def list_recent(self, limit: int = 20, folder: str = "INBOX", unread_only: bool = False) -> list[EmailMessage]:
        criteria = "UNSEEN" if unread_only else "ALL"
        with self.reader() as r:
            return list(r.iter_recent(limit=limit, folder=folder, criteria=criteria))

    def send(self, to, subject: str, body: str, force_send: bool = False, **kwargs) -> str:
        """Send or save as draft, depending on config.send_mode.

        Returns: "sent" if delivered via SMTP, "draft" if saved to drafts folder.
        Pass force_send=True to override draft mode.
        """
        msg = self.sender.build(to=to, subject=subject, body=body, **kwargs)
        if self.config.send_mode == "draft" and not force_send:
            self.save_draft(msg)
            return "draft"
        self.sender.send(msg)
        self._copy_to_sent(msg)
        return "sent"

    def save_draft(self, msg) -> None:
        """Store a built message in the configured drafts folder via IMAP APPEND."""
        raw = msg.as_bytes()
        with self.reader() as r:
            r.append(self.config.drafts_folder, raw, flags="\\Draft \\Seen")

    def _copy_to_sent(self, msg) -> None:
        """Copy a successfully-sent message into the IMAP Sent folder.

        Silently ignores errors — the message was delivered; failure here is
        only a local mirroring issue and should not surface as a send failure.
        """
        try:
            raw = msg.as_bytes()
            with self.reader() as r:
                r.append(self.config.sent_folder, raw, flags="\\Seen")
        except Exception:
            pass
