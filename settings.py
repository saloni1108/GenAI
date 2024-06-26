import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API = os.getenv("GEMINI_API")
genai.configure(api_key=GEMINI_API)

model = genai.GenerativeModel('gemini-1.0-pro-latest')