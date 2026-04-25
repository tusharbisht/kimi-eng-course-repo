from fastapi import FastAPI

from app.api import orders

app = FastAPI(title="Streamflow Course API")
app.include_router(orders.router)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
