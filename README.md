# Inventory & Order Management System

Full-stack application built with FastAPI, PostgreSQL, SQLAlchemy, Alembic, and React.

## Quick start with Docker

1. Copy `.env.example` to `.env`.
2. Replace `POSTGRES_PASSWORD` and `SECRET_KEY` with strong, unique random secrets.
3. Run `docker compose config`, then `docker compose up --build -d`.
4. Open the frontend at <http://localhost:8080>, API docs at <http://localhost:8000/docs>, and health check at <http://localhost:8000/health>.

See [`DEPLOYMENT.md`](DEPLOYMENT.md) for local development, configuration, troubleshooting, and production considerations.

## Current scope and limitations

The repository contains authentication, product/category management, basic inventory and order flows, payment/review/notification/dashboard modules, a React UI, an Alembic migration history, and a Postman collection. The assignment's full multi-warehouse stock ledger, complete fulfillment/returns workflows, idempotency guarantees, warehouse-scoped authorization, immutable audit history, and required test coverage still need to be completed and verified. See [`REQUIREMENTS_GAP.md`](REQUIREMENTS_GAP.md) for the acceptance checklist.

**Do not treat a successful startup as proof of production readiness.** Test against PostgreSQL, verify migrations from an empty database, and pass the required business-rule and concurrency tests before production use.

## Project layout

- `backend/` — FastAPI API, SQLAlchemy models, services/repositories, Alembic migrations
- `frontend/` — React/Vite application
- `postman/` — API collection
- `docker-compose.yml` — local multi-service deployment
- `DEPLOYMENT.md` — setup and operations guide
- `REQUIREMENTS_GAP.md` — assignment acceptance checklist

## Security

Never commit `.env`, credentials, tokens, or production data. `.env.example` contains placeholders only. Rotate any credential that was previously placed in a shared archive. Use TLS, managed secrets, database backups, monitoring, and a security review for a production deployment.
