import requests
from bs4 import BeautifulSoup as bs4

response = requests.get("http://r64vsk.lv")
soup = bs4(response.content, "html.parser")

izm = soup.find("div", class_="r64-events")


text = izm.text

print(text)