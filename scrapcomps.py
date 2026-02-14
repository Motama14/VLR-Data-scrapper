import requests
from bs4 import BeautifulSoup

id = 1120
url = "https://www.vlr.gg/team/stats/" +str(id)
headers = {
        "User-Agent": "Mozilla/5.0"
    }

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

mapas = ["Bind", "Haven", "Split", "Ascent", "Icebox", "Breeze", "Fracture", "Pearl", "Lotus", "Sunset", "Abyss", "Corrode"]

for map in mapas:
    container = soup.find_all("div", class_="agent-comp-agg mod-first", attrs={"data-map": map})
    for contenedor in container[:3]:
        agent_img = contenedor.find_all("img")
        for agent in agent_img:
            raw = agent.get("src")
            print(raw[21:].replace(".png", ""))