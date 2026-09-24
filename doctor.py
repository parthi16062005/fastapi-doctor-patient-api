from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr

router = APIRouter()


class Doctor(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True


doctors = []


@router.post("/doctors")
def create_doctor(doctor: Doctor):
    doctor_data = doctor.model_dump()
    doctor_data["id"] = len(doctors) + 1
    doctors.append(doctor_data)
    return doctor_data


@router.get("/doctors")
def get_doctors():
    return doctors


@router.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):
    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return doctor

    raise HTTPException(status_code=404, detail="Doctor not found")