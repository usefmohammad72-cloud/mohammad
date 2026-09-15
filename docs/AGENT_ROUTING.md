# Agent Routing Matrix

| Request type | Primary | Secondary | Output |
|---|---|---|---|
| Coding | Claude Code | Codex | source + tests |
| Debugging | Codex | Claude Code | diagnosis + patch + tests |
| Architecture | Orchestrator | Claude + Codex | design decision |
| Research | Research Agent | QA | sourced notes |
| Graphic design | Visual Designer | Vision/Asset | prompt/spec/assets |
| Image analysis | Vision/Asset | QA | findings + asset notes |
| Documents | Document Agent | Research | Markdown/Word/PDF-ready source |
| Presentation | Document Agent | Visual Designer | slide source + visual plan |
| QA | QA Agent | Codex | test report |
| Release | Orchestrator | QA | release checklist |

## Multi-agent rule

Use parallel specialists only for independent work. The Orchestrator integrates outputs and resolves conflicts before declaring completion.
