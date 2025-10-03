from src.controller import orchestrate_query
import warnings
warnings.filterwarnings('ignore')
from dotenv import load_dotenv
load_dotenv()
while True:
    q = input("You: ")
    if q.lower() in ("exit", "quit"):
        break
    result = orchestrate_query(q)
    print("Bot:", result["final_answer"])
