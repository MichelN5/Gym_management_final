# Gym Management Frontend

React/Vite frontend for the Gym Management System. It connects to the Django backend for authentication, members, fee packages, payments, bills, notifications, and admin/member dashboard flows.

## Tech Stack

- React
- Vite
- React Router
- Redux Toolkit
- Apollo Client
- Axios
- DaisyUI / Tailwind-related styling

## Docker

Run from the project root:

```bash
docker compose up --build
```

The frontend runs at:

```text
http://127.0.0.1:5173/
```

## Local Setup

Install dependencies:

```bash
npm install
```

Create an environment file:

```bash
cp .env.example .env
```

Run the dev server:

```bash
npm run dev
```

Build for production:

```bash
npm run build
```

Preview the production build:

```bash
npm run preview
```

## Environment Variables

| Variable | Purpose |
|---|---|
| `VITE_API_URL` | Django REST API base URL |
| `VITE_GRAPHQL_URL` | Django GraphQL endpoint |

Example:

```text
VITE_API_URL=http://127.0.0.1:8000
VITE_GRAPHQL_URL=http://127.0.0.1:8000/graphql/
```

## Project Structure

```text
gym-management-main/
  public/
  src/
    apollo/
    app/
    components/
    context/
    css/
    hooks/
    pages/
    services/
    slices/
  Dockerfile
  package.json
```
