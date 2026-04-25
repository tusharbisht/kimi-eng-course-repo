# Module 6 — Capstone: Ship POST /orders via GitHub Actions

**Goal:** ship a production-grade `POST /orders` endpoint that passes:
- Pydantic v2 input validation
- Idempotency-Key handling (201 / 200 / 409)
- Testcontainers-backed integration tests (NOT SQLite)
- `pytest --cov-fail-under=80` + ruff + mypy strict
- GHA `lab-grade.yml` runs all of the above on every push

## Flow
1. Fork this repo on your own GitHub.
2. `git checkout module-6-capstone && uv pip install -e ".[dev]" && pytest -q` — starter tests fail on purpose (`test_capstone_is_unfinished`).
3. Use Aider+Kimi to implement:
   - `app/api/orders.py::create_order` (idempotency + persistence)
   - `app/db/idempotency.py` (model + repository for the idempotency_keys table)
   - `tests/api/test_orders.py` (4 integration scenarios above)
   For the capstone, pin to `kimi-k2-latest` if you want the freshest snapshot:
   ```
   aider --model openai/moonshotai/kimi-k2-latest \
     --openai-api-base https://openrouter.ai/api/v1
   ```
4. `git commit -am "capstone: POST /orders with idempotency"` and `git push origin module-6-capstone` (or any branch).
5. GHA runs `lab-grade.yml` automatically. Watch the Actions tab on YOUR fork.
6. Paste the run URL (`https://github.com/<your-fork>/actions/runs/<id>`) into the course's capstone submit textarea.

## Idempotency contract
- Client sends `Idempotency-Key: <uuid>` on every request.
- Same key + same body (within 24h) → 200 + original OrderResponse body.
- Same key + different body → 409 Conflict.
- Key not seen → persist order + key atomically → 201.

Postgres schema:
```sql
CREATE TABLE idempotency_keys (
    key TEXT PRIMARY KEY,
    request_hash TEXT NOT NULL,
    response_body JSONB,
    status_code INT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

## Pass = GHA conclusion `success`
The course's grader polls the run URL you paste; the `grade` job must complete successfully.
