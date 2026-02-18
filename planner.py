import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

def create_research_plan(goal: str):
    api_key = os.getenv("OPENROUTER_API_KEY")
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    prompt = f"""
    Return ONLY a JSON object for the goal: "{goal}".
    Format: {{"search_queries": ["q1", "q2", "q3"]}}
    """
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/taji42/ai-research-agent", 
    }
    
    data = {
        "model": "google/gemini-2.0-flash-lite-preview-02-05:free",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status() 
        content = response.json()['choices'][0]['message']['content']
        
        # Strip potential markdown formatting
        clean_json = content.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_json)
        
    except Exception as e:
        print(f"Agent Logic: AI is busy. Using fallback. ({e})")
        return {"search_queries": [f"research {goal}", "latest trends", "overview"]}
