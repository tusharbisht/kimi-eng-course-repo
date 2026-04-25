from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.order import Order


@dataclass
class OrderSummary:
    """Returned by get_recent_orders — bundles order + customer name."""

    id: int
    customer_name: str
    total: Decimal
    created_at: datetime


class OrderService:
    """Service for read-side order operations.

    PLANTED BUG (intentional — module 1): get_recent_orders triggers an
    N+1 query. The .customer relationship is lazy="select", so for every
    order we yield, SQLAlchemy issues an extra SELECT to fetch the customer.
    21 queries for 20 orders.

    The right fix (after M2's AGENTS.md teaches team conventions): use
    selectinload(Order.customer) on the select() statement so customers
    load in a single batched query.
    """

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_recent_orders(self, limit: int = 20) -> list[OrderSummary]:
        result = await self._session.execute(
            select(Order).order_by(Order.created_at.desc()).limit(limit)
        )
        orders = result.scalars().all()
        return [
            OrderSummary(
                id=o.id,
                customer_name=o.customer.name,  # ← triggers per-order lazy load (N+1)
                total=o.total,
                created_at=o.created_at,
            )
            for o in orders
        ]
