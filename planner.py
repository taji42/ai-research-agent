import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

def create_research_plan(goal: str):
    """
    Calls Gemini via OpenRouter to bypass regional location blocks.
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    prompt = f"""
    You are a Research Planner. Goal: "{goal}"
    Create 3 specific search queries to gather info for this goal.
    Return ONLY this JSON structure:
    {{
        "search_queries": ["query 1", "query 2", "query 3"]
    }}
    """
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "google/gemini-2.0-flash-lite-preview-02-05:free",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status() # Check for errors
        
        result = response.json()
        content = result['choices'][0]['message']['content']
        
        # Clean up any potential markdown formatting from the AI
        clean_text = content.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_text)
        
    except Exception as e:
        print(f"Agent Logic: AI is busy or blocked. Using system defaults. ({e})")
        return {
            "search_queries": [
                f"latest developments in {goal}",
                f"business impact of {goal} 2026",
                f"implementation guide for {goal}"
            ]
        }
