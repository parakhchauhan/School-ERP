from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.schemas.user import AdminCreate, AdminLogin
from app.schemas.token import Token
from app.crud.user import create_admin
from app.models.user import Admin
from app.db import get_db
from app.auth.jwt import create_access_token
from app.schemas.user import AdminOut


router = APIRouter(prefix="/api", tags=["Auth"])


router = APIRouter(prefix="/api", tags=["Admins"])

@router.get("/admins", response_model=list[AdminOut])
def get_all_admins(db: Session = Depends(get_db)):
    return db.query(Admin).all()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/register")
def register_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    existing = db.query(Admin).filter(Admin.email == admin.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Admin with this email already exists."
        )
    return create_admin(db, admin)

@router.post("/login", response_model=Token)
def login(admin: AdminLogin, db: Session = Depends(get_db)):
    user = db.query(Admin).filter(Admin.email == admin.email).first()
    if not user or not verify_password(admin.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}


from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.models.user import Admin

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

SECRET_KEY = "your-super-secret-key"  # Same one used in JWT creation
ALGORITHM = "HS256"


@router.get("/me")
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Token payload missing email")

        user = db.query(Admin).filter(Admin.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="Admin not found")

        return {"name": user.name, "email": user.email}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")