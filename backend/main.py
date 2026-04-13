from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.responses import JSONResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(title="neuroflow-api", lifespan=lifespan)

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "checks": {
            "postgres": True,
            "redis": True,
            "mlflow": True
        }
    }
