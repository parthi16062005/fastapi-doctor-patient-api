# FastAPI Doctor and Patient API

## Project Overview

This project is a simple **REST API application** developed using **FastAPI** and Python.

The application provides APIs to manage **Doctors and Patients** using in-memory storage.

## Technologies Used

* Python 3.9+
* FastAPI
* Pydantic
* Uvicorn
* Email Validator

## Project Structure

```text
fastapi_assignment/
│
├── main.py
├── doctor.py
├── patient.py
├── README.md
└── venv/
```

### File Description

* **main.py** – Main FastAPI application and router connection.
* **doctor.py** – Doctor model, storage, and Doctor APIs.
* **patient.py** – Patient model, storage, and Patient APIs.
* **README.md** – Project and setup instructions.

## API Endpoints

### Doctor APIs

| Method | Endpoint               | Description         |
| ------ | ---------------------- | ------------------- |
| POST   | `/doctors`             | Create a new doctor |
| GET    | `/doctors`             | Get all doctors     |
| GET    | `/doctors/{doctor_id}` | Get doctor by ID    |

### Patient APIs

| Method | Endpoint    | Description          |
| ------ | ----------- | -------------------- |
| POST   | `/patients` | Create a new patient |
| GET    | `/patients` | Get all patients     |

## Data Validation

The project uses **Pydantic** for request validation.

* Doctor email must be a valid email address.
* Patient age must be greater than 0.
* Invalid input returns a validation error.
* `HTTPException` is used for errors such as a doctor not being found.

## Storage

The application uses **in-memory storage** with Python lists.

```python
doctors = []
patients = []
```

Data remains available while the application is running. Since the data is stored in memory, it will be cleared when the server is restarted.

## Installation and Setup

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install fastapi uvicorn email-validator
```

### 4. Start the FastAPI server

```bash
uvicorn main:app --reload
```

### 5. Open Swagger UI

Open the following URL in a browser:

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides an interactive interface to test all the API endpoints.

## Example Request

### Create Doctor

```json
{
  "name": "Dr. Kumar",
  "specialization": "Cardiologist",
  "email": "kumar@gmail.com",
  "is_active": true
}
```

### Create Patient

```json
{
  "name": "Arun",
  "age": 25,
  "phone": "9876543210"
}
```

