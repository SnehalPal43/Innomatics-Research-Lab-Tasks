from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import date

app = FastAPI()

# ------------------ MODELS ------------------

class Patient(BaseModel):
    name: str
    age: int = Field(gt=0)
    gender: str

class Doctor(BaseModel):
    name: str
    specialization: str
    experience: int

class Appointment(BaseModel):
    patient_id: int
    doctor_id: int
    date: date

# ------------------ DATABASE ------------------

patients = []
doctors = []
appointments = []

# ------------------ PATIENT APIs ------------------

@app.post("/patients")
def add_patient(patient: Patient):
    patients.append(patient)
    return {"message": "Patient added"}

@app.get("/patients")
def get_patients():
    return patients

@app.get("/patients/{id}")
def get_patient(id: int):
    return patients[id]

@app.put("/patients/{id}")
def update_patient(id: int, patient: Patient):
    patients[id] = patient
    return {"message": "Updated"}

@app.delete("/patients/{id}")
def delete_patient(id: int):
    patients.pop(id)
    return {"message": "Deleted"}

# ------------------ DOCTOR APIs ------------------

@app.post("/doctors")
def add_doctor(doctor: Doctor):
    doctors.append(doctor)
    return {"message": "Doctor added"}

@app.get("/doctors")
def get_doctors():
    return doctors

@app.get("/doctors/{id}")
def get_doctor(id: int):
    return doctors[id]

@app.put("/doctors/{id}")
def update_doctor(id: int, doctor: Doctor):
    doctors[id] = doctor
    return {"message": "Updated"}

@app.delete("/doctors/{id}")
def delete_doctor(id: int):
    doctors.pop(id)
    return {"message": "Deleted"}

# ------------------ APPOINTMENT APIs ------------------

@app.post("/appointments")
def book_appointment(appo: Appointment):

    if appo.patient_id >= len(patients):
        return {"error": "Patient not found"}

    if appo.doctor_id >= len(doctors):
        return {"error": "Doctor not found"}

    for a in appointments:
        if a.doctor_id == appo.doctor_id and a.date == appo.date:
            return {"error": "Doctor not available"}

    appointments.append(appo)
    return {"message": "Appointment booked"}

@app.get("/appointments")
def get_appointments():
    return appointments

@app.get("/appointments/{id}")
def get_appointment(id: int):
    return appointments[id]

@app.delete("/appointments/{id}")
def delete_appointment(id: int):
    appointments.pop(id)
    return {"message": "Cancelled"}

@app.get("/appointments/patient/{pid}")
def get_by_patient(pid: int):
    return [a for a in appointments if a.patient_id == pid]

# ------------------ EXTRA FEATURES ------------------

@app.get("/search_patient")
def search_patient(name: str):
    return [p for p in patients if name.lower() in p.name.lower()]

@app.get("/filter_appointments")
def filter_by_date(app_date: date):
    return [a for a in appointments if a.date == app_date]

@app.get("/sort_doctors")
def sort_doctors():
    return sorted(doctors, key=lambda x: x.experience, reverse=True)

@app.get("/paginate_patients")
def paginate(page: int = 1, limit: int = 2):
    start = (page - 1) * limit
    end = start + limit
    return patients[start:end]

@app.get("/doctor_available/{doctor_id}")
def check_availability(doctor_id: int, app_date: date):
    for a in appointments:
        if a.doctor_id == doctor_id and a.date == app_date:
            return {"available": False}
    return {"available": True}