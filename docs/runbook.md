# NeuroFlow Architecture Runbook

## Incident 1: High Query Latency (P95 > 10s)
- **Check:** Jaeger traces to see which span (retrieval vs generation) is slow.
- **Remediation:** Flush Redis cache, scale API replicas, or check Postgres `pg_stat_statements`.

## Incident 2: Evaluation Scores Degrading
- **Check:** Recent ingested documents (low-quality input) or MLflow for recent fine-tuning changes.
- **Remediation:** Revert to the last stable model version.

## Incident 3: LLM Provider Circuit Breaker Open
- **Check:** `GET /health` for status. Check provider status page (e.g., status.openai.com).
- **Remediation:** Wait for recovery timeout or manually reset via `POST /admin/circuit-breaker/reset`.

## Incident 4: Ingestion Queue Depth > 100
- **Check:** Worker logs for errors or stuck jobs in Redis.
- **Remediation:** Restart worker containers; scale workers if traffic is legitimate.

## Incident 5: Database Disk Usage > 80%
- **Check:** Which table is growing fastest (likely `pipeline_runs`).
- **Remediation:** Run the manual data retention job: `python -m backend.jobs.retention`.