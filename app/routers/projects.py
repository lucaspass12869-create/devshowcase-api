from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from..database import get_db
from.. import models, schemas
router = APIRouter(prefix="/api/projects", tags=["projects"])
@router.post("/")
def create(p: schemas.ProjectCreate, db: Session = Depends(get_db)):
    if not db.query(models.Profile).filter(models.Profile.id == p.profile_id).first():
        raise HTTPException(status_code=404, detail="profile_id não existe")
    new = models.Project(title=p.title, link=str(p.link) if p.link else None, profile_id=p.profile_id)
    db.add(new); db.commit(); db.refresh(new)
    return {"id": new.id, "title": new.title, "link": new.link, "profile_id": new.profile_id}
@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return db.query(models.Project).all()
