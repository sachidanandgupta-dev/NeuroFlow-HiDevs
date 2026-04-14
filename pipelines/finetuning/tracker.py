import mlflow

def start_training_job(job_id, pairs, base_model):
    with mlflow.start_run(run_name=f"finetune-{job_id}") as run:
        mlflow.log_params({
            "base_model": base_model,
            "training_pair_count": len(pairs),
            "avg_quality_score": sum(p.get('score', 0) for p in pairs) / len(pairs) if pairs else 0
        })
        # Log training data as an artifact
        mlflow.log_artifact(f"training_data/{job_id}.jsonl")
        return run.info.run_id

def log_job_results(run_id, job_result):
    with mlflow.start_run(run_id=run_id):
        mlflow.log_metrics({
            "training_loss": job_result.training_loss,
            "validation_loss": job_result.validation_loss,
            "training_token_count": job_result.trained_tokens
        })