# Deployment Guide: NeuroFlow AI Platform

## Deployment Target: Railway
1. Install CLI: `npm install -g @railway/cli`
2. Login: `railway login`
3. Initialize: `railway init`
4. Deploy Services:
   - Database (Postgres with pgvector)
   - Redis
   - Backend API (using `backend/Dockerfile`)
   - Worker

## Production Verification Checklist
- [ ] `GET /health` returns all green.
- [ ] Uploading a PDF via `/ingest` reaches `complete` status.
- [ ] Query returns cited answer.
- [ ] Evaluation entry appears in `/evaluations`.
- [ ] `GET /metrics` shows Prometheus data.

## Rollback Procedure
1. **Redeploy:** Go to Railway Dashboard -> Service -> Deployments -> Select previous successful build -> "Redeploy".
2. **Database:** If a migration failed, run `alembic downgrade -1` (if applicable).
3. **Verify:** Check `/health` endpoint to ensure the system is back online.