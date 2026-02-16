import os
import json
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

# Initialize Gemini Client with the new 2026 SDK
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def create_research_plan(goal: str):
    """
    Uses Gemini 2.5 Flash-Lite to create search queries.
    """
    prompt = f"""
    You are a Research Planner. Goal: "{goal}"
    Create 3 specific search queries to gather info for this goal.
    Return ONLY this JSON:
    {{
        "search_queries": ["query 1", "query 2", "query 3"]
    }}
    """
    
    try:
        # gemini-2.5-flash-lite is the current stable free-tier model
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        
        # Remove markdown code blocks if the AI includes them
        raw_text = response.text
        clean_text = raw_text.replace("```json", "").replace("```", "").strip()
        
        return json.loads(clean_text)
        
    except Exception as e:
        print(f"Planner Error: {e}")
        # Fallback queries if the API fails
        return {"search_queries": [f"research {goal}", "latest trends", "overview"]}

if __name__ == "__main__":
    # Test the planner alone
    print(create_research_plan("Test Goal"))
