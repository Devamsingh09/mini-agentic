# src/reasoner.py
import os
from pathlib import Path
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Set GEMINI_API_KEY in your .env")

PROMPT_FILES = {
    "v1": Path(__file__).parent.parent / "prompts" / "reasoner_v1.txt",
    "v2": Path(__file__).parent.parent / "prompts" / "reasoner_v2.txt"
}

def get_reasoner(prompt_version="v1"):
    prompt_file = PROMPT_FILES.get(prompt_version)
    if not prompt_file.exists():
        raise FileNotFoundError(f"Prompt file {prompt_file} not found")
    prompt_text = prompt_file.read_text(encoding="utf-8")
    prompt = PromptTemplate(input_variables=["context", "question", "tool_output"], template=prompt_text)

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.0,
        api_key=GEMINI_API_KEY
    )

    return LLMChain(llm=llm, prompt=prompt)
