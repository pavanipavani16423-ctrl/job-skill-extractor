from pydantic import BaseModel
from typing import List

class JobExtraction(BaseModel):
    job_title: str
    required_skills: List[str]
    experience: str
    education: str
    tools_technologies: List[str]
    soft_skills: List[str]