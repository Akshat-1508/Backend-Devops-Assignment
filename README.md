# 🚀 Backend DevOps Assignment
### AI-Powered Financial Transaction Processing System

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Redis](https://img.shields.io/badge/Redis-Cache-red?logo=redis)
![Celery](https://img.shields.io/badge/Celery-Background%20Tasks-37814A?logo=celery)
![Gemini](https://img.shields.io/badge/Google-Gemini%20AI-blue)

---

## 📌 Project Overview

This project is an AI-powered backend system that processes financial transaction CSV files asynchronously. Users can upload transaction files through a REST API, after which the system cleans, validates, analyzes, and summarizes the data using Google Gemini AI.

The application is built using **FastAPI**, **PostgreSQL**, **Redis**, **Celery**, **Docker**, and **Google Gemini AI**, following a modular backend architecture suitable for production-style applications.

---

# ✨ Features

- 📂 Upload CSV transaction files
- ⚡ Background processing using Celery
- 🗄 PostgreSQL database integration
- 🔄 Redis message broker
- 🧹 Automatic data cleaning
- 🚨 Anomaly detection
- 🤖 AI-powered financial insights using Google Gemini
- 📊 Job status tracking
- 📄 Report generation
- 🐳 Dockerized deployment
- 📑 Interactive Swagger API documentation

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Background Tasks | Celery |
| Message Broker | Redis |
| AI | Google Gemini API |
| Containerization | Docker & Docker Compose |
| Language | Python 3.11 |

---

# 📁 Project Structure

```
Backend_DevOps_Assignment
│
├── app
│   ├── api
│   │     jobs.py
│   │
│   ├── core
│   │     config.py
│   │     database.py
│   │     celery_app.py
│   │
│   ├── models
│   │     job.py
│   │     transaction.py
│   │     summary.py
│   │
│   ├── schemas
│   │     job_schema.py
│   │
│   ├── services
│   │     cleaner.py
│   │     anomaly.py
│   │     pipeline.py
│   │     llm_service.py
│   │
│   ├── workers
│   │     tasks.py
│   │
│   ├── utils
│   │     helper.py
│   │
│   └── main.py
│
├── uploads
├── reports
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ System Architecture

```
                 User
                   │
                   │ Upload CSV
                   ▼
             FastAPI REST API
                   │
         Creates Processing Job
                   │
                   ▼
             PostgreSQL Database
                   │
                   ▼
              Celery Worker
                   │
         Reads Uploaded CSV
                   │
      Cleans & Validates Data
                   │
         Detects Anomalies
                   │
          Google Gemini AI
                   │
         Generates Summary
                   │
                   ▼
          PostgreSQL + Reports
                   │
                   ▼
           REST API Response
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/backend-devops-assignment.git

cd backend-devops-assignment
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/backenddb

REDIS_URL=redis://redis:6379/0

GEMINI_API_KEY=YOUR_API_KEY

UPLOAD_FOLDER=uploads

REPORT_FOLDER=reports
```

---

# 🐳 Run Using Docker

Build the containers

```bash
docker compose build
```

Start the application

```bash
docker compose up
```

Run in detached mode

```bash
docker compose up -d
```

Stop containers

```bash
docker compose down
```

---

# 📚 API Documentation

After running the application:

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# 📌 REST API Endpoints

## Upload CSV

```
POST /jobs/upload
```

Uploads a transaction CSV file.

---

## Get All Jobs

```
GET /jobs
```

Returns all uploaded jobs.

---

## Check Job Status

```
GET /jobs/{job_id}/status
```

Returns processing status.

---

## View AI Summary

```
GET /jobs/{job_id}/results
```

Returns the generated financial summary.

---

## Download Report

```
GET /jobs/{job_id}/download
```

Downloads the generated report.

---

# 📂 Sample CSV

```csv
transaction_id,merchant,amount,currency,status,category
1,Amazon,2500,INR,Completed,Shopping
2,Zomato,450,INR,Pending,Food
3,Netflix,799,INR,Completed,Entertainment
4,Apple,100000,USD,Completed,Electronics
```

---

# 🧹 Data Cleaning Pipeline

The uploaded CSV undergoes multiple preprocessing steps:

- Validate required columns
- Remove duplicate transactions
- Normalize merchant names
- Normalize currency values
- Convert amounts to numeric values
- Handle missing categories
- Remove invalid records
- Standardize transaction status

---

# 🚨 Anomaly Detection

Transactions are analyzed using a statistical threshold.

Current logic:

- Calculate median transaction amount
- Flag transactions greater than **3 × median** as anomalies

Example:

| Merchant | Amount | Anomaly |
|----------|---------|----------|
| Amazon | 2500 | No |
| Apple | 100000 | Yes |

---

# 🤖 AI Analysis

Google Gemini generates:

- Spending overview
- High-value transactions
- Suspicious activity
- Expense distribution
- Financial recommendations

---

# 📄 Generated Reports

Each uploaded CSV generates:

- Cleaned transaction data
- Database records
- AI-generated financial summary
- Downloadable report

---

# 🔒 Error Handling

The application handles:

- Invalid CSV uploads
- Missing columns
- Invalid numeric values
- Database errors
- Gemini API failures
- Background task failures

---

# 📈 Future Improvements

- JWT Authentication
- Role-based access control
- Alembic database migrations
- Unit testing with Pytest
- Pagination & filtering
- PDF report generation
- Email notifications
- Kubernetes deployment
- CI/CD pipeline using GitHub Actions

---

# 📷 Screenshots

screenshots/
![Home API](images/Screenshot%202026-06-27%20221308.png)

![Swagger UI](images/Screenshot%202026-06-27%20221419.png)

![POST API](images/Screenshot%202026-06-27%20221520.png)
```

# 👨‍💻 Learning Outcomes

During this project, the following concepts were implemented:

- REST API Development
- FastAPI Framework
- Docker & Docker Compose
- PostgreSQL Integration
- SQLAlchemy ORM
- Redis
- Celery Background Processing
- AI Integration using Gemini
- CSV Processing
- Modular Backend Architecture

---

# 📜 License

This project is developed for educational and internship evaluation purposes.

---

# 👤 Author

**Akshat Bansal**

Backend Developer | Python | FastAPI | SQL | Docker | AI Integration

GitHub:
https://github.com/Akshat-1508/Backend-Devops-Assignment

LinkedIn:
https://www.linkedin.com/in/akshat-bansal-b11832322/

---

## ⭐ If you found this project useful, consider giving it a star on GitHub.