from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Define the URL and user-agent header
url = 'https://prolifics.com/us/'
headers = {'User-Agent': 'Mozilla/5.0'}
list1=[]
# request bhej rahe hei.....
req = Request(url, headers=headers)

#  webpage content ko wapas la rahe hei ....
webpage = urlopen(req).read()

# BeautifulSoup lady data ko process kar rahi hei .....
soup = BeautifulSoup(webpage, 'html.parser')

#print(soup)
# Abb hum BeautifulSoup lady data pr process kr rahe hei.....
title = soup.title
print(soup.get_text())
# Title print ho raha hei ...
print("Page Title:", title)

# print  all Links present on that page
links = soup.find_all('a')
for link in links:
    print("Link:", link.get('href'))
# data = soup.find_all('div')
# for d in data:
#     print(d)
# data = soup.find_all('div')
# for d in data:
#   #  if "xlmns" not in str(d): 
#     #print(d.get_text())
#     code=d.get_text()
#     p="".join([s for s in code.splitlines(True) if s.strip("\r\n")])
#     print(p)
#     list1.append(p)
#     print("------end-------------------------------------")
# print(list1)