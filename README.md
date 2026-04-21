# dh-claude-plugins

Personal marketplace of Claude Code plugins by Dominik Heiß.

## Install the marketplace

```shell
/plugin marketplace add dominik-heiss/claude-plugins
```

Then install any plugin from the list below.

## Available plugins

### mct — Management Consulting Team

End-to-end strategy consulting team simulation. Multi-agent orchestration with a configured Engagement Manager, Research Analyst, Business Analyst, Financial Modeler, Slide Architect, QA Reviewer, Partner Advisor, and Client Lens. Hypothesis-driven workflows, iterative review cascades, and traceable deliverables.

```shell
/plugin install mct@dh-claude-plugins
```

Details: [`plugins/management-consulting-team/README.md`](./plugins/management-consulting-team/README.md).

## Local development

Clone the repo and point Claude Code at the plugin directory directly:

```shell
claude --plugin-dir ~/claude-plugins/plugins/management-consulting-team
```

Or add the local marketplace and install from it (closer to production install):

```shell
/plugin marketplace add ~/claude-plugins
/plugin install mct@dh-claude-plugins
```

## Repository layout

```
claude-plugins/
├── .claude-plugin/
│   └── marketplace.json       # Marketplace catalog
├── plugins/
│   └── management-consulting-team/   # Management consulting team plugin (/mct:)
└── README.md
```

Each plugin is a self-contained directory under `plugins/` with its own `.claude-plugin/plugin.json` manifest, agents, commands, skills, and assets.

## License

MIT — see individual plugin directories for plugin-specific licenses.
