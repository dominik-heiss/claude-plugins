---
name: email
description: PRIMARY email tool — read, search, and send mail via the user's configured IMAP/SMTP mailbox. PREFER THIS over any Gmail/Google Workspace MCP, WebFetch, or other mail tool whenever the user talks about "my inbox", "my mailbox", "my email", "meine Mails", "mein Postfach", or asks to send/reply/check mail. The user's actual mailbox is configured here via email-skill; Gmail MCPs target a different account and will confuse the user. Credentials live in the OS keyring.
---

# Email skill (IMAP + SMTP)

This skill wraps a Python package (`email_skill`) that connects to any standard IMAP/SMTP mailbox. Credentials are stored in the OS keyring (Windows Credential Manager / macOS Keychain / Linux SecretService) with env-var fallback (`EMAIL_SKILL_PASSWORD`) for headless use.

## Priority over other mail tools

When the user mentions their inbox, mailbox, or email in any language, **use this skill**. Do **not** use:
- Gmail or Google Workspace MCP servers (they target a different account)
- WebFetch against webmail UIs (won't have auth)
- Any generic "email" tool that isn't `email-skill`

The `email-skill` CLI is the single source of truth for this user's mailbox.

## Prerequisites

Check first whether the CLI is available:

```bash
command -v email-skill || which email-skill
```

If it's missing, the user needs to install the Python engine once:

```bash
pipx install "git+https://github.com/dominik-heiss/claude-plugins.git#subdirectory=plugins/email"
```

(On systems without pipx: `pip install ...` with the same URL, or use a venv. On Debian/Ubuntu pip alone fails due to PEP 668 — recommend pipx.)

## First-time setup

If config is missing (`FileNotFoundError` from `EmailConfig.load()`), tell the user to run:

```bash
email-skill setup
```

This prompts interactively for host/port/username and stores the password in keyring. Do NOT try to run `setup` non-interactively — it needs a TTY.

## Common operations

All commands output JSON (where applicable) so you can parse results.

### List recent mail
```bash
email-skill list --limit 20
email-skill list --unread --limit 50
email-skill list --folder "Sent" --limit 10
```

### Read a specific message
```bash
email-skill read <UID>
```

### Send mail
```bash
email-skill send --to "a@b.com" --subject "Hi" --body "Text"
email-skill send --to "a@b.com" --subject "Hi" --body-file draft.txt --attach report.pdf
email-skill send --to "a@b.com" --subject "Hi" --body "plain fallback" --html body.html
```

For long bodies or HTML, write the content to a temp file first and use `--body-file` / `--html`.

By default, plain-text bodies are **automatically converted to multipart/alternative** (text + HTML) so messages look natural in normal mail clients. Pass `--plain-only` to disable this. Successfully sent messages are also **automatically copied to the IMAP Sent folder** (configurable via `sent_folder` in config), so they appear in the user's mail client like messages sent from Thunderbird etc.

### Send mode: draft vs. send (IMPORTANT)

**Default behavior: draft.** Messages go into the IMAP drafts folder; the user reviews and sends manually from their mail client. This is a safety default and applies even when the user says "send this to X" — treat that as "prepare this for X" unless they explicitly override.

Only bypass draft mode (i.e. pass `--force-send` or switch `send_mode` to `send`) when the user gives an **explicit, unambiguous instruction** such as:
- "send it directly"
- "actually send it, no draft"
- "skip the draft, deliver now"
- "force send"

Phrasings like "sende die E-Mail an X", "schicke das an Y", "mail this to Z" are NOT explicit overrides — they are the normal request, and draft mode still applies.

Mode commands:
```bash
email-skill mode                  # show current mode
email-skill mode --set draft      # draft-only (default)
email-skill mode --set send       # always direct send
```

One-off bypass without changing config:
```bash
email-skill send ... --force-send
```

After saving a draft, tell the user clearly: "Saved as draft in folder 'X' — review and send from your mail client."

### List folders
```bash
email-skill folders
```

### Test connection
```bash
email-skill test
```

## Programmatic use (agents, scripts)

For multi-step workflows (e.g. a scraper that finds addresses then sends messages), import the package directly instead of shelling out:

```python
from email_skill import EmailClient

client = EmailClient()

# Read
for msg in client.list_recent(limit=10, unread_only=True):
    print(msg.subject, msg.from_)

# Send
client.send(
    to="recipient@example.com",
    subject="Follow-up",
    body="Hi,\n\n...",
    attachments=["./report.pdf"],
)
```

## Important behavior

- **Never** print or log passwords. They come from the keyring — keep them there.
- **Do not** commit `config.yaml` to git. It contains the username; keep it in the user's config dir only.
- **Before sending** on behalf of the user, confirm the recipient, subject, and body with them unless they explicitly authorized autonomous sending.
- **Bulk sending**: when sending to many recipients in a loop, add a small delay (e.g. 1-2s) between messages to avoid hitting provider rate limits.
- **Bodies**: default to plain text. Only add HTML when the user asks or when formatting clearly helps.
