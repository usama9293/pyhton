#url='C:\Users\USAMA\Desktop\practice\python\index.html'
from bs4 import BeautifulSoup
with open('index.html','r') as file:
    content=file.read()
    soup=BeautifulSoup(content,'html.parser')
    tags=soup.find_all('td')
    for word in tags:
        print(tags.contents)