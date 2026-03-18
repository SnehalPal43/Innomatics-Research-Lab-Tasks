# 🩺 Medical Appointment System (FastAPI Project)

## 📌 Project Description
This project is a FastAPI-based backend application designed to manage medical appointments.  
It allows users to perform operations on patients, doctors, and appointments with proper validation and workflow.

---

## 🚀 Features

- Patient Management (Create, Read, Update, Delete)
- Doctor Management (Create, Read, Update, Delete)
- Appointment Booking System
- Pydantic Data Validation
- Search Patients by Name
- Filter Appointments by Date
- Sort Doctors by Experience
- Pagination for Patient Records
- Doctor Availability Check

---

## 🛠 Tech Stack

- Python
- FastAPI
- Uvicorn

---

## 📂 API Endpoints

### Patient APIs
- POST /patients
- GET /patients
- GET /patients/{id}
- PUT /patients/{id}
- DELETE /patients/{id}

### Doctor APIs
- POST /doctors
- GET /doctors
- GET /doctors/{id}
- PUT /doctors/{id}
- DELETE /doctors/{id}

### Appointment APIs
- POST /appointments
- GET /appointments
- GET /appointments/{id}
- DELETE /appointments/{id}
- GET /appointments/patient/{pid}

### Additional Features
- GET /search_patient
- GET /filter_appointments
- GET /sort_doctors
- GET /paginate_patients
- GET /doctor_available/{doctor_id}

---

## ▶️ How to Run the Project

1. Install dependencies: