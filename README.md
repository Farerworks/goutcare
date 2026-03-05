cat > ~/farerworks-studio/startups/goutcare/README.md << 'EOF'
# GoutCare

GoutCare is an MVP skeleton (Next.js + FastAPI + Postgres) running via Docker Compose.

## What is running
- Frontend (Next.js): http://localhost:3001
- Backend (FastAPI): http://localhost:8000
- DB (Postgres): localhost:5432 (compose service name: db)

## Quick Start (Local)
cd ~/farerworks-studio/startups/goutcare
docker compose up -d --build
docker compose ps

## Health Checks

Backend:
curl -i http://localhost:8000/api/v1/health

Expected result:
HTTP/1.1 200 OK
{"status":"ok"}

Frontend:
Open browser:
http://localhost:3001

If the page shows "API health: ok", it’s connected.

## Stop / Reset

Stop containers:
docker compose down

Stop and remove database volume:
docker compose down -v

## Logs

Backend logs:
docker compose logs -f backend

Frontend logs:
docker compose logs -f frontend

Database logs:
docker compose logs -f db

## Notes
backend/app/generated/ and frontend/app/generated/ are auto-generated files.
Do not edit them manually unless you know why.
EOF