import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

async def get_ai_response(prompt: str) -> str:
    response = await model.generate_content_async(prompt)
    return response.text
