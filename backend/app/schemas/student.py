from pydantic import BaseModel
from datetime import date
from typing import Optional
from typing import List
from pydantic import BaseModel, EmailStr



class AdminCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    contact: str

class GuardianBase(BaseModel):
    father_name: str
    father_phone: str
    mother_name: str
    mother_phone: str

class AcademicBase(BaseModel):
    roll_number: str
    class_name: str
    section: str
    admission_date: date
    house: Optional[str] = None

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    dob: date
    gender: str
    nationality: str
    blood_group: Optional[str]
    aadhar_no: Optional[str]
    profile_photo_url: Optional[str]
    status: Optional[str] = "Active"
    guardian: GuardianBase
    academic: AcademicBase

class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    dob: date
    gender: str
    nationality: str
    blood_group: Optional[str]
    aadhar_no: Optional[str]
    profile_photo_url: Optional[str]
    status: Optional[str]
    guardian: Optional[GuardianBase]
    academic: Optional[AcademicBase]

class Config:
    orm_mode = True

class StudentList(BaseModel):
    students: List[StudentResponse]
