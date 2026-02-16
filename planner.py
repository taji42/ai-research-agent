import os
import json
from dotenv import load_dotenv
from google import genai

# 1. Load the environment variables from .env
load_dotenv()

# 2. Initialize the Gemini Client with your key
# The client automatically looks for the key in your .env
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def create_research_plan(goal: str):
    """
    Takes a research goal and asks Gemini 2.0 to create 
    a list of search queries.
    """
    
    prompt = f"""
    You are a Research Planner Agent. 
    Your goal is: "{goal}"
    
    Create exactly 3 specific search queries that will help gather 
    the most important information for this goal.
    
    Return the result in ONLY this JSON format:
    {{
        "search_queries": ["query 1", "query 2", "query 3"]
    }}
    """
    
    try:
        # 3. Call the modern Gemini 2.0 Flash model
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        
        # 4. Clean up the response text
        # Sometimes AI adds ```json ... ``` tags which we must remove
        raw_text = response.text
        clean_text = raw_text.replace("```json", "").replace("```", "").strip()
        
        # 5. Convert string to a real Python dictionary
        plan = json.loads(clean_text)
        return plan

    except Exception as e:
        print(f"Error in Planner: {e}")
        # Return a fallback plan so the project doesn't crash
        return {"search_queries": [f"basic info on {goal}", "latest news", "key details"]}

if __name__ == "__main__":
    # Test it directly
    test_goal = "Build a PC in 2026"
    print(create_research_plan(test_goal))
