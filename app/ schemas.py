app/schemas.py`
Apaga TUDO e cola:
from pydantic import BaseModel, Field
from typing import List, Optional

class TechnologyCreate(BaseModel):
    name: str
class TechnologyOut(TechnologyCreate):
    id: int
    class Config:
        from_attributes = True

class ProfileCreate(BaseModel):
    bio: str
    github_url: str
class ProfileOut(ProfileCreate):
    id: int
    class Config:
        from_attributes = True

class FeedbackCreate(BaseModel):
    note: int = Field(..., ge=1, le=5, description="Nota 1 a 5")
    comments: Optional[str] = None
class FeedbackOut(FeedbackCreate):
    id: int
    project_id: int
    class Config:
        from_attributes = True

class ProjectCreate(BaseModel):
    title: str = Field(..., max_length=150)
    description: str
    repo_url: str
    profile_id: int
    technologies: List[int] = []
class ProjectOut(BaseModel):
    id: int
    title: str
    description: str
    repo_url: str
    stars: int
    average_rating: float
    profile_id: int
    technologies: List[TechnologyOut] = []
    feedbacks: List[FeedbackOut] = []
    class Config:
        from_attributes = True
