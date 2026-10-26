# Deployment and verification guide

> **Important:** this package includes a Docker Compose deployment scaffold and source-level hardening. It is not certified as a complete implementation of every requirement in the assignment. The existing application still needs the outstanding business workflows and automated integration/concurrency tests listed in `REQUIREMENTS_GAP.md`. Do not expose it to real customers or production data until those checks pass.

## Local Docker deployment

Prerequisites: Docker Engine/Desktop with the Compose plugin.

1. Copy the root environment template:

   ```bash
   cp .env.example .env
   ```

   On Windows PowerShell use `Copy-Item .env.example .env`.

2. Replace `POSTGRES_PASSWORD` and `SECRET_KEY` with unique random values. Use a secret manager for real production deployments. Never commit `.env`.
3. Check configuration and build:

   ```bash
   docker compose config
   docker compose build
   ```

4. Start services:

   ```bash
   docker compose up -d
   docker compose ps
   docker compose logs -f backend
   ```

   The backend container runs `alembic upgrade head` before starting Uvicorn. If migrations fail, the backend will not become healthy; inspect logs and fix the migration/database issue rather than bypassing migrations.

5. Verify:
   - Frontend: http://localhost:8080
   - API health: http://localhost:8000/health
   - Swagger: http://localhost:8000/docs
   - OpenAPI: http://localhost:8000/openapi.json

6. Stop services with `docker compose down`. Persistent database data remains in the `postgres_data` volume. To irreversibly delete local database data as well, `docker compose down -v`.

## Configuration

- `DATABASE_URL`: provided to the backend by Compose and points to the Compose PostgreSQL service.
- `SECRET_KEY`: must be a long, random, private value.
- `CORS_ORIGINS`: comma-separated browser origins allowed to call the API.
- `VITE_API_BASE_URL`: API base URL compiled into the frontend at build time. Set it to the externally reachable API URL when deploying to a different host/domain, then rebuild the frontend.
- `BACKEND_PORT` and `FRONTEND_PORT`: host ports.

For HTTPS, use a managed reverse proxy/load balancer and TLS certificates. Restrict database network access, enable backups and restore tests, configure monitoring/log retention, and use platform-managed secrets before production use. Do not use the sample credentials.

## Manual development mode

Backend (from `backend/`): create/activate a Python 3.12 virtual environment, install `requirements.txt`, copy `.env.example` to `.env`, set a reachable PostgreSQL `DATABASE_URL` and strong `SECRET_KEY`, then run `alembic upgrade head` and `uvicorn app.main:app --reload`.

Frontend (from `frontend/`): `npm ci`, configure `VITE_API_BASE_URL` in a local `.env`, then `npm run dev`.

## Verification commands

```bash
# Source syntax check
python -m compileall -q backend/app backend/alembic

# Backend tests (requires backend dependencies and a valid test configuration)
cd backend
pytest -q

# Frontend production build (requires Node.js and npm)
cd ../frontend
npm ci
npm run build
npm run lint
```

A successful image build or health endpoint only proves the process starts; it does not prove all business rules, authorization boundaries, transaction rollback behavior, or concurrency guarantees. Run the acceptance criteria in `REQUIREMENTS_GAP.md` before calling the project production-ready.
