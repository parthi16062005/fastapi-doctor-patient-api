from fastapi import FastAPI
from doctor import router as doctor_router
from patient import router as patient_router

app = FastAPI(title="Doctor & Patient Management API")


@app.get("/")
def home():
    return {"message": "Doctor & Patient Management API is working!"}


app.include_router(doctor_router)
app.include_router(patient_router)