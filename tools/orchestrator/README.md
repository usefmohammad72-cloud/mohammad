# Local Orchestrator

The orchestrator is a local-first Python 3.11+ control plane. GitHub stores durable project files; execution happens on the user's machine.

## Smoke test

From the repository root:

```powershell
python tools/orchestrator/orchestrator.py --demo
```

Expected JSON contains `"status": "DONE"` and a generated `outputs/REPORT-*.md` path.

## Run a repository task file

Task files are UTF-8 JSON objects. The `command` field must be an argument array, not a shell command string. This keeps execution on `shell=False` and avoids shell interpolation.

Example:

```powershell
python tools/orchestrator/orchestrator.py --task examples/tasks/coding-smoke.json
```

A task can contain:

```json
{
  "id": "coding-smoke",
  "project": "orchestrator-demo",
  "task_type": "CODING",
  "prompt": "Run the Phase 2 smoke test.",
  "command": ["python", "-c", "print('TASK_FILE_EXECUTION_OK')"],
  "timeout": 30
}
```

The `task_type` determines the planned agent route. Phase 2 records that route and executes the supplied local command; actual Claude/Codex invocation is intentionally deferred to Phase 3.

## Utilities

```powershell
python tools/orchestrator/orchestrator.py --detect "fix my Python code"
python tools/orchestrator/orchestrator.py --route CODING
```

SQLite state is stored locally at `tools/orchestrator/state.db` and must never be committed.
