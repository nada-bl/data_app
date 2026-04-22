from bs4 import BeautifulSoup
import pandas as pd
import json


with open("github_HTTP.txt", "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')



script_tag = soup.find('script', {'data-target': 'react-app.embeddedData'})

extracted_data = []

if script_tag:
    # We use json to turn the text into a list Python understands
    data_json = json.loads(script_tag.string)
    results = data_json['payload']['results']
    
    for item in results:
        # Pull out the info for each repo
        title = item.get('hl_name', '').replace('<em>', '').replace('</em>', '')
        repo_info = item.get('repo', {}).get('repository', {})
        owner = repo_info.get('owner_login', '')
        name = repo_info.get('name', '')
        
        extracted_data.append({
            "Title": title,
            "URL": f"https://github.com/{owner}/{name}",
            "Description": item.get('hl_trunc_description', 'No description')
        })


df = pd.DataFrame(extracted_data)
df.to_csv("mental_health_competitors.csv", index=False)

print(f"Success! Found {len(extracted_data)} repositories.")
