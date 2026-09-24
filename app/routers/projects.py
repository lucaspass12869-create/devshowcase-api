from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
import app.models as models
import app.schemas as schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.ProjectOut)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = models.Project(title=project.title, description=project.description, repo_url=project.repo_url, profile_id=project.profile_id)
    if project.technologies:
        techs = db.query(models.Technology).filter(models.Technology.id.in_(project.technologies)).all()
        db_project.technologies = techs
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@router.get("/", response_model=List[schemas.ProjectOut])
def list_projects(tecnologia: Optional[str] = Query(None), search: Optional[str] = Query(None), page: int = Query(1, ge=1), size: int = Query(10, ge=1, le=50), db: Session = Depends(get_db)):
    query = db.query(models.Project)
    if tecnologia:
        query = query.join(models.Project.technologies).filter(models.Technology.name == tecnologia)
    if search:
        query = query.filter(models.Project.title.contains(search))
    return query.offset((page-1)*size).limit(size).all()

@router.get("/{project_id}", response_model=schemas.ProjectOut)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return project

@router.put("/{project_id}/upvote", response_model=schemas.ProjectOut)
def upvote_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    project.stars += 1
    db.commit()
    db.refresh(project)
    return project

@router.post("/{project_id}/feedback", response_model=schemas.FeedbackOut, status_code=201)
def create_feedback(project_id: int, feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    db_feedback = models.Feedback(note=feedback.note, comments=feedback.comments, project_id=project_id)
    db.add(db_feedback)
    db.commit()
    all_notes = db.query(models.Feedback).filter(models.Feedback.project_id == project_id).all()
    project.average_rating = sum([f.note for f in all_notes]) / len(all_notes)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback
Commit: 
