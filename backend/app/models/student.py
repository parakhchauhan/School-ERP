from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, Decimal
from sqlalchemy.orm import relationship
from .base import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    middle_name = Column(String, nullable=True)
    last_name = Column(String)
    dob = Column(Date)
    gender = Column(String)
    nationality = Column(String)
    blood_group = Column(String, nullable=True)
    aadhar_no = Column(String, nullable=True)
    profile_photo_url = Column(String, nullable=True)
    mobile = Column(String, nullable=True)
    email = Column(String, nullable=True)
    present_address = Column(Text, nullable=True)
    permanent_address = Column(Text, nullable=True)
    city_state_country = Column(String, nullable=True)
    zip_code = Column(String, nullable=True)
    status = Column(String, default="Active")

    guardian = relationship("Guardian", back_populates="student", uselist=False)
    academic = relationship("AcademicInfo", back_populates="student", uselist=False)
    fee_transport = relationship("FeeTransportInfo", back_populates="student", uselist=False)
    documents = relationship("StudentDocuments", back_populates="student", uselist=False)

class Guardian(Base):
    __tablename__ = "guardians"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    father_name = Column(String)
    father_occupation = Column(String, nullable=True)
    father_phone = Column(String)
    mother_name = Column(String)
    mother_occupation = Column(String, nullable=True)
    mother_phone = Column(String)
    emergency_contact_person = Column(String, nullable=True)
    emergency_contact_number = Column(String, nullable=True)
    student = relationship("Student", back_populates="guardian")

class AcademicInfo(Base):
    __tablename__ = "academic_info"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    admission_number = Column(String, nullable=True)
    admission_date = Column(Date)
    roll_number = Column(String)
    class_name = Column(String)
    section = Column(String)
    previous_school = Column(String, nullable=True)
    transfer_certificate = Column(String, nullable=True)
    house = Column(String, nullable=True)
    student = relationship("Student", back_populates="academic")

class FeeTransportInfo(Base):
    __tablename__ = "fee_transport_info"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    fee_plan = Column(String, nullable=True)
    transport_route = Column(String, nullable=True)
    hostel_room = Column(String, nullable=True)
    student = relationship("Student", back_populates="fee_transport")

class StudentDocuments(Base):
    __tablename__ = "student_documents"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    birth_certificate = Column(String, nullable=True)
    passport_photo = Column(String, nullable=True)
    transfer_certificate_doc = Column(String, nullable=True)
    aadhar_proof = Column(String, nullable=True)
    signature = Column(String, nullable=True)
    student = relationship("Student", back_populates="documents")
