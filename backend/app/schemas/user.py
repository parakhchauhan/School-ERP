from pydantic import BaseModel, EmailStr

class AdminCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    contact: str

class AdminLogin(BaseModel):
    email: EmailStr
    password: str

class AdminOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    contact: str

class Config:
    from_attributes = True
