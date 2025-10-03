# src/actor_web.py
import os
from dotenv import load_dotenv
from tavily import TavilyClient  # correct Tavily SDK import

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
if not TAVILY_API_KEY:
    raise ValueError("Set TAVILY_API_KEY in your .env")

class WebSearchTool:
    """
    Wrapper for Tavily API to perform web searches.
    Returns top N snippets for a given query.
    """
    def __init__(self):
        self.client = TavilyClient(api_key=TAVILY_API_KEY)

    def search(self, query: str, num_results: int = 3) -> str:
        try:
            # Perform search
            response = self.client.search(query)
            
            # Tavily usually returns a dict with a 'results' list
            results_list = response.get("results", []) if isinstance(response, dict) else response
            
            # Collect snippets
            snippets = []
            for r in results_list[:num_results]:
                snippet = r.get("snippet") or r.get("description") or r.get("title")
                if snippet:
                    snippets.append(snippet)
            
            if not snippets:
                return "No results found."
            
            return "\n".join(snippets)
        except Exception as e:
            return f"Error during web search: {e}"
