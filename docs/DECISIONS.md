# Architecture Decisions

## ADR-001: Keep provider credentials outside Git

OmniRoute provider authentication remains local. Repository files may document variable names and endpoints, but never store live credentials.

## ADR-002: Use a shared agent contract

`AGENTS.md` is the common operating contract. `CLAUDE.md` and `CODEX.md` provide tool-specific instructions while inheriting the shared rules.

## ADR-003: Separate planning from execution

The Orchestrator decomposes requests before specialists implement them. This reduces duplicated work and makes mixed technical/creative projects auditable.

## ADR-004: Human approval for irreversible actions

Agents may prepare changes, commits, assets, and release notes, but destructive external actions or publication should require explicit user approval unless a future project policy says otherwise.
