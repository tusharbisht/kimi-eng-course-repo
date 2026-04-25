"""Smoke test for OrderService.

Module 1 task: don't write the integration test yet — fix the N+1 first
with Aider+Kimi. The full integration test (with Testcontainers) lives in
M3 onwards.
"""
import pytest


def test_smoke_compiles() -> None:
    """Trivial — the real N+1 detection lives in M3.S2 once you've
    written AGENTS.md and rerun Aider with the right context."""
    from app.services.order_service import OrderService  # noqa: F401

    assert True, "OrderService import works"
