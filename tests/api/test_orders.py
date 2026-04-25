"""CAPSTONE INTEGRATION TEST STUB — extend with @pytest.mark.integration
+ Testcontainers (Postgres) + httpx.AsyncClient. You MUST cover at least:

  (a) Happy path: POST /orders with a valid body + Idempotency-Key returns 201 + the OrderResponse.
  (b) Validation failure: missing customer_id returns 422.
  (c) Idempotency replay: same Idempotency-Key + same body returns 200 + the SAME OrderResponse.
  (d) Idempotency conflict: same Idempotency-Key + DIFFERENT body returns 409.

The lab-grade.yml GHA workflow runs `pytest -q --cov=app --cov-fail-under=80`
+ ruff check + mypy strict. This file fails on purpose right now.
"""
import pytest


def test_capstone_is_unfinished() -> None:
    pytest.fail(
        "CAPSTONE TODO — implement the 4 integration-test scenarios "
        "described in this module's docstring."
    )
