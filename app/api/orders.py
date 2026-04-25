"""CAPSTONE — finish this endpoint to production grade.

Requirements (the lab-grade.yml GHA workflow tests all of these):

  1. POST /orders accepts a CreateOrderRequest JSON body.
  2. If validation fails, FastAPI returns 422 (default Pydantic behavior).
  3. Idempotency: the client sends an "Idempotency-Key" header.
       - If a prior request with the SAME key + same body succeeded → return 200 + the original OrderResponse.
       - If a prior request with the SAME key is still processing → return 409.
       - Otherwise persist atomically + return 201.
     Storage: Postgres table idempotency_keys(key TEXT PRIMARY KEY, request_hash TEXT, response_body JSONB, status_code INT, created_at TIMESTAMPTZ).
  4. Use async transactions (`async with session.begin()`) — order + idempotency row commit atomically.
  5. NO N+1 queries when loading related entities.
  6. Integration tests use Testcontainers + real Postgres, NOT in-memory SQLite.
"""
from __future__ import annotations

from fastapi import APIRouter, Header, status

from app.schemas.orders import CreateOrderRequest, OrderResponse

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(
    request: CreateOrderRequest,
    idempotency_key: str = Header(..., alias="Idempotency-Key"),
) -> OrderResponse:
    # TODO: implement idempotency check (201/200/409), persistence, atomic commit
    raise NotImplementedError("CAPSTONE TODO — implement this endpoint")
