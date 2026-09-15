# Local Orchestrator

The orchestrator is a local-first Python 3.11+ control plane. GitHub stores durable project files; execution happens on the user's machine.

## Smoke test

From the repository root:

```powershell
python tools/orchestrator/orchestrator.py --demo
```

Expected JSON contains `"status": "DONE"` and a generated `outputs/REPORT-*.md` path.

## Utilities

```powershell
python tools/orchestrator/orchestrator.py --detect "fix my Python code"
python tools/orchestrator/orchestrator.py --route CODING
```

SQLite state is stored locally at `tools/orchestrator/state.db` and must never be committed.
