
```markdown
# Mini Agentic Pipeline

A lightweight AI-driven agentic pipeline that retrieves knowledge from a small knowledge base, reasons using a large language model (LLM), executes actions via tools (CSV lookup or web search), and provides step-by-step traceable answers.

---

## Table of Contents
- [Objective](#objective)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Evaluation](#evaluation)
- [Demo](#demo)
- [Design Decisions](#design-decisions)
- [Limitations](#limitations)
- [License](#license)

---

## Objective
The pipeline:
1. Retrieves relevant context from a small knowledge base (KB).
2. Uses an LLM to reason and decide the next step.
3. Executes an action via a tool (CSV lookup or web search via Tavily API).
4. Produces a final answer with a clear step-by-step trace/log.

---

## Features
- **Retriever**: FAISS-based retrieval of 8–20 text documents.
- **Reasoner**: LLM-driven reasoning (supports multiple prompt versions: v1, v2).
- **Actor Tools**:
  - Local CSV lookup (`prices.csv`)
  - Web search via [Tavily API](https://tavily.com/)
- **Agentic Behavior**: System decides automatically whether to use KB or tools.
- **Logging**: Step-by-step trace of retrieval, reasoning, and tool usage.

---

## Project Structure
```

mini-agentic/
├── data/
│   ├── docs/                # 8–20 KB text documents
│   └── prices.csv           # Local CSV used as tool
├── src/
│   ├── retriever.py
│   ├── reasoner.py
│   ├── actor_csv.py
│   ├── actor_web.py
│   ├── controller.py
│   ├── evaluate.py
│   └── utils.py
├── prompts/
│   ├── reasoner_v1.txt
│   └── reasoner_v2.txt
├── requirements.txt
├── generate.py              # Generates sample docs & CSV
├── interactive.py           # Run interactive chatbot
└── README.md

````

---

## Setup Instructions
1. Clone the repository:
```bash
git clone https://github.com/Devamsingh09/mini-agentic.git
cd mini-agentic
````

2. Create a Python virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and set your API keys:

```env
TAVILY_API_KEY=your_tavily_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

5. Generate sample documents and CSV (optional):

```bash
python generate.py
```

6. Build the FAISS index:

```bash
python src/retriever.py
```

---

## Usage

### Interactive Chat

```bash
python interactive.py
```

* Type your query and get a step-by-step response.
* Exit by typing `exit` or `quit`.

### Example Query

```
You: Who is Narendra Modi?
Bot: <Answer from KB or Web Search>
```

### Programmatic Usage

```python
from src.controller import orchestrate_query

result = orchestrate_query("What is the maximum price in prices.csv?", prompt_version="v2")
print(result["final_answer"])
```

---

## Evaluation

* Run automated tests on 8–12 queries:

```bash
python src/evaluate.py
```

* Reports:

  * Latency per query
  * Tool usage
  * Answer quality

---

## Demo

Record a 5–8 minute video showing:

* Architecture explanation
* Code walkthrough
* Demo on 3–4 queries
* Learnings and limitations

---

## Design Decisions

* **FAISS** for fast KB retrieval
* **HuggingFace embeddings** for semantic search
* **Tavily API** for reliable web search
* **CSV tool** as a local structured data source
* Modular prompt system with versions

---

## Limitations

* Limited KB (8–20 documents)
* Web search depends on Tavily API availability
* LLM reasoning may not be perfect for all queries
* CSV tool only works with structured queries about prices

---
