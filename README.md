```markdown
# School Management System (Django Backend)

## Overview

A backend application built with Django and Django REST Framework to manage students, teachers, and courses. It supports CRUD operations, JWT-based authentication, background task scheduling with Celery, and caching with Redis.

## Features

- Manage students, teachers, and courses
- JWT authentication for secure API access
- Automated tasks with Celery
- Redis caching for faster data retrieval

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Aditi-bairagi61/School-Management-System.git
   cd School-Management-System
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure PostgreSQL and Redis, then run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Start Celery:
   ```bash
   celery -A school_mgmt_backend worker --loglevel=info
   ```

## API Endpoints

| Endpoint               | Method | Description           |
|------------------------|--------|-----------------------|
| `/api/students/`       | GET    | List students         |
| `/api/students/`       | POST   | Add a new student     |
| `/api/teachers/`       | GET    | List teachers         |
| `/api/courses/`        | GET    | List courses          |

