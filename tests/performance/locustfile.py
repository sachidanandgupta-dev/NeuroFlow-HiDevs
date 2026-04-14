import random
from locust import HttpUser, task, between

SAMPLE_QUERIES = ["What is NeuroFlow?", "How does RAG work?", "Show me recent evaluations."]
TEST_DOCS = ["tests/fixtures/test_doc.pdf"]

class QueryUser(HttpUser):
    weight = 7
    @task
    def query_pipeline(self):
        self.client.post("/query", json={"query": random.choice(SAMPLE_QUERIES)})

class IngestUser(HttpUser):
    weight = 2
    @task
    def ingest_document(self):
        with open(random.choice(TEST_DOCS), "rb") as f:
            self.client.post("/ingest", files={"file": f})

class AdminUser(HttpUser):
    weight = 1
    @task
    def check_evaluations(self):
        self.client.get("/evaluations")