import requests
from bs4 import BeautifulSoup

url = "https://store.steampowered.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    popular_game_containers = soup.find("div", id= "tab_topsellers_content")

    if popular_game_containers:
         game_containers = popular_game_containers.find_all("a", class_="tab_item")
    
    with open("popular_games.txt", "w", encoding="utf-8") as file:
        for game in game_containers:
            game_title = game.find("div", class_="tab_item_name")
            if game_title:
                file.write(game_title.text.strip() + "\n")
            else: 
                print("Game title not found")

else: 
    print("Failed to retreive from Steam.")
