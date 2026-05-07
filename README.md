# Data Subject Rights Portal — AI Service

## Project Overview

The Data Subject Rights Portal is an AI-powered web application developed as a capstone internship project.

This module focuses on the AI Service built using Flask and integrated with the Groq API for intelligent response generation.

The AI service provides:

- AI-generated responses
- Secure prompt validation
- Injection attack prevention
- API rate limiting
- AI quality testing
- Docker container support

---

# Project Architecture

Frontend (React)  
⬇  
Backend (Spring Boot)  
⬇  
AI Service (Flask + Groq API)

---

# Technology Stack

| Component            | Technology               |
| -------------------- | ------------------------ |
| Backend AI Service   | Flask                    |
| AI Model API         | Groq API (LLaMA 3.3 70B) |
| Programming Language | Python 3.10              |
| Security Testing     | OWASP ZAP                |
| Unit Testing         | Pytest                   |
| Rate Limiting        | Flask-Limiter            |
| Containerization     | Docker                   |
| Version Control      | Git + GitHub             |

---

# Folder Structure

```plaintext
ai-service/
│
├── prompts/
├── routes/
├── services/
├── tests/
├── app.py
├── requirements.txt
├── Dockerfile
└── .env





AI Features
AI prompt processing
Secure response generation
Prompt injection prevention
SQL injection filtering
HTML sanitization
API abuse protection
Security validation
Automated testing
API Endpoints
1. Health Endpoint
Route

GET /health

Purpose

Checks whether the AI service is running correctly.

Example Response
{
  "status": "AI service running"
}
2. Generate Endpoint
Route

POST /generate

Example Request
{
  "prompt": "Explain REST API simply"
}
Example Response
{
  "response": "REST API allows applications to communicate over HTTP."
}
3. Root Endpoint
Route

GET /

Purpose

Basic service availability verification.

Security Features

The AI service includes multiple security protections:

SQL Injection Protection
Prompt Injection Filtering
HTML Sanitization
Flask Rate Limiting
Security Headers
OWASP ZAP Security Testing
Pytest Security Validation
Security Testing
Manual Testing

Performed:

Empty input testing
SQL injection testing
Prompt injection testing
HTML injection testing

Unsafe requests correctly return:

HTTP 400 Bad Request
OWASP ZAP Testing

Completed:

Automated vulnerability scan
Security header verification
Critical vulnerability review

Result:

No critical vulnerabilities found
Pytest Testing

Implemented:

8 automated unit tests
Endpoint validation
Injection rejection tests
Error handling tests

Result:

All tests passed successfully
AI Quality Review

AI response quality was evaluated using:

10 fresh prompts
Accuracy scoring
Prompt tuning

Final Average Score:

4.5 / 5
Running the Project Locally
Step 1 — Install Dependencies
pip install -r requirements.txt
Step 2 — Configure Environment Variables

Create:

.env

Add:

GROQ_API_KEY=your_api_key_here
Step 3 — Run Flask Server
python app.py

Server runs on:

http://127.0.0.1:5000
Running Tests
Pytest
pytest

Expected Result:

8 passed
Docker Support
Build and Run
docker compose up --build
Demo Features

The demo includes:

Health endpoint verification
AI prompt generation
SQL injection rejection
Prompt injection rejection
Rate limiting demonstration
Security testing explanation
GitHub Repository

Repository Link:

https://github.com/KIRANHR04/data-subject-rights-portal
Developer Contribution
Kiran — AI Developer 2

Responsibilities:

Groq API Integration
Flask AI Security
Prompt Injection Prevention
OWASP ZAP Testing
Pytest Unit Testing
AI Quality Review
Docker AI Testing
Security Documentation
AI Demo Preparation
Final Status

AI Service implementation completed successfully with:

security validation
automated testing
AI quality verification
demo preparation
GitHub documentation
```
