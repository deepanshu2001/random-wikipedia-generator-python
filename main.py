import requests
import webbrowser
from bs4 import BeautifulSoup


while True:
    link=requests.get("https://en.wikipedia.org/wiki/Special:Random")
    parsed_link=BeautifulSoup(link.content,"html.parser")
    title=parsed_link.find(class_="firstHeading").text
    ans=input(f"{title} Do you want to view the article(y/n):")

    if (ans=='y'):
         url = 'https://en.wikipedia.org//wiki//%s' %title
         webbrowser.open(url)
         break
    elif(ans=='n'):
        print("Generating next article")
        continue

    else:
        print("Invalid ans!")
        break

    
