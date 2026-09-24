from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class Patient(BaseModel):
    name: str
    age: int = Field(gt=0)
    phone: str


patients = []


@router.post("/patients")
def create_patient(patient: Patient):
    patient_data = patient.model_dump()
    patient_data["id"] = len(patients) + 1
    patients.append(patient_data)
    return patient_data


@router.get("/patients")
def get_patients():
    return patients