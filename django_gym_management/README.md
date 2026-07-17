# Gym Management Backend

Django REST API for the Gym Management System. It provides authentication, member management, fee packages, billing, payments, notifications, and GraphQL support.

## Tech Stack

- Python 3.12
- Django 5.1
- Django REST Framework
- Simple JWT
- django-allauth
- Graphene Django
- SQLite for local development

## Docker

Run from the project root:

```bash
docker compose up --build
```

The backend runs at:

```text
http://127.0.0.1:8000/
```

Docker startup runs:

```text
migrate -> seed_admin -> runserver
```

Development admin:

```text
username: admin
password: admin12345
```

## Local Setup

```bash
python -m venv .venv
```

On Windows:

```powershell
.\.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Prepare the database:

```bash
python manage.py migrate
python manage.py seed_admin
```

Run the server:

```bash
python manage.py runserver 127.0.0.1:8000
```

## Main Routes

| Route | Purpose |
|---|---|
| `/admin/` | Django admin |
| `/api/token/` | JWT login |
| `/api/token/refresh/` | Refresh JWT |
| `/api/user/register/` | Register user |
| `/api/auth/user/` | Current user |
| `/api/members/` | Member routes |
| `/api/notifications/` | Notification routes |
| `/api/` | Payment and fee package routes |
| `/graphql/` | GraphQL endpoint |

## Environment Variables

See `.env.example`.
