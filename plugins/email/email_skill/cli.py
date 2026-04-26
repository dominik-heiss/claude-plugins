"""CLI: setup, test, list, send, read.

Usage:
  python -m email_skill setup              Interactive setup (config + password)
  python -m email_skill test               Verify IMAP + SMTP connection
  python -m email_skill list [--limit N] [--unread] [--folder INBOX]
  python -m email_skill read UID [--folder INBOX]
  python -m email_skill send --to X --subject S --body B [--html file] [--attach FILE]
  python -m email_skill folders
  python -m email_skill reset-password
"""
from __future__ import annotations

import argparse
import getpass
import json
import sys
from pathlib import Path

from email_skill.config import EmailConfig, config_path
from email_skill import credentials
from email_skill.client import EmailClient


def _cmd_setup(args) -> int:
    print(f"Config will be saved to: {config_path()}")
    existing = None
    try:
        existing = EmailConfig.load()
        print(f"(Existing config loaded for {existing.username})")
    except FileNotFoundError:
        pass

    def ask(prompt: str, default=None):
        suffix = f" [{default}]" if default is not None else ""
        val = input(f"{prompt}{suffix}: ").strip()
        return val or default

    username = ask("Username (full email address)", existing.username if existing else None)
    imap_host = ask("IMAP host", existing.imap_host if existing else None)
    imap_port = int(ask("IMAP port", existing.imap_port if existing else 993))
    smtp_host = ask("SMTP host", existing.smtp_host if existing else imap_host)
    smtp_port = int(ask("SMTP port (587=STARTTLS, 465=SSL)", existing.smtp_port if existing else 587))
    use_starttls = smtp_port != 465
    from_name = ask("From display name (optional, Enter to skip)", existing.from_name if existing else "") or None

    default_mode = existing.send_mode if existing else "send"
    send_mode = ask("Send mode — 'send' delivers via SMTP, 'draft' stores in IMAP drafts folder", default_mode)
    if send_mode not in ("send", "draft"):
        print(f"Invalid mode {send_mode!r}, defaulting to 'send'")
        send_mode = "send"
    drafts_folder = ask("Drafts folder name", existing.drafts_folder if existing else "Drafts")

    cfg = EmailConfig(
        imap_host=imap_host, imap_port=imap_port,
        smtp_host=smtp_host, smtp_port=smtp_port,
        username=username, use_ssl_imap=True,
        use_starttls_smtp=use_starttls, from_name=from_name,
        send_mode=send_mode, drafts_folder=drafts_folder,
    )
    saved = cfg.save()
    print(f"Saved config to {saved}")

    pw = getpass.getpass("Password (hidden, stored in OS keyring): ")
    if pw:
        credentials.set_password(username, pw)
        print("Password stored in keyring.")
    else:
        print(f"No password entered. You can set env var {credentials.ENV_VAR} later.")
    return 0


def _cmd_test(args) -> int:
    client = EmailClient()
    print(f"Testing {client.config.username} ...")
    with client.reader() as r:
        folders = r.list_folders()
        print(f"IMAP OK — {len(folders)} folders. Sample: {folders[:5]}")
    s = client.sender
    import smtplib
    if s.use_starttls:
        with smtplib.SMTP(s.host, s.port, timeout=30) as conn:
            conn.ehlo(); conn.starttls(); conn.ehlo()
            conn.login(s.username, s.password)
    else:
        with smtplib.SMTP_SSL(s.host, s.port, timeout=30) as conn:
            conn.login(s.username, s.password)
    print("SMTP OK — login successful.")
    return 0


def _cmd_list(args) -> int:
    client = EmailClient()
    msgs = client.list_recent(limit=args.limit, folder=args.folder, unread_only=args.unread)
    out = [
        {
            "uid": m.uid,
            "date": m.date.isoformat() if m.date else None,
            "from": m.from_,
            "subject": m.subject,
            "unread": m.is_unread,
            "attachments": m.attachments,
        }
        for m in msgs
    ]
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


def _cmd_read(args) -> int:
    client = EmailClient()
    with client.reader() as r:
        r.select(args.folder)
        msg = r.fetch(args.uid)
    print(json.dumps({
        "uid": msg.uid,
        "date": msg.date.isoformat() if msg.date else None,
        "from": msg.from_,
        "to": msg.to,
        "subject": msg.subject,
        "body": msg.body_text or msg.body_html,
        "attachments": msg.attachments,
        "unread": msg.is_unread,
    }, indent=2, ensure_ascii=False))
    return 0


def _cmd_send(args) -> int:
    client = EmailClient()
    html = Path(args.html).read_text(encoding="utf-8") if args.html else None
    body = args.body
    if args.body_file:
        body = Path(args.body_file).read_text(encoding="utf-8")
    if args.plain_only:
        client.config.auto_html = False
    result = client.send(
        to=args.to,
        subject=args.subject,
        body=body or "",
        html=html,
        cc=args.cc or None,
        bcc=args.bcc or None,
        attachments=args.attach or None,
        force_send=args.force_send,
    )
    if result == "draft":
        print(f"Saved draft to '{client.config.drafts_folder}' folder (send_mode=draft). "
              f"Use --force-send to bypass, or change send_mode in config.")
    else:
        print(f"Sent to {args.to}")
    return 0


def _cmd_folders(args) -> int:
    client = EmailClient()
    with client.reader() as r:
        for f in r.list_folders():
            print(f)
    return 0


def _cmd_mode(args) -> int:
    cfg = EmailConfig.load()
    if args.set:
        if args.set not in ("send", "draft"):
            print(f"Invalid mode {args.set!r}. Use 'send' or 'draft'.", file=sys.stderr)
            return 2
        cfg.send_mode = args.set
        cfg.save()
        print(f"send_mode = {cfg.send_mode}")
    else:
        print(f"send_mode = {cfg.send_mode}")
        print(f"drafts_folder = {cfg.drafts_folder}")
    return 0


def _cmd_reset_password(args) -> int:
    cfg = EmailConfig.load()
    pw = getpass.getpass("New password: ")
    credentials.set_password(cfg.username, pw)
    print(f"Password updated for {cfg.username}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="email_skill")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("setup", help="Interactive setup").set_defaults(func=_cmd_setup)
    sub.add_parser("test", help="Verify IMAP + SMTP").set_defaults(func=_cmd_test)
    sub.add_parser("folders", help="List IMAP folders").set_defaults(func=_cmd_folders)
    sub.add_parser("reset-password", help="Update stored password").set_defaults(func=_cmd_reset_password)

    pm = sub.add_parser("mode", help="Show or set send_mode (send|draft)")
    pm.add_argument("--set", choices=["send", "draft"], help="Change mode")
    pm.set_defaults(func=_cmd_mode)

    pl = sub.add_parser("list", help="List recent messages")
    pl.add_argument("--limit", type=int, default=20)
    pl.add_argument("--folder", default="INBOX")
    pl.add_argument("--unread", action="store_true")
    pl.set_defaults(func=_cmd_list)

    pr = sub.add_parser("read", help="Fetch one message by UID")
    pr.add_argument("uid")
    pr.add_argument("--folder", default="INBOX")
    pr.set_defaults(func=_cmd_read)

    ps = sub.add_parser("send", help="Send a message")
    ps.add_argument("--to", required=True)
    ps.add_argument("--subject", required=True)
    ps.add_argument("--body", default="")
    ps.add_argument("--body-file", help="Read body from file")
    ps.add_argument("--html", help="Path to HTML body file")
    ps.add_argument("--cc", action="append")
    ps.add_argument("--bcc", action="append")
    ps.add_argument("--attach", action="append", help="Attachment path (repeatable)")
    ps.add_argument("--force-send", action="store_true",
                    help="Send via SMTP even if config.send_mode is 'draft'")
    ps.add_argument("--plain-only", action="store_true",
                    help="Disable auto-HTML; send plain text only")
    ps.set_defaults(func=_cmd_send)

    args = p.parse_args(argv)
    try:
        return args.func(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
