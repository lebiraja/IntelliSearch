import streamlit as st
from dotenv import load_dotenv
from search_engine import get_search_results
from nlp_processing import summarize_results
from ml_model import rank_results
import os

# Load API keys from .env file
load_dotenv()

API_KEY = "AIzaSyD50sjuTCEKhe6FFM06_lf2SXecWBpCV8Q"
CX_KEY = "74c299e208bb94cbc"
# Streamlit UI
st.title("🔍 IntelliSearch AI")
st.write("A smart search assistant powered by AI.")

# User input
query = st.text_input("Enter your search query:")

if st.button("Search") and query:
    st.write("🔎 Searching, please wait...")
    
    results = get_search_results(query, API_KEY, CX_KEY)
    
    if not results:
        st.error("❌ No results found. Try a different query.")
    else:
        summarized_results = summarize_results(results)
        ranked_results = rank_results(summarized_results)
        
        st.subheader("📌 Top Results:")
        for i, (title, link, summary) in enumerate(ranked_results, 1):
            st.markdown(f"### {i}. [{title}]({link})")
            st.write(f"📖 {summary}")
