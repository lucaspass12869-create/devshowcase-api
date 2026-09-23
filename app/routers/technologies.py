from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from..database import get_db
from.. import models, schemas
router = APIRouter(prefix="/api/technologies", tags=["technologies"])
@router.post("/")
def create(t: schemas.TechCreate, db: Session = Depends(get_db)):
    new = models.Technology(name=t.name)
    db.add(new); db.commit(); db.refresh(new)
    return {"id": new.id, "name": new.name}
@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return db.query(models.Technology).all()
