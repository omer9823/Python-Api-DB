from fastapi import FastAPI, Depends
from .routers import user_router

app = FastAPI(title="Python-API-DB", version="0.1.0")
app.include_router(user_router.router)

@app.get("/health", summary="Health-check")
async def health():
    return {"status": "OK"}

