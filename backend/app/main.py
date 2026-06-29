from fastapi import FastAPI
from app.api.jd_routes import router as jd_router




app = FastAPI(
    title="HIRO API",
    version="1.0.0"
)

app.include_router(jd_router)


@app.get("/")
def root():
    return {
        "message": "HIRO Backend Running 🚀"
    }
