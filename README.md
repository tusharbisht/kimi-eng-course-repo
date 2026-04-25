# Module 1 — Feel the Pain: Aider+Kimi WITHOUT context

You're working in `app/services/order_service.py`. Your team uses `OrderService.get_recent_orders()` on the customer dashboard. Streamflow's SRE team flagged it for slow response times — every call triggers ~21 database queries for 20 orders.

**Your task** (~20 min):
1. Start Aider against this branch:
   ```
   export OPENAI_API_KEY=sk-or-...   # OpenRouter free tier
   aider --model openai/moonshotai/kimi-k2-0905 \
     --openai-api-base https://openrouter.ai/api/v1
   ```
2. Add the file: `/add app/services/order_service.py`
3. Ask Kimi to find + fix the bug. Use `/architect` first if you want, then `/code`.
4. **DO NOT** author `AGENTS.md` yet — you'll do that in Module 2.
5. Paste back: (a) the prompt you used, (b) the diff Aider produced, (c) any edits you had to make by hand because Kimi didn't know your team's conventions.

What you'll observe: without context, Kimi may use SQLAlchemy 1.x `query()` syntax (your team uses 2.0 `select()`), suggest unittest instead of pytest, or import sync APIs into your async code path. Whatever it gets wrong is what you'll add to `AGENTS.md` in M2.

## Verify locally before/after the fix
```bash
uv pip install -e ".[dev]"
pytest -q                        # Smoke test should pass
ruff check . && mypy app/        # Should also pass
```
