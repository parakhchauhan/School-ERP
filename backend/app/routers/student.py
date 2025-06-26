from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.student import StudentCreate, StudentResponse, StudentList, GuardianBase, AcademicBase
from app.db import get_db
from app.models import student as models

router = APIRouter()

@router.post("/students")
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    new_student = models.Student(
        first_name=data.first_name,
        last_name=data.last_name,
        dob=data.dob,
        gender=data.gender,
        nationality=data.nationality,
        blood_group=data.blood_group,
        aadhar_no=data.aadhar_no,
        profile_photo_url=data.profile_photo_url,
        status=data.status
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    new_guardian = models.Guardian(
        student_id=new_student.id,
        father_name=data.guardian.father_name,
        father_phone=data.guardian.father_phone,
        mother_name=data.guardian.mother_name,
        mother_phone=data.guardian.mother_phone
    )
    db.add(new_guardian)

    new_academic = models.AcademicInfo(
        student_id=new_student.id,
        roll_number=data.academic.roll_number,
        class_name=data.academic.class_name,
        section=data.academic.section,
        admission_date=data.academic.admission_date,
        house=data.academic.house
    )
    db.add(new_academic)

    db.commit()

    return {
        "message": "Student saved successfully 🎉",
        "student_id": new_student.id
    }

@router.get("/students", response_model=StudentList)
def get_all_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    response = []

    for s in students:
        guardian_data = None
        if s.guardian:
            guardian_data = GuardianBase(
                father_name=s.guardian.father_name,
                father_phone=s.guardian.father_phone,
                mother_name=s.guardian.mother_name,
                mother_phone=s.guardian.mother_phone
            )

        academic_data = None
        if s.academic:
            academic_data = AcademicBase(
                roll_number=s.academic.roll_number,
                class_name=s.academic.class_name,
                section=s.academic.section,
                admission_date=s.academic.admission_date,
                house=s.academic.house
            )

        response.append(StudentResponse(
            id=s.id,
            first_name=s.first_name,
            last_name=s.last_name,
            dob=s.dob,
            gender=s.gender,
            nationality=s.nationality,
            blood_group=s.blood_group,
            aadhar_no=s.aadhar_no,
            profile_photo_url=s.profile_photo_url,
            status=s.status,
            guardian=guardian_data,
            academic=academic_data
        ))
    return {"students": response}

@router.get("/students/{student_id}", response_model=StudentResponse)
def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    guardian_data = None
    if student.guardian:
        guardian_data = GuardianBase(
            father_name=student.guardian.father_name,
            father_phone=student.guardian.father_phone,
            mother_name=student.guardian.mother_name,
            mother_phone=student.guardian.mother_phone
        )

    academic_data = None
    if student.academic:
        academic_data = AcademicBase(
            roll_number=student.academic.roll_number,
            class_name=student.academic.class_name,
            section=student.academic.section,
            admission_date=student.academic.admission_date,
            house=student.academic.house
        )

    return StudentResponse(
        id=student.id,
        first_name=student.first_name,
        last_name=student.last_name,
        dob=student.dob,
        gender=student.gender,
        nationality=student.nationality,
        blood_group=student.blood_group,
        aadhar_no=student.aadhar_no,
        profile_photo_url=student.profile_photo_url,
        status=student.status,
        guardian=guardian_data,
        academic=academic_data
    )