# Module 3 — Aider workflows: /architect, /code, /run, custom commands

Two exercises:

1. **Plan-then-apply with /architect → /code** (~10 min)
   Use Aider's `/architect` mode to PLAN a refactor of `OrderService` into a separate `OrderQueryRepository` (single-responsibility split). Aider produces a plan (no edits). Review it, then `/code` to apply. Run `/test pytest -q` to verify.
   Paste: the architect plan + the resulting diff + a screenshot of `pytest -q` passing.

2. **Author your first custom command** (~15 min)
   Create `.aider/commands/audit-endpoint.md` — a reusable prompt that audits any FastAPI endpoint for: missing `Depends()` auth, manual exception handling that should use exception handlers, response schema mismatches, N+1 risks via lazy SQLAlchemy relationships. Then run `/audit-endpoint app/api/orders.py` (after you've created that file in M6) — or `/audit-endpoint app/services/order_service.py` for now.

## Aider mode primitives at a glance
- `/architect <prompt>` — plan, do NOT edit files. Best for design discussions.
- `/code <prompt>` — edit files to implement what was planned.
- `/ask <prompt>` — answer a question, no plan and no edits.
- `/run <command>` — execute a shell command and add output to chat. Best: `/run pytest -q`.
- `/test pytest -q` — same as `/run` but specifically for tests; failures auto-feed back to Kimi.
- `/diff` — show what's been changed in the chat session.
- `/undo` — revert the last edit.
