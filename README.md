# dh-claude-plugins

Personal marketplace of Claude Code plugins by Dominik Heiß.

## Install the marketplace

```shell
/plugin marketplace add dominik-heiss/claude-plugins
```

Then install any plugin from the list below.

## Available plugins

| Plugin | Description |
|---|---|
| [`email`](plugins/email) | Read, search, and send emails via IMAP/SMTP. Cross-platform, secure credential storage via OS keyring, draft-mode by default. |
| [`marp-presentation`](plugins/marp-presentation) | Author and export MARP markdown presentations with the bundled editorial theme (display serif + sans, terracotta accent, 16:9). |

Install any plugin with:

```shell
/plugin install <name>@dh-claude-plugins
```

## Repository layout

```
claude-plugins/
├── .claude-plugin/
│   └── marketplace.json       # Marketplace catalog
├── plugins/                   # Each plugin is a self-contained directory
└── README.md
```

Each plugin lives under `plugins/<name>/` with its own `.claude-plugin/plugin.json` manifest, agents, commands, skills, and assets.

## License

MIT — see individual plugin directories for plugin-specific licenses.
