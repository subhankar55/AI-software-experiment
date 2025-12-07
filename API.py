import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="can you perform the task?"
)
print(response.text)