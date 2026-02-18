import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

def create_research_plan(goal: str):
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
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/taji42/ai-research-agent", # Required by some free models
        "X-Title": "AI Research Agent"
    }
    
    data = {
        "model": "deepseek/deepseek-r1:free", # Using DeepSeek R1 (Very stable free model)
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status() 
        
        result = response.json()
        content = result['choices'][0]['message']['content']
        
        # Clean up thinking/markdown blocks
        clean_text = content.split('}') [0] + '}' # Keeps only the JSON part
        if "{" not in clean_text:
             clean_text = content.replace("```json", "").replace("```", "").strip()
             
        return json.loads(clean_text)
        
    except Exception as e:
        print(f"AI Logic: {e}. Using fallback queries.")
        return {
            "search_queries": [
                f"latest developments in {goal}",
                f"top 10 {goal} trends",
                f"expert guide on {goal}"
            ]
        }
