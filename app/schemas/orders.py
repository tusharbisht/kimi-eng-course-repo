"""Pydantic v2 schemas for POST /orders capstone."""
from __future__ import annotations

from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field, field_validator


class CreateOrderRequest(BaseModel):
    customer_id: int = Field(..., gt=0)
    product_ids: list[int] = Field(..., min_length=1, max_length=50)
    total_amount: Decimal = Field(..., gt=0)

    @field_validator("product_ids")
    @classmethod
    def validate_product_ids_positive(cls, v: list[int]) -> list[int]:
        if not all(pid > 0 for pid in v):
            raise ValueError("all product_ids must be positive")
        return v


class OrderResponse(BaseModel):
    id: int
    customer_id: int
    total_amount: Decimal
    created_at: datetime
