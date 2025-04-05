import streamlit as st
from dotenv import load_dotenv
import os
import requests
import ollama
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Tuple
import re

# Load environment variables
load_dotenv()

# Configuration
API_KEY = os.getenv("GOOGLE_API_KEY") 
CX_KEY = os.getenv("CX_SEARCH_ENGINE_ID") 
LLM_MODEL = "deepseek-r1:1.5b"

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def get_search_results(query: str, num_results: int = 5) -> List[Tuple[str, str, str]]:
    """Fetch web search results from Google Custom Search API"""
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX_KEY}&num={num_results}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return [(item["title"], item["link"], item.get("snippet", "")) for item in data.get("items", [])]
    except Exception as e:
        st.error(f"Search error: {str(e)}")
        return []

def clean_llm_output(response: str) -> str:
    """Remove <think> tags and their content"""
    return re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()

def generate_with_llm(prompt: str) -> str:
    """Generate response using Ollama's DeepSeek R1"""
    try:
        response = ollama.generate(
            model=LLM_MODEL,
            prompt=prompt,
            options={'temperature': 0.3}
        )
        return clean_llm_output(response['response'])
    except Exception as e:
        st.error(f"LLM error: {str(e)}")
        return "Error generating response."

def rank_results(results: List[Tuple[str, str, str]], query: str) -> List[Tuple[str, str, str]]:
    """Rank results using TF-IDF similarity"""
    if not results:
        return results

    corpus = [query] + [snippet for _, _, snippet in results]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarities = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1:])

    ranked_results = sorted(zip(similarities[0], results), reverse=True, key=lambda x: x[0])
    return [item[1] for item in ranked_results]

def summarize_with_llm(results: List[Tuple[str, str, str]], query: str) -> str:
    """Generate a summary of search results using LLM"""
    context = "\n\n".join([f"{title}: {snippet}" for title, _, snippet in results])
    prompt = f"""
    Summarize these search results about '{query}' in 3-4 paragraphs clearly without internal thoughts or explanations.
    {context}
    Provide key insights, highlight contradictions, and mention references.
    """
    return generate_with_llm(prompt)

def process_search(query: str):
    """Main pipeline: Search -> Rank -> Summarize -> Provide references"""
    results = get_search_results(query)
    ranked_results = rank_results(results, query)
    summary = summarize_with_llm(ranked_results, query)

    # Add to history before displaying
    st.session_state.chat_history.append(("ai", summary))

    # Display summary
    st.markdown("### 🔍 Search Summary")
    

    # Display references
    st.markdown("### 🔗 References")
    for title, link, _ in ranked_results:
        st.markdown(f"- [{title}]({link})")

# --- Streamlit UI ---
st.title("🔍 IntelliSearch AI")
st.write("AI-powered search assistant combining DeepSeek R1 & Google Search API")

query = st.chat_input("Ask me anything...")
if query:
    with st.spinner("Processing..."):
        process_search(query)

# Display chat history (last 4 entries)
for role, message in st.session_state.chat_history[-4:]:
    with st.chat_message(role):
        st.markdown(message)
