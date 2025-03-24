import requests

def get_search_results(query, api_key, cx_key):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx_key}"

    response = requests.get(url)
    data = response.json()

    if "items" in data:
        return [(item["title"], item["link"], item.get("snippet", "")) for item in data["items"][:5]]
    else:
        return []
