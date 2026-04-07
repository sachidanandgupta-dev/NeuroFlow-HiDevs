# API Contracts

- **POST /ingest**: File/URL ingestion.
- **POST /query**: RAG query execution.
- **GET /query/{id}/stream**: SSE stream for generation.
- **GET /evaluations**: Paginated evaluation results.
- **GET /evaluations/aggregate**: Rolling quality metrics.
- **POST /finetune/jobs**: Submit a new training job.