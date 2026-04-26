"""Cross-platform password storage via keyring with env-var fallback.

Priority:
  1. EMAIL_SKILL_PASSWORD env var (useful for headless/CI)
  2. OS keyring (Windows Credential Manager, macOS Keychain, Linux SecretService)
"""
from __future__ import annotations

import os

SERVICE = "email_skill"
ENV_VAR = "EMAIL_SKILL_PASSWORD"


def _keyring():
    try:
        import keyring
        return keyring
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: keyring. Run: pip install keyring"
        ) from exc


def get_password(username: str) -> str:
    env = os.environ.get(ENV_VAR)
    if env:
        return env
    pw = _keyring().get_password(SERVICE, username)
    if not pw:
        raise RuntimeError(
            f"No password stored for {username!r}. "
            f"Run: python -m email_skill setup  (or set {ENV_VAR})"
        )
    return pw


def set_password(username: str, password: str) -> None:
    _keyring().set_password(SERVICE, username, password)


def delete_password(username: str) -> None:
    try:
        _keyring().delete_password(SERVICE, username)
    except Exception:
        pass
