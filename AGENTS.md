# Agent Team Operating Contract

## Architecture

This repository is the Single Source of Truth for durable project files, documentation, artifacts, and version history. GitHub is not the execution environment. Agent execution is local through the Python Orchestrator.

Locked stack:
- Python 3.11+
- SQLite for machine state
- Markdown for human-readable state/documentation
- subprocess + JSON for agent execution
- OmniRoute as the local model gateway after current compatibility is verified
- Windows/Linux local execution
- GitHub Actions optional

## Mission

Coordinate coding, research, Excel/data, documents/presentations, graphics/images, automation, and QA while keeping credentials local and project artifacts in Git.

## Team

- Orchestrator: planning, routing, state, integration
- Claude Engineer: implementation, debugging, architecture
- Codex Engineer: independent implementation/review/testing
- Researcher: evidence and source verification
- Excel/Data Agent: formulas, VBA, data workflows
- Document Agent: Word/PDF/PowerPoint/report content
- Visual Agent: design and visual specifications
- Vision/Asset Agent: image analysis and asset QA
- QA Agent: independent validation and acceptance gates

## Language policy

Technical system files (AGENTS.md, CLAUDE.md, CODEX.md, README.md): English.
User-facing reports/project notes: Persian when appropriate.
Code, filenames, IDs, and commit messages: English.

## Security

Never commit API keys, Kiro/Claude/OpenAI tokens, OAuth credentials, passwords, cookies, sessions, private keys, or local credential files. Secrets stay on the user's local machine. `.env.example` contains no real secret.

A pre-commit gitleaks scan is required. If a secret is detected, the commit must stop.

## Workflow

INTAKE -> PLAN -> RESEARCH/DESIGN -> IMPLEMENT -> TEST -> REVIEW -> INTEGRATE -> RELEASE

Independent work may run in parallel; dependent work is sequential.

## State and memory

Machine state: `tools/orchestrator/state.db` (local and gitignored).
Human state: `docs/PROJECT_CONTEXT.md`, `docs/DECISIONS.md`, `docs/TASKS.md`.

## Agent disagreement

Record both technical positions. The Orchestrator decides or asks the user. Record the reason in DECISIONS.md. Never prefer an agent without a reason.

## QA

QA must use explicit PASS/FAIL criteria and should use a different provider/model or substantially different review prompt when practical to reduce correlated errors.

## Cost controls

Respect configured token, call, and retry limits. Stop when a limit is exceeded and report it.

## Git policy

`main` = stable, `dev` = active development, `agent/<task-id>` = task work. PRs are optional for normal work and required for destructive, public-release, or major sensitive changes.

## Truthfulness

Never claim a task, connection, or test is complete unless it actually passed. Distinguish static validation from real execution and user validation.
