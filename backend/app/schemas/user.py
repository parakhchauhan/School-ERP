from pydantic import BaseModel, EmailStr

class AdminCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    contact: str

class AdminLogin(BaseModel):
    email: str
    password: str