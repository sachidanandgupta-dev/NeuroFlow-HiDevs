import asyncio
from evaluation.metrics.faithfulness import evaluate_faithfulness
from evaluation.metrics.answer_relevance import evaluate_answer_relevance
from evaluation.metrics.context_precision import evaluate_context_precision
from evaluation.metrics.context_recall import evaluate_context_recall

class EvaluationJudge:
    async def evaluate_run(self, query, answer, context, chunks, run_id):
        # 1. Run all in parallel
        f, ar, cp, cr = await asyncio.gather(
            evaluate_faithfulness(query, answer, context),
            evaluate_answer_relevance(query, answer),
            evaluate_context_precision(query, chunks, answer),
            evaluate_context_recall(query, chunks, answer)
        )
        
        # 2. Compute weighted overall score
        overall_score = (0.35 * f) + (0.30 * ar) + (0.20 * cp) + (0.15 * cr)
        
        # 3. Log to DB (Simulated)
        print(f"Logged run {run_id} with score {overall_score}")
        
        # 4. Training pair extraction
        if overall_score > 0.8:
            print("Candidate for fine-tuning added to training_pairs")
            
        return {"overall": overall_score, "metrics": {"f": f, "ar": ar, "cp": cp, "cr": cr}}