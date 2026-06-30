from pydantic import BaseModel, EmailStr
from typing import List, Optional


class Project(BaseModel):
    title: str
    description: str
    technologies: List[str]


class UserProfile(BaseModel):
    full_name: str
    email: EmailStr
    college: str
    graduation_year: int

    target_roles: List[str]
    preferred_locations: List[str]

    skills: List[str]

    projects: List[Project]

    github: Optional[str] = None
    linkedin: Optional[str] = None
    portfolio: Optional[str] = None