from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.models.user import Admin
from app.schemas.user import AdminCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_admin(db: Session, admin: AdminCreate):
    new_admin = Admin(
        name=admin.name,
        email=admin.email,
        hashed_password=get_password_hash(admin.password),
        contact=admin.contact
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin