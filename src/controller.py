# src/controller.py
from src.retriever import load_faiss_index
from src.reasoner import get_reasoner
from src.actor_csv import CSVTool
from src.actor_web import WebSearchTool
import time
from dotenv import load_dotenv

# Load environment variables including TAVILY_API_KEY
load_dotenv()

def orchestrate_query(question: str, prompt_version="v1", k=4, use_tool_auto=True):
    logs = []
    start_time = time.time()

    # 1. Retrieval from KB
    vect = load_faiss_index()
    retriever = vect.as_retriever(search_type="similarity", search_kwargs={"k": k})
    docs = retriever.get_relevant_documents(question)
    context_text = "\n---\n".join(
        [f"[{d.metadata.get('source','unknown')}] {d.page_content}" for d in docs]
    )
    logs.append({
        "step": "retrieval",
        "num_hits": len(docs),
        "sources": [d.metadata.get("source","unknown") for d in docs]
    })

    # 2. Initial reasoning
    reasoner = get_reasoner(prompt_version=prompt_version)
    reason_output = reasoner.run({"context": context_text, "question": question, "tool_output": ""})
    logs.append({"step": "reasoner_initial", "output": reason_output})

    # 3. Decide if tool is needed
    decision = None
    call_tool = False
    use_web = False
    if use_tool_auto:
        output_upper = reason_output.upper()
        if "USE_CSV" in output_upper:
            call_tool = True
            decision = "CSV"
        elif "USE_WEB" in output_upper:
            call_tool = True
            use_web = True
            decision = "WEB"
        else:
            call_tool = False
            decision = "KB"

    # 4. Execute tool if needed
    tool_out = ""
    tool_latency = None
    tool_calls = []

    if call_tool:
        t0 = time.time()
        try:
            if use_web:
                web_tool = WebSearchTool()
                result = web_tool.search(question)
                tool_out = str(result)
                tool_name = "WebSearchTool"
            else:
                csv_tool = CSVTool()
                result = csv_tool.query_price(question)
                tool_out = str(result)
                tool_name = "CSVTool"
        except Exception as e:
            result = f"Error executing tool: {e}"
            tool_out = result
            tool_name = "ToolError"

        tool_latency = time.time() - t0
        logs.append({
            "step": "tool_call",
            "tool": tool_name,
            "input": question,
            "output": result,
            "latency": tool_latency
        })
        tool_calls.append({"tool": tool_name, "latency": tool_latency})

    # 5. Final reasoning with tool output
    final_reasoner = get_reasoner(prompt_version=prompt_version)
    final_resp = final_reasoner.run({"context": context_text, "question": question, "tool_output": tool_out})
    logs.append({"step": "reasoner_final", "output": final_resp})

    total_time = time.time() - start_time
    return {
        "question": question,
        "final_answer": final_resp,
        "context_snippets": [d.metadata.get("source","unknown") for d in docs],
        "logs": logs,
        "tool_calls": tool_calls,
        "total_latency": total_time,
        "decision": decision
    }


if __name__ == "__main__":
    example = orchestrate_query("Who is Narendra Modi?", prompt_version="v2")
    print(example)
