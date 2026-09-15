# Mohammad Agent Workspace

A local-first multi-agent project workspace backed by GitHub.

## Architecture

GitHub is the Single Source of Truth for durable project files, specifications, artifacts, and version history. It is not the execution environment.

Execution happens on the user's local machine through the Python 3.11+ Orchestrator.

```text
User -> Local Orchestrator -> Agent Team -> OmniRoute -> Providers/Models
                     |                         |
                     +------ QA <--------------+
                              |
                              v
                           GitHub
                              |
                              v
                     User downloads/tests
```

## Stack

- Claude Code — primary implementation agent
- Codex — independent implementation/review agent
- OmniRoute — local model gateway
- Python 3.11+ — Orchestrator
- SQLite — machine state
- Markdown — human-readable project memory
- GitHub — storage, version control, and delivery

## Current implementation

Phase 2 contains a minimal local Orchestrator at `tools/orchestrator/orchestrator.py`.

Smoke test:

```powershell
python tools/orchestrator/orchestrator.py --demo
```

Utilities:

```powershell
python tools/orchestrator/orchestrator.py --detect "fix my Python code"
python tools/orchestrator/orchestrator.py --route CODING
```

Local SQLite state is written to `tools/orchestrator/state.db` and is ignored by Git.

## Project storage

Use isolated project folders:

```text
projects/
  <project-name>/
    README.md
    input/
    source/
    code/
    data/
    research/
    docs/
    design/
    assets/
    tests/
    output/
    final/
```

Generated files placed in the repository can be downloaded by the user and tested locally. Large binaries should use Git LFS or suitable external storage.

## Security

Never commit API keys, Kiro/Claude/OpenAI tokens, OAuth credentials, passwords, cookies, sessions, private keys, or local credential files. Secrets remain local.

Pre-commit secret scanning uses gitleaks. A detected secret must block the commit.

## Phases

1. Foundation
2. Minimal Orchestrator
3. Claude Code + OmniRoute
4. Codex Reviewer
5. Specialized Teams
6. START.ps1 + Security Automation
