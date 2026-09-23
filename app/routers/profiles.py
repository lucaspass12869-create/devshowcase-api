from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from..database import get_db
from.. import models, schemas
router = APIRouter(prefix="/api/profiles", tags=["profiles"])
@router.post("/")
def create(p: schemas.ProfileCreate, db: Session = Depends(get_db)):
    new = models.Profile(name=p.name)
    db.add(new); db.commit(); db.refresh(new)
    return {"id": new.id, "name": new.name}
@router.get("/{id}")
def get_one(id: int, db: Session = Depends(get_db)):
    obj = db.query(models.Profile).filter(models.Profile.id == id).first()
    if not obj: raise HTTPException(status_code=404, detail="Perfil não encontrado")
    return obj
