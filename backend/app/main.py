from fastapi import FastAPI
from app.api.jd_routes import router as jd_router
from app.api.planner_routes import router as planner_router




app = FastAPI(
    title="HIRO API",
    version="1.0.0"
)

app.include_router(jd_router)
app.include_router(planner_router)

@app.get("/")
def root():
    return {
        "message": "HIRO Backend Running 🚀"
    }
