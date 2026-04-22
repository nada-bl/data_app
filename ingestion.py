import requests

url = "https://github.com/search?q=mental+health+ai&type=repositories"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

print(f"Response Status: {response.status_code}")

if response.status_code == 200:
    with open("github_HTTP.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("HTML content successfully saved to github_HTTP.txt")
else:
    print("Failed to retrieve the page.")
