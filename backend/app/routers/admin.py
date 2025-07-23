from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.user import Admin
from app.schemas.user import AdminOut

router = APIRouter(prefix="/api", tags=["Admins"])

@router.get("/admins", response_model=list[AdminOut])
def get_all_admins(db: Session = Depends(get_db)):
    return db.query(Admin).all()