import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url='https://py4e-data.dr-chuck.net/comments_1891489.html'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags=soup('span')
sum=0
for word in tags:
    nums=(word.contents[0])
    nums=int(nums)
    sum+=nums
    print(sum)