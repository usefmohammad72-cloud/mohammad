from __future__ import annotations

import argparse
import json
import os
import sqlite3
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "tools" / "orchestrator" / "state.db"
REPORT_DIR = ROOT / "outputs"

PROJECT_TYPES = {
    "CODING", "RESEARCH", "EXCEL", "DATA_ANALYSIS", "DOCUMENT",
    "PRESENTATION", "GRAPHICS", "IMAGE", "AUTOMATION", "QA", "MIXED"
}

ROUTES = {
    "CODING": ["claude", "codex", "qa"],
    "RESEARCH": ["research", "fact_checker", "qa"],
    "EXCEL": ["excel", "formula_vba", "qa"],
    "DATA_ANALYSIS": ["data", "qa"],
    "DOCUMENT": ["document", "reviewer", "qa"],
    "PRESENTATION": ["document", "visual", "qa"],
    "GRAPHICS": ["visual", "vision", "qa"],
    "IMAGE": ["vision", "visual", "qa"],
    "AUTOMATION": ["claude", "codex", "qa"],
    "QA": ["qa"],
    "MIXED": ["orchestrator", "qa"],
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def init_db() -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as db:
        db.execute("""CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            project TEXT NOT NULL,
            task_type TEXT NOT NULL,
            status TEXT NOT NULL,
            agent TEXT,
            command TEXT,
            started_at TEXT,
            finished_at TEXT,
            exit_code INTEGER,
            result TEXT,
            error TEXT,
            retries INTEGER DEFAULT 0
        )""")
        db.commit()


def detect_project_type(text: str) -> str:
    t = text.lower()
    scores = {
        "CODING": sum(x in t for x in ["python", "code", "coding", "bug", "program", "javascript"]),
        "RESEARCH": sum(x in t for x in ["research", "paper", "article", "thesis", "proposal", "literature"]),
        "EXCEL": sum(x in t for x in ["excel", "xlsx", "formula", "vba", "spreadsheet"]),
        "DATA_ANALYSIS": sum(x in t for x in ["data analysis", "dataset", "statistics", "csv"]),
        "DOCUMENT": sum(x in t for x in ["word", "pdf", "report", "document"]),
        "PRESENTATION": sum(x in t for x in ["powerpoint", "presentation", "slides", "slide"]),
        "GRAPHICS": sum(x in t for x in ["poster", "graphic", "design", "banner"]),
        "IMAGE": sum(x in t for x in ["image", "photo", "picture", "visual"]),
        "AUTOMATION": sum(x in t for x in ["automation", "automate", "script"]),
    }
    positive = [k for k, v in scores.items() if v > 0]
    if len(positive) > 1:
        return "MIXED"
    if positive:
        return max(positive, key=scores.get)
    return "QA"


def route(task_type: str) -> list[str]:
    task_type = task_type.upper()
    if task_type not in PROJECT_TYPES:
        raise ValueError(f"Unsupported project type: {task_type}")
    return ROUTES[task_type]


def record_task(task_id: str, project: str, task_type: str, status: str, agent: str | None = None,
                command: str | None = None, **kwargs) -> None:
    with sqlite3.connect(DB_PATH) as db:
        db.execute("""INSERT OR REPLACE INTO tasks
            (id, project, task_type, status, agent, command, started_at, finished_at,
             exit_code, result, error, retries)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (task_id, project, task_type, status, agent, command,
             kwargs.get("started_at"), kwargs.get("finished_at"), kwargs.get("exit_code"),
             kwargs.get("result"), kwargs.get("error"), kwargs.get("retries", 0)))
        db.commit()


def run_command(command: list[str], timeout: int = 300) -> tuple[int, str, str]:
    env = os.environ.copy()
    proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True,
                          timeout=timeout, env=env)
    return proc.returncode, proc.stdout, proc.stderr


def write_report(task_id: str, project: str, task_type: str, status: str,
                 agents: list[str], details: str = "") -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    path = REPORT_DIR / f"REPORT-{task_id}.md"
    path.write_text(
        f"# Task Report\n\n"
        f"- Task: `{task_id}`\n"
        f"- Project: `{project}`\n"
        f"- Type: `{task_type}`\n"
        f"- Status: `{status}`\n"
        f"- Agents: {', '.join(agents)}\n"
        f"- Finished: `{utc_now()}`\n\n"
        f"## Details\n{details}\n",
        encoding="utf-8",
    )
    return path


def demo_task() -> int:
    init_db()
    task_id = f"demo-{uuid.uuid4().hex[:8]}"
    project = "orchestrator-demo"
    task_type = "CODING"
    agents = route(task_type)
    started = utc_now()
    command = [sys.executable, "-c", "print('ORCHESTRATOR_CODING_TASK_OK')"]
    record_task(task_id, project, task_type, "IN_PROGRESS", agents[0], " ".join(command), started_at=started)
    try:
        code, stdout, stderr = run_command(command)
        status = "DONE" if code == 0 and "ORCHESTRATOR_CODING_TASK_OK" in stdout else "FAILED"
        record_task(task_id, project, task_type, status, agents[0], " ".join(command),
                    started_at=started, finished_at=utc_now(), exit_code=code,
                    result=stdout, error=stderr)
        report = write_report(task_id, project, task_type, status, agents,
                              f"Command exit code: `{code}`\n\n```text\n{stdout}\n```\n")
        print(json.dumps({"task_id": task_id, "status": status, "report": str(report.relative_to(ROOT))}, ensure_ascii=False))
        return 0 if status == "DONE" else 1
    except Exception as exc:
        record_task(task_id, project, task_type, "FAILED", agents[0], " ".join(command),
                    started_at=started, finished_at=utc_now(), error=str(exc))
        write_report(task_id, project, task_type, "FAILED", agents, str(exc))
        print(json.dumps({"task_id": task_id, "status": "FAILED", "error": str(exc)}, ensure_ascii=False))
        return 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Local multi-agent project orchestrator")
    parser.add_argument("--detect", metavar="TEXT", help="Detect project type")
    parser.add_argument("--route", metavar="TYPE", help="Show route for a project type")
    parser.add_argument("--demo", action="store_true", help="Run the end-to-end local CODING smoke task")
    args = parser.parse_args()
    init_db()
    if args.detect:
        print(json.dumps({"project_type": detect_project_type(args.detect)}, ensure_ascii=False))
        return 0
    if args.route:
        print(json.dumps({"route": route(args.route)}, ensure_ascii=False))
        return 0
    if args.demo:
        return demo_task()
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
