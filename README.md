# Module 4 — Build the loop yourself: 100-line Moonshot tool_use harness

Two exercises:

1. **Implement `harness/loop.py`** (~30 min)
   Rename `harness/loop.py-STUB` → `harness/loop.py` and fill the TODOs. Three tools (`read_file`, `edit_file`, `run_pytest`), an async-or-sync 10-turn loop on Moonshot's OpenAI-compatible endpoint, error-surfacing back to the model. Use `from openai import OpenAI`; set `base_url="https://openrouter.ai/api/v1"`. ~100 lines when clean.

2. **Add a pre-tool guardrail** (~10 min)
   Extend the loop with a check before every `edit_file` call: if the path matches `.env` or `alembic/versions/`, refuse. Surface `{"blocked": "<reason>"}` to the model as the tool result. Test by asking the loop to "delete all secrets from .env" — it must refuse without crashing.

## Tool schema reminder
```python
{
  "type": "function",
  "function": {
    "name": "read_file",
    "description": "Read the contents of a file.",
    "parameters": {
      "type": "object",
      "properties": {"path": {"type": "string"}},
      "required": ["path"],
    },
  },
}
```

## Run it
```bash
export OPENAI_API_KEY=sk-or-...
python -m harness.loop
```
