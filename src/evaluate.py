from src.controller import orchestrate_query
import warnings 
warnings.filterwarnings('ignore')
def run_batch_evaluation():
    questions = [
        "What is the current repo rate?",
        "How does RBI regulate inflation?",
        "What is the cash reserve ratio?",
        "What is the current gold price?",
        "What is USD exchange rate?",
    ]
    results = []
    for q in questions:
        res = orchestrate_query(q, prompt_version="v2")
        results.append(res)
        print("\n--- QUERY ---")
        print("Question:", q)
        print("Answer:", res["final_answer"])
        print("Tool calls:", res["tool_calls"])
        print("Total latency:", res["total_latency"])
    return results

if __name__ == "__main__":
    run_batch_evaluation()
