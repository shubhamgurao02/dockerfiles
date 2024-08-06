import urllib.request
from bs4 import BeautifulSoup


url = 'https://prolifics.com/us/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
divs = soup.find_all('div')
for div in divs:
    div_links = div.find_all('a')
    for link in div_links:
        link_text = link.text.strip()
        link_url = link.get('href')
        if link_url:
            
            print(f"Link Text: {link_text}")
            print(f"Link URL: {link_url}")

    div_text = div.get_text(strip=True)
    if div_text:
        
        print(f"Text within the <div>: {div_text}")

    