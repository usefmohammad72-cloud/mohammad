import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools" / "orchestrator"))

from orchestrator import detect_project_type, route


def test_detect_coding():
    assert detect_project_type("fix my Python code") == "CODING"


def test_detect_excel():
    assert detect_project_type("write an Excel VBA formula") == "EXCEL"


def test_detect_mixed():
    assert detect_project_type("research this paper and create PowerPoint slides") == "MIXED"


def test_route_coding():
    assert route("CODING") == ["claude", "codex", "qa"]


def test_route_research():
    assert route("RESEARCH") == ["research", "fact_checker", "qa"]


def test_route_graphics():
    assert route("GRAPHICS") == ["visual", "vision", "qa"]
