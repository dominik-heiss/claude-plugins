---
description: Read, send, or manage email via the user's IMAP/SMTP mailbox (the email skill from this plugin). Use this when the user explicitly invokes /email, even if a Gmail/Google MCP is also available.
argument-hint: "[check | send <to> | reply <uid> | mode | <free-form request>]"
---

# /email — IMAP/SMTP mailbox operations

The user invoked `/email` with arguments: **$ARGUMENTS**

## What you must do

1. Use the **`email` skill** from this plugin (claude-plugins/email), NOT any Gmail/Google MCP server, NOT WebFetch, NOT any other email tool. The user's mailbox is configured here — other tools will fail or hit the wrong account.

2. The CLI is `email-skill` (already installed via pipx). All operations go through it. Read `~/.claude/skills/email.md` if you need the full contract.

3. Interpret `$ARGUMENTS` as the user's intent:
   - empty / `check` / `inbox` → list recent mail (`email-skill list --limit 20`)
   - `unread` → `email-skill list --unread --limit 50`
   - `send <recipient> ...` → compose and route through draft mode (default) unless the user explicitly said "send directly" / "force send"
   - `reply <UID>` → fetch that UID, draft a reply
   - `mode` → show current send mode
   - free-form text → infer the operation, ask if ambiguous

4. **Send safety**: the configured `send_mode` (default: `draft`) is authoritative. NEVER pass `--force-send` unless the user has just used phrasing like "send it directly", "actually send", "no draft", "force send", "skip the draft". Normal "send X to Y" requests → draft.

5. After any action, briefly tell the user what happened in 1-2 sentences. For drafts, name the folder and remind them to review/send from their mail client.

## If setup is missing

If `email-skill test` reports a config error or `FileNotFoundError`, tell the user to run `email-skill setup` in their own terminal (interactive, needs a TTY — you cannot run it).
