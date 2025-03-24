import os
from search_engine import get_search_results
from nlp_processing import summarize_results
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
API_KEY = "AIzaSyD50sjuTCEKhe6FFM06_lf2SXecWBpCV8Q"
CX_KEY = "74c299e208bb94cbc"


def main():
    while True:
        query = input("\n🔍 Enter search query (or type 'exit' to quit'): ")
        if query.lower() == "exit":
            break

        print("\n🔎 Searching, please wait...\n")

        # ✅ Pass API_KEY and CX_KEY properly
        results = get_search_results(query, API_KEY, CX_KEY)

        if results:
            summarized_results = summarize_results(results)
            for i, (title, link, summary) in enumerate(summarized_results, 1):
                print(f"{i}. {title}\n   🔗 {link}\n   📄 {summary}\n")
        else:
            print("❌ No results found.")

if __name__ == "__main__":
    main()
