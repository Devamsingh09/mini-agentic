
````markdown
# Mini Agentic Pipeline


https://github.com/Devamsingh09/mini-agentic/blob/main/Gemini_Generated_Image_q5eb7zq5eb7zq5eb.png


A Python-based mini agentic system that:
- Retrieves relevant context from a small knowledge base (KB).
- Uses an LLM to reason and decide the next step.
- Executes actions via a tool (local CSV lookup or web search via Tavily API).
- Produces final answers with step-by-step logs and reasoning traces.

---

## Features

- **Retriever**: Uses FAISS vector store with HuggingFace embeddings for fast context retrieval from 8–20 KB documents.
- **Reasoner**: LLM-based reasoning with modular prompt templates (`v1`, `v2`).
- **Actor**: Executes actions using:
  - Local CSV tool (`prices.csv`) for numeric or pricing queries.
  - Web search tool via Tavily API for general queries.
- **Orchestrator**: Handles agentic behavior, decides when to use tools, logs each step, and returns detailed outputs.
- **Evaluation**: Test multiple queries, track latency, and assess answer quality.

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Devamsingh09/mini-agentic.git
cd mini-agentic
````

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your API key:

```text
TAVILY_API_KEY=your_tavily_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here  # if using Gemini
```

---

## Usage

### 1. Generate FAISS Index

Before running the bot, generate the FAISS index from your KB documents:

```bash
python src/retriever.py
```

This will create a FAISS index in the `faiss_index` folder for fast retrieval.

### 2. Run the Bot in Real-Time

Start the interactive chatbot:

```bash
python interactive.py
```

* Type your queries and get answers.
* Exit the chat by typing `exit` or `quit`.

### 3. Evaluate the System

Run automated evaluation on predefined test queries:

```bash
python src/evaluate.py
```

* Produces reports including:

  * Latency per query
  * Tool usage (CSV or web search)
  * Answer quality

---

## Project Structure

```
mini-agentic/
├── data/
│   ├── docs/           # KB documents (8–20 text files)
│   └── prices.csv      # CSV used as a tool
├── src/
│   ├── retriever.py    # Builds & loads FAISS index
│   ├── reasoner.py     # LLM reasoning
│   ├── actor_csv.py    # CSV lookup tool
│   ├── actor_web.py    # Tavily web search tool
│   ├── controller.py   # Orchestrates retrieval, reasoning, and tools
│   ├── evaluate.py     # Runs evaluation queries and metrics
│   └── utils.py        # Utility functions
├── prompts/
│   ├── reasoner_v1.txt
│   └── reasoner_v2.txt
├── requirements.txt
├── interactive.py      # Interactive chatbot CLI
└── README.md
```

---

## Notes

* Ensure `data/docs/` contains meaningful text documents for KB context.
* Make sure `data/prices.csv` exists and has the expected structure for CSV queries.
* `Tavily` API key is required for web search queries.
* The system decides automatically whether to use KB, CSV, or web search based on the question.




```



