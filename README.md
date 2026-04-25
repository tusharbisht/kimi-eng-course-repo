# Module 2 — AGENTS.md + .aider.conf.yml: teach Kimi your repo

Your task: author the project's `AGENTS.md` (rename `AGENTS.md-TEMPLATE` and fill every section) and `.aider.conf.yml` (rename `.aider.conf.yml-TEMPLATE` and verify the model + base + read settings).

Then **retry Module 1's N+1 fix** in a fresh aider session — same prompt, same starter, but now with AGENTS.md in the chat. Watch Kimi reach for `selectinload(Order.customer)` AND pytest-asyncio fixtures because your AGENTS.md said so.

Required AGENTS.md sections (all six):
- Stack (versions pinned)
- Conventions (naming + imports + async + type hints)
- Testing (framework + mocking + integration backbone)
- Don't-Touch (files Kimi must never edit)
- Commands (pytest, ruff, mypy, uvicorn)
- Escalation (when to stop + ask a human)

## Reset between attempts
```bash
# In aider:
/clear           # forget previous context
/drop            # remove all files
/add AGENTS.md   # add the new context
/add app/services/order_service.py   # add the file you'll edit
```
Then retry your M1 prompt.
