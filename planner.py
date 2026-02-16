import os
import json
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Initialize Gemini Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def create_research_plan(goal: str):
    """
    Asks Gemini to create 3 search queries for a goal.
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
        # Using 1.5-flash-8b to avoid the 'limit: 0' quota error
        response = client.models.generate_content(
            model="gemini-1.5-flash-8b",
            contents=prompt
        )
        
        # Clean markdown tags if present
        raw_text = response.text
        clean_text = raw_text.replace("```json", "").replace("```", "").strip()
        
        return json.loads(clean_text)
    except Exception as e:
        print(f"Planner Error: {e}")
        return {"search_queries": [f"research {goal}", "latest trends", "overview"]}

if __name__ == "__main__":
    print(create_research_plan("Test Goal"))
