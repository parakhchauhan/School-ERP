from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class StudentCreate(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    dob: date
    gender: str
    blood_group: Optional[str]
    nationality: str
    aadhar_number: Optional[str]
    email: EmailStr
    mobile: str
    city: str
    state: str
    country: str
    postal_code: str