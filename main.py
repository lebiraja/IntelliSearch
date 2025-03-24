import os
from dotenv import load_dotenv
from search_engine import get_search_results  # FIXED IMPORT
from nlp_processing import summarize_results
from ml_model import rank_results

# Load API keys from .env file
load_dotenv()
API_KEY = "AIzaSyD50sjuTCEKhe6FFM06_lf2SXecWBpCV8Q"
CX_KEY = "74c299e208bb94cbc"


def main():
    while True:
        query = input("\n🔍 Enter your search query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            print("👋 Exiting IntelliSearch. Goodbye!")
            break
        
        print("\n🔎 Searching, please wait...\n")
        results = get_search_results(query, API_KEY, CX_KEY)

        if not results:
            print("❌ No results found. Try a different query.")
            continue

        # Summarize and Rank Results
        summarized_results = summarize_results(results)
        ranked_results = rank_results(summarized_results)

        # Display Results
        print("\n📌 **Top Results:**")
        for i, (title, link, summary) in enumerate(ranked_results, 1):
            print(f"\n{i}. {title}\n   🔗 {link}\n   📖 Summary: {summary}\n")

if __name__ == "__main__":
    main()
