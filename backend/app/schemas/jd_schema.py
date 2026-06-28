from pydantic import BaseModel
from typing import List, Optional


class JDParseRequest(BaseModel):
    job_description: str




class JDParseResponse(BaseModel):
    company: str
    role: str
    skills: List[str]
    experience: Optional[str] = None
    location: Optional[str] = None
    employment_type: Optional[str] = None
    deadline: Optional[str] = None
