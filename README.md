# dh-claude-plugins

Personal marketplace of Claude Code plugins by Dominik Heiß.

## Install the marketplace

```shell
/plugin marketplace add dominik-heiss/claude-plugins
```

Then install any plugin from the list below.

## Available plugins

_None published yet — plugins are added here as they're released._

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
