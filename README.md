# Mohammad Agent Workspace

A persistent multi-agent workspace for software, research, documents, graphics, images, automation, and QA.

## Stack

- **Claude Code** — primary implementation and reasoning agent
- **Codex** — independent implementation, automation, and review agent
- **OmniRoute** — local routing layer between the coding agents and configured providers
- **GitHub** — durable project memory, source, task state, specifications, and artifacts

## Start here

1. Read `AGENTS.md`.
2. Read `CLAUDE.md` when working with Claude Code.
3. Read `CODEX.md` when working with Codex.
4. Check `docs/TASKS.md` for active work.
5. Check `docs/PROJECT_CONTEXT.md` and `docs/DECISIONS.md` for durable context.
6. Use `docs/AGENT_ROUTING.md` to choose specialists.

## OmniRoute

Expected local gateway:

`http://localhost:20128`

Keep all live provider credentials in OmniRoute or environment variables. Never commit them to Git.

## Workspace model

Each project can live under its own folder. Upload source files, datasets, documents, images, prompts, and specifications into the appropriate project folder. The agent team should inspect the repository first, preserve existing work, and leave reproducible artifacts and tests behind.

## Suggested project layout

```text
projects/
  <project-name>/
    README.md
    input/
    src/
    tests/
    docs/
    design/
    assets/
    output/
```

For large binary assets, use Git LFS or external storage rather than committing huge files directly.

## Security

Never commit API keys, OAuth tokens, cookies, session files, private keys, or other secrets.
