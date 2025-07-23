from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.student import StudentCreate, StudentResponse, StudentList, GuardianBase, AcademicBase, FeeTransportBase, DocumentsBase
from app.db import get_db
from app.models import student as models

router = APIRouter()

@router.post("/students")
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    # Create student record
    new_student = models.Student(
        first_name=data.first_name,
        middle_name=data.middle_name,
        last_name=data.last_name,
        dob=data.dob,
        gender=data.gender,
        nationality=data.nationality,
        blood_group=data.blood_group,
        aadhar_no=data.aadhar_no,
        profile_photo_url=data.profile_photo_url,
        mobile=data.mobile,
        email=data.email,
        present_address=data.present_address,
        permanent_address=data.permanent_address,
        city_state_country=data.city_state_country,
        zip_code=data.zip_code,
        status=data.status
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    # Create guardian record
    new_guardian = models.Guardian(
        student_id=new_student.id,
        father_name=data.guardian.father_name,
        father_occupation=data.guardian.father_occupation,
        father_phone=data.guardian.father_phone,
        mother_name=data.guardian.mother_name,
        mother_occupation=data.guardian.mother_occupation,
        mother_phone=data.guardian.mother_phone,
        emergency_contact_person=data.guardian.emergency_contact_person,
        emergency_contact_number=data.guardian.emergency_contact_number
    )
    db.add(new_guardian)

    # Create academic info record
    new_academic = models.AcademicInfo(
        student_id=new_student.id,
        admission_number=data.academic.admission_number,
        admission_date=data.academic.admission_date,
        roll_number=data.academic.roll_number,
        class_name=data.academic.class_name,
        section=data.academic.section,
        previous_school=data.academic.previous_school,
        transfer_certificate=data.academic.transfer_certificate,
        house=data.academic.house
    )
    db.add(new_academic)

    # Create fee/transport info if provided
    if data.fee_transport:
        new_fee_transport = models.FeeTransportInfo(
            student_id=new_student.id,
            fee_plan=data.fee_transport.fee_plan,
            transport_route=data.fee_transport.transport_route,
            hostel_room=data.fee_transport.hostel_room
        )
        db.add(new_fee_transport)

    # Create documents info if provided
    if data.documents:
        new_documents = models.StudentDocuments(
            student_id=new_student.id,
            birth_certificate=data.documents.birth_certificate,
            passport_photo=data.documents.passport_photo,
            transfer_certificate_doc=data.documents.transfer_certificate_doc,
            aadhar_proof=data.documents.aadhar_proof,
            signature=data.documents.signature
        )
        db.add(new_documents)

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
                father_occupation=s.guardian.father_occupation,
                father_phone=s.guardian.father_phone,
                mother_name=s.guardian.mother_name,
                mother_occupation=s.guardian.mother_occupation,
                mother_phone=s.guardian.mother_phone,
                emergency_contact_person=s.guardian.emergency_contact_person,
                emergency_contact_number=s.guardian.emergency_contact_number
            )

        academic_data = None
        if s.academic:
            academic_data = AcademicBase(
                admission_number=s.academic.admission_number,
                admission_date=s.academic.admission_date,
                roll_number=s.academic.roll_number,
                class_name=s.academic.class_name,
                section=s.academic.section,
                previous_school=s.academic.previous_school,
                transfer_certificate=s.academic.transfer_certificate,
                house=s.academic.house
            )

        fee_transport_data = None
        if s.fee_transport:
            fee_transport_data = FeeTransportBase(
                fee_plan=s.fee_transport.fee_plan,
                transport_route=s.fee_transport.transport_route,
                hostel_room=s.fee_transport.hostel_room
            )

        documents_data = None
        if s.documents:
            documents_data = DocumentsBase(
                birth_certificate=s.documents.birth_certificate,
                passport_photo=s.documents.passport_photo,
                transfer_certificate_doc=s.documents.transfer_certificate_doc,
                aadhar_proof=s.documents.aadhar_proof,
                signature=s.documents.signature
            )

        response.append(StudentResponse(
            id=s.id,
            first_name=s.first_name,
            middle_name=s.middle_name,
            last_name=s.last_name,
            dob=s.dob,
            gender=s.gender,
            nationality=s.nationality,
            blood_group=s.blood_group,
            aadhar_no=s.aadhar_no,
            profile_photo_url=s.profile_photo_url,
            mobile=s.mobile,
            email=s.email,
            present_address=s.present_address,
            permanent_address=s.permanent_address,
            city_state_country=s.city_state_country,
            zip_code=s.zip_code,
            status=s.status,
            guardian=guardian_data,
            academic=academic_data,
            fee_transport=fee_transport_data,
            documents=documents_data
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
            father_occupation=student.guardian.father_occupation,
            father_phone=student.guardian.father_phone,
            mother_name=student.guardian.mother_name,
            mother_occupation=student.guardian.mother_occupation,
            mother_phone=student.guardian.mother_phone,
            emergency_contact_person=student.guardian.emergency_contact_person,
            emergency_contact_number=student.guardian.emergency_contact_number
        )

    academic_data = None
    if student.academic:
        academic_data = AcademicBase(
            admission_number=student.academic.admission_number,
            admission_date=student.academic.admission_date,
            roll_number=student.academic.roll_number,
            class_name=student.academic.class_name,
            section=student.academic.section,
            previous_school=student.academic.previous_school,
            transfer_certificate=student.academic.transfer_certificate,
            house=student.academic.house
        )

    fee_transport_data = None
    if student.fee_transport:
        fee_transport_data = FeeTransportBase(
            fee_plan=student.fee_transport.fee_plan,
            transport_route=student.fee_transport.transport_route,
            hostel_room=student.fee_transport.hostel_room
        )

    documents_data = None
    if student.documents:
        documents_data = DocumentsBase(
            birth_certificate=student.documents.birth_certificate,
            passport_photo=student.documents.passport_photo,
            transfer_certificate_doc=student.documents.transfer_certificate_doc,
            aadhar_proof=student.documents.aadhar_proof,
            signature=student.documents.signature
        )

    return StudentResponse(
        id=student.id,
        first_name=student.first_name,
        middle_name=student.middle_name,
        last_name=student.last_name,
        dob=student.dob,
        gender=student.gender,
        nationality=student.nationality,
        blood_group=student.blood_group,
        aadhar_no=student.aadhar_no,
        profile_photo_url=student.profile_photo_url,
        mobile=student.mobile,
        email=student.email,
        present_address=student.present_address,
        permanent_address=student.permanent_address,
        city_state_country=student.city_state_country,
        zip_code=student.zip_code,
        status=student.status,
        guardian=guardian_data,
        academic=academic_data,
        fee_transport=fee_transport_data,
        documents=documents_data
    )
