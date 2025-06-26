from sqlalchemy import Column, Integer, String, Date, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(Date)
    gender = Column(String)
    nationality = Column(String)
    blood_group = Column(String, nullable=True)
    aadhar_no = Column(String, nullable=True)
    profile_photo_url = Column(String, nullable=True)
    status = Column(String, default="Active")

    guardian = relationship("Guardian", back_populates="student", uselist=False)
    academic = relationship("AcademicInfo", back_populates="student", uselist=False)

class Guardian(Base):
    __tablename__ = "guardians"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    father_name = Column(String)
    father_phone = Column(String)
    mother_name = Column(String)
    mother_phone = Column(String)
    student = relationship("Student", back_populates="guardian")

class AcademicInfo(Base):
    __tablename__ = "academic_info"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    roll_number = Column(String)
    class_name = Column(String)
    section = Column(String)
    admission_date = Column(Date)
    house = Column(String, nullable=True)
    student = relationship("Student", back_populates="academic")