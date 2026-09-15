# Project Context

## Purpose

This repository is the durable workspace for the user's projects. It is intended to support both technical and creative work, including coding, research, documents, presentations, graphics, image workflows, automation, and QA.

## Execution model

Claude Code and Codex are the primary engineering agents. OmniRoute is the local routing/gateway layer. Provider authentication and quotas are handled outside Git and must never be committed.

## Agent routing

- Coding / debugging -> Claude Engineer + Codex Engineer
- Architecture -> Orchestrator + Claude Engineer + Codex review
- Research -> Researcher + QA
- Graphics / UI / posters / visual concepts -> Visual Designer + Vision/Asset Agent
- Documents / reports / slides -> Document Agent + Researcher
- Release / regression -> QA + Codex review

## Artifact policy

Git should contain source files, prompts, specifications, reproducible configuration, documentation, tests, and project decisions. Large or sensitive local assets should not be committed unless explicitly requested.

## Current infrastructure target

Local OmniRoute endpoint: `http://localhost:20128`

Claude Code should be launched through OmniRoute rather than embedding provider credentials in repository files.
