# Gym Management System

A full-stack gym management application for managing members, fee packages, bills, payments, notifications, users, and workout-related dashboard flows.

## Features

- Admin and member authentication
- Admin dashboard
- Member dashboard
- Member management
- Fee package management
- Billing and payment tracking
- Notifications
- Google OAuth callback support
- REST API with JWT authentication
- GraphQL endpoint for notifications
- Dockerized local development setup

## Tech Stack

Frontend:

- React
- Vite
- React Router
- Redux Toolkit
- Apollo Client
- Axios
- DaisyUI / Tailwind-related styling

Backend:

- Python 3.12
- Django 5.1
- Django REST Framework
- Simple JWT
- django-allauth
- Graphene Django
- SQLite for local development

## Project Structure

```text
Gym_management_final/
  docker-compose.yml
  django_gym_management/   # Django backend
  gym-management-main/     # React/Vite frontend
```

## Run With Docker

Requirements:

- Docker Desktop
- Docker Compose

From the project root:

```bash
docker compose up --build
```

Open the app:

```text
http://127.0.0.1:5173/
```

Backend:

```text
http://127.0.0.1:8000/
```

Django admin:

```text
http://127.0.0.1:8000/admin/
```

Seeded development admin:

```text
username: admin
password: admin12345
```

## Local Development

Backend:

```bash
cd django_gym_management
python -m venv .venv
```

On Windows:

```powershell
.\.venv\Scripts\activate
```

Install and run:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_admin
python manage.py runserver 127.0.0.1:8000
```

Frontend:

```bash
cd gym-management-main
npm install
npm run dev
```

Open:

```text
http://localhost:5173/
```

## Environment Files

Backend example:

```text
django_gym_management/.env.example
```

Frontend example:

```text
gym-management-main/.env.example
```

Do not commit real `.env` files.

## Repository Hygiene

The repository ignores generated/local files such as:

- `.venv/`
- `node_modules/`
- `dist/`
- `db.sqlite3`
- `__pycache__/`
- logs
- real `.env` files
