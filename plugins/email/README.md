# email skill

A Claude Code plugin that lets Claude read and send emails over any standard IMAP/SMTP mailbox. Part of [claude-plugins](https://github.com/dominik-heiss/claude-plugins).

- **Cross-platform**: Windows, macOS, Linux
- **Secure by default**: passwords stored in the OS keyring (never in config files), with env-var fallback for headless/CI use
- **Works with any provider**: GMX, all-inkl, Fastmail, Migadu, self-hosted, etc. — just provide host/port
- **Two usage modes**: CLI (for Claude to invoke via Bash) or Python API (for agent scripts)

## Install

Recommended: [pipx](https://pipx.pypa.io/) (isolated venv, global CLI):

```bash
pipx install "git+https://github.com/dominik-heiss/claude-plugins.git#subdirectory=plugins/email"
```

On headless Linux (no desktop keyring), use the env-var fallback:

```bash
pipx install "git+https://github.com/dominik-heiss/claude-plugins.git#subdirectory=plugins/email[linux-headless]"
# or
export EMAIL_SKILL_PASSWORD="..."
```

## Setup

```bash
email-skill setup
```

Interactive wizard: asks for IMAP/SMTP host, port, username; stores the password in the OS keyring. Config is written to:

- Linux: `~/.config/email_skill/config.yaml`
- macOS: `~/.config/email_skill/config.yaml` (or `$XDG_CONFIG_HOME`)
- Windows: `%APPDATA%\email_skill\config.yaml`

Verify:

```bash
email-skill test
```

## CLI usage

```bash
email-skill list --limit 20                  # recent mail (JSON)
email-skill list --unread --limit 50         # unread only
email-skill read <UID>                       # full message
email-skill send --to x@y.com --subject S --body "Hi"
email-skill send --to x@y.com --subject S --body-file draft.txt --attach report.pdf
email-skill folders                          # list IMAP folders
email-skill mode                             # show send mode (draft|send)
```

## Python API

```python
from email_skill import EmailClient

client = EmailClient()

for msg in client.list_recent(limit=10, unread_only=True):
    print(msg.date, msg.from_, msg.subject)

client.send(
    to="recipient@example.com",
    subject="Hello",
    body="Plain text body",
    attachments=["./attachment.pdf"],
)
```

## As a Claude Code skill

The plugin includes `.claude/skills/email.md`. When installed as a Claude Code plugin, Claude can invoke email operations on demand — check inbox, send messages, reply, etc. See the skill file for the invocation contract.

## Credential priority

1. `EMAIL_SKILL_PASSWORD` environment variable (if set) — use for CI/cron
2. OS keyring entry for `(email_skill, <username>)` — default for desktop use

## Security notes

- Passwords are never written to disk in plaintext. The keyring uses OS-level encryption.
- `config.yaml` is gitignored — don't commit it.
- For 2FA/app-specific passwords (e.g. many providers require these), generate one in your provider's control panel and paste it into `setup`.

## License

MIT
