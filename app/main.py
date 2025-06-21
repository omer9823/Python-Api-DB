from fastapi import FastAPI, Depends
from app.schemas import schemas

app = FastAPI(title="Python-API-DB", version="0.1.0")

@app.get("/health", summary="Health-check")
async def health():
    return {"status": "OK"}

