import requests
from bs4 import BeautifulSoup as bs4

#Jābūt pareizs klases nosaukums tāpat kā mājaslapā
choice = str(input())

response = requests.get("http://r64vsk.lv")
soup = bs4(response.content, "html.parser")

izm = soup.find("div", class_="r64-events").text

izmC = ""

for i in izm.splitlines():
    if choice in i:
        izmC = izmC + i
        izmC = izmC + "\n"


if not izmC:
    print("Not found")
else:
    print(izmC)




