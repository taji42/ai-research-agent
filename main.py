import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

# Get API key from .env file
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Make sure your .env file is set correctly.")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Send a test prompt
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Say hello like a pirate."
)

# Print response
print(response.text)

