from fastapi import FastAPI

app = FastAPI(title="Streamflow Course API")

@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
