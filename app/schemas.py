from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
class ProfileCreate(BaseModel):
    name: str = Field(..., min_length=3)
class TechCreate(BaseModel):
    name: str = Field(..., min_length=2)
class ProjectCreate(BaseModel):
    title: str = Field(..., min_length=3)
    link: Optional[HttpUrl] = None
    profile_id: int
