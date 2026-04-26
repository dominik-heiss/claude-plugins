"""Configuration loading for email_skill.

Non-sensitive settings live in YAML; paths follow XDG conventions cross-platform.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("Missing dependency: pyyaml. Run: pip install pyyaml") from exc


def config_dir() -> Path:
    """Return platform-appropriate config directory."""
    override = os.environ.get("EMAIL_SKILL_CONFIG_DIR")
    if override:
        return Path(override)
    xdg = os.environ.get("XDG_CONFIG_HOME")
    if xdg:
        return Path(xdg) / "email_skill"
    if os.name == "nt":
        base = os.environ.get("APPDATA") or str(Path.home() / "AppData" / "Roaming")
        return Path(base) / "email_skill"
    return Path.home() / ".config" / "email_skill"


def config_path() -> Path:
    return config_dir() / "config.yaml"


@dataclass
class EmailConfig:
    imap_host: str
    imap_port: int
    smtp_host: str
    smtp_port: int
    username: str
    use_ssl_imap: bool = True
    use_starttls_smtp: bool = True
    from_name: str | None = None
    send_mode: str = "draft"         # Default: store in IMAP drafts for safety. Set to "send" to deliver via SMTP.
    drafts_folder: str = "Drafts"    # IMAP folder for drafts (often "Drafts", "INBOX.Drafts", "Entwürfe")
    sent_folder: str = "Sent"        # IMAP folder where sent messages are copied after SMTP delivery
    auto_html: bool = True           # Auto-generate an HTML alternative from plain text bodies

    @classmethod
    def load(cls, path: Path | None = None) -> "EmailConfig":
        p = path or config_path()
        if not p.exists():
            raise FileNotFoundError(
                f"No config at {p}. Run: python -m email_skill setup"
            )
        data: dict[str, Any] = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        missing = {"imap_host", "imap_port", "smtp_host", "smtp_port", "username"} - data.keys()
        if missing:
            raise ValueError(f"Config missing keys: {sorted(missing)}")
        return cls(**data)

    def save(self, path: Path | None = None) -> Path:
        p = path or config_path()
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(yaml.safe_dump(asdict(self), sort_keys=False), encoding="utf-8")
        return p
