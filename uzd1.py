import requests
from bs4 import BeautifulSoup as bs4

response = requests.get("http://r64vsk.lv")
soup = bs4(response.content, "html.parser")

h1 = soup.find_all("h1")
print(len(h1))