import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = "AIzaSyBXaA3L_gcfJLi_WFIoZpQZ8qHLoLlqF_Y"

# Configure Gemini AI
genai.configure(api_key=API_KEY)

def generate_ai_summary(query, search_results):
    """
    Uses Gemini AI to summarize search results and enhance the response.
    """
    model = genai.GenerativeModel("gemini-pro")
    context = f"Provide a concise, informative summary of the topic: {query}. Based on the following search results:\n"
    
    for i, (title, link, summary) in enumerate(search_results, 1):
        context += f"{i}. {title} - {summary}\n"

    response = model.generate_content(context)
    return response.text if response else "AI could not generate a summary."
