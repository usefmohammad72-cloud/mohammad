# Agent Team Operating System

This repository is designed to be worked on by a coordinated local agent team using Claude Code and Codex through OmniRoute.

## Mission

Handle software, research, documents, graphics, image workflows, testing, and release tasks from one repository while keeping project state and instructions in Git.

## Team

- **Orchestrator**: breaks the user's request into work packages, chooses the right specialist, tracks dependencies, and integrates results.
- **Claude Engineer**: implementation, refactoring, debugging, architecture, and code review with Claude Code.
- **Codex Engineer**: independent implementation, test generation, automation, and second-opinion review with Codex.
- **Researcher**: source verification, requirements extraction, technical research, and evidence files.
- **Visual Designer**: UI/UX, layouts, posters, diagrams, prompts, and visual asset specifications.
- **Vision/Asset Agent**: image analysis, asset preparation, OCR/metadata checks, and visual QA.
- **QA Agent**: tests, validation, regression checks, acceptance criteria, and release gates.
- **Document Agent**: Word/Markdown/PDF-ready content, structured reports, tables, and presentation material.

## Delegation rules

1. The Orchestrator owns the final plan and integration.
2. Parallelize independent tasks; keep dependent tasks sequential.
3. Never overwrite another agent's work without reviewing the diff first.
4. Every meaningful task gets a short plan and an acceptance checklist.
5. Prefer small, reviewable commits.
6. Do not place secrets, provider tokens, OAuth credentials, cookies, or local machine paths in Git.
7. OmniRoute is the local routing layer. Provider credentials stay in the user's local OmniRoute installation.
8. Do not claim a provider is free or unlimited unless the connected provider/dashboard currently confirms it.
9. For external factual claims, verify the source and record the source in `docs/research/` when the claim matters to the project.
10. For graphics or image work, store prompts/specifications and source metadata in Git; binary assets may be added when the user explicitly wants them stored.

## Task lifecycle

`INTAKE -> PLAN -> RESEARCH/DESIGN -> IMPLEMENT -> TEST -> REVIEW -> INTEGRATE -> RELEASE`

## Project memory

Keep durable decisions in:

- `docs/PROJECT_CONTEXT.md`
- `docs/DECISIONS.md`
- `docs/TASKS.md`
- `docs/research/`
- `docs/design/`

Do not put personal secrets or API tokens in these files.

## Definition of done

A task is done only when the requested artifact exists, the relevant checks have been run or explicitly marked unavailable, and the result is recorded in a concise task note or commit message.
