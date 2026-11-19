from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Ask Gemini something simple
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Hello! Tell me what you are in one sentence."
)

print(response.text)