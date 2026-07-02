
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
import app.models
import asyncio

app = FastAPI(title="HIRO API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

from app.api.jd_routes import router as jd_router
from app.api.planner_routes import router as planner_router
app.include_router(jd_router)
app.include_router(planner_router)

@app.get("/")
def root():
    return {"message": "HIRO Backend Running 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}
