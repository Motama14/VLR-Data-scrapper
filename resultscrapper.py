import requests
from bs4 import BeautifulSoup

id = 59563

for i in range(1,10):
    url = "https://vlr.gg/"+str(id)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    cont_equipo1 = soup.find("div", class_="match-header-link-name mod-1")
    cont_equipo2 = soup.find("div", class_="match-header-link-name mod-2")

    equipo1 = cont_equipo1.find("div", class_="wf-title-med").text.strip()
    equipo2 = cont_equipo2.find("div", class_="wf-title-med").text.strip()

    cont_score = soup.find("span", class_="match-header-vs-score-colon")
    
    cont1 = cont_score.find_previous_sibling("span")
    cont2 = cont_score.find_next_sibling("span")
    
    res1 = cont1.text.strip()
    res2 = cont2.text.strip()
    
    print("Equipo 1: " +equipo1+ ":" +str(res1))
    print("Equipo 2: " +equipo2+ ":" +str(res2))
    id += 1
    if id == 595640:
        id += 1