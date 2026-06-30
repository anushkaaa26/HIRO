from fastapi import APIRouter
from pydantic import BaseModel

from app.planner.workflows import apply_workflow

router = APIRouter(
    prefix="/planner",
    tags=["Planner"]
)

class PlannerRequest(BaseModel):
    job_description: str


@router.post("/apply")
def apply(request: PlannerRequest):
    return apply_workflow(request.job_description)