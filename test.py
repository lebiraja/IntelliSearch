import requests

# Replace with your API Key & Search Engine ID
API_KEY = "AIzaSyD50sjuTCEKhe6FFM06_lf2SXecWBpCV8Q"
CX_KEY = "74c299e208bb94cbc"

def get_search_results(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX_KEY}"

    response = requests.get(url)
    data = response.json()

    if "items" in data:
        results = [(item["title"], item["link"]) for item in data["items"][:5]]
        return results
    else:
        return []

# Example usage
if __name__ == "__main__":
    query = input("Enter your search query: ")
    results = get_search_results(query)

    if results:
        for i, (title, link) in enumerate(results, 1):
            print(f"{i}. {title}\n   🔗 {link}\n")
    else:
        print("❌ No results found.")
