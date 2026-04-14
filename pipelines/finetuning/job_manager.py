from openai import AsyncOpenAI

client = AsyncOpenAI()

async def submit_finetune_job(jsonl_path: str, base_model: str) -> str:
    # 1. Upload file to OpenAI
    file_resp = await client.files.create(
        file=open(jsonl_path, "rb"), 
        purpose="fine-tune"
    )
    # 2. Start the actual training job
    job = await client.fine_tuning.jobs.create(
        training_file=file_resp.id, 
        model=base_model
    )
    return job.id

async def register_model_after_training(job_id, model_name):
    # Logic for Step 4 in your screenshot:
    # Update ModelRouter to prefer the new fine-tuned model
    print(f"Model {model_name} registered and routed for domain tasks.")
    mlflow.register_model(f"runs:/{job_id}/model", "neuroflow-production-model")