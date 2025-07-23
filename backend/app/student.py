from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional, List

class GuardianBase(BaseModel):
    father_name: str
    father_occupation: Optional[str] = None
    father_phone: str
    mother_name: str
    mother_occupation: Optional[str] = None
    mother_phone: str
    emergency_contact_person: Optional[str] = None
    emergency_contact_number: Optional[str] = None

class AcademicBase(BaseModel):
    admission_number: Optional[str] = None
    admission_date: date
    roll_number: str
    class_name: str
    section: str
    previous_school: Optional[str] = None
    transfer_certificate: Optional[str] = None
    house: Optional[str] = None

class FeeTransportBase(BaseModel):
    fee_plan: Optional[str] = None
    transport_route: Optional[str] = None
    hostel_room: Optional[str] = None

class DocumentsBase(BaseModel):
    birth_certificate: Optional[str] = None
    passport_photo: Optional[str] = None
    transfer_certificate_doc: Optional[str] = None
    aadhar_proof: Optional[str] = None
    signature: Optional[str] = None

class StudentCreate(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    dob: date
    gender: str
    nationality: str
    blood_group: Optional[str] = None
    aadhar_no: Optional[str] = None
    profile_photo_url: Optional[str] = None
    mobile: Optional[str] = None
    email: Optional[str] = None
    present_address: Optional[str] = None
    permanent_address: Optional[str] = None
    city_state_country: Optional[str] = None
    zip_code: Optional[str] = None
    status: Optional[str] = "Active"
    guardian: GuardianBase
    academic: AcademicBase
    fee_transport: Optional[FeeTransportBase] = None
    documents: Optional[DocumentsBase] = None

class StudentResponse(BaseModel):
    id: int
    first_name: str
    middle_name: Optional[str]
    last_name: str
    dob: date
    gender: str
    nationality: str
    blood_group: Optional[str]
    aadhar_no: Optional[str]
    profile_photo_url: Optional[str]
    mobile: Optional[str]
    email: Optional[str]
    present_address: Optional[str]
    permanent_address: Optional[str]
    city_state_country: Optional[str]
    zip_code: Optional[str]
    status: Optional[str]
    guardian: Optional[GuardianBase]
    academic: Optional[AcademicBase]
    fee_transport: Optional[FeeTransportBase]
    documents: Optional[DocumentsBase]

    class Config:
        orm_mode = True

class StudentList(BaseModel):
    students: List[StudentResponse]
