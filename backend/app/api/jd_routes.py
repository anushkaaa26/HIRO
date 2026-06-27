from fastapi import APIRouter

from app.schemas.jd_schema import (
    JDParseRequest,
    JDParseResponse
)

from app.services.jd_parser_service import parse_job_description

router = APIRouter(prefix="/jd", tags=["JD Parser"])


@router.post("/parse", response_model=JDParseResponse)
def parse_jd(request: JDParseRequest):
    return parse_job_description(request.job_description)