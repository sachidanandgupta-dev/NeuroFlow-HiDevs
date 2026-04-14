import httpx
import asyncio
import json

class NeuroFlowClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {api_key}"}

    async def query(self, query: str, pipeline_id: str, stream: bool = False):
        async with httpx.AsyncClient(timeout=60.0) as client:
            if not stream:
                resp = await client.post(f"{self.base_url}/query", 
                                       json={"query": query, "pipeline_id": pipeline_id}, 
                                       headers=self.headers)
                return resp.json()
            
            # SSE Streaming Implementation
            async with client.stream("GET", f"{self.base_url}/query/stream", headers=self.headers) as response:
                async for line in response.aiter_lines():
                    if line.startswith("data: "):
                        yield json.loads(line[6:])

    async def ingest_file(self, file_path: str):
        # Implementation for polling for completion
        async with httpx.AsyncClient() as client:
            with open(file_path, "rb") as f:
                resp = await client.post(f"{self.base_url}/ingest", files={"file": f}, headers=self.headers)
                job_id = resp.json()["job_id"]
            
            # Poll for status
            while True:
                status_resp = await client.get(f"{self.base_url}/ingest/{job_id}", headers=self.headers)
                if status_resp.json()["status"] == "complete":
                    break
                await asyncio.sleep(2)
            return True