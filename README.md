# Open-Source AI Coding — Kimi K2 + Aider Course Repo

Each module is its own branch. The bootstrap one-liner from your course step checks out the right branch automatically.

## Prerequisites
- Python 3.11+ (3.12 fine)
- `uv` or `pip` (`pip install uv`)
- `aider-chat` (`uv tool install aider-chat` or `pipx install aider-chat`)
- An OpenRouter or Moonshot API key (free tier on OpenRouter is enough for the whole course)

## Module branches
- `module-0-preflight` — verify your toolchain
- `module-1-starter` — `OrderService.get_recent_orders` with a planted N+1 (no AGENTS.md)
- `module-2-claudemd` — author AGENTS.md + .aider.conf.yml; retry M1's fix
- `module-3-agents` — Aider commands + your first `/audit-endpoint` custom command
- `module-4-hooks` — build `harness/loop.py` (~100 lines) directly on Moonshot's tool_use API
- `module-5-mcp` — wire the team-tickets MCP via a Python adapter
- `module-6-capstone` — POST /orders capstone with GHA `lab-grade.yml`

## Running locally
```bash
uv pip install -e ".[dev]"
pytest -q
ruff check .
mypy app/
uvicorn app.main:app --reload
```

## Provider setup (BYO-key)
```bash
# OpenRouter (free tier, recommended)
export OPENAI_API_KEY=sk-or-v1-...your-key...
aider --model openai/moonshotai/kimi-k2-0905 --openai-api-base https://openrouter.ai/api/v1

# Moonshot direct (lower latency)
export OPENAI_API_KEY=sk-...your-moonshot-key...
aider --model openai/kimi-k2-0905 --openai-api-base https://api.moonshot.ai/v1
```
