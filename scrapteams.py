import requests
from bs4 import BeautifulSoup


url = "https://www.vlr.gg/event/2685"
headers = {
        "User-Agent": "Mozilla/5.0"
    }

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

container = soup.find("div", class_="wf-module-item event-team-name")

teams = soup.find_all("a", class_="wf-module-item event-team-name")

for team in teams:
    print(team.text[11:])