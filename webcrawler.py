
"""
Created on Mon Jan 18 20:15:11 2021

@author: rafal

Webscrapping with beautifulsoup which is searching for any link in the 
specified URL, the scrapping is done by different threads and they
all print data in the console with titles and links for specific articles
"""


import requests
import bs4
import threading
from requests_html import HTMLSession
threads = []

session = HTMLSession()
url = 'https://news.google.com/publications/CAAqBwgKMNq-lgswveStAw?hl=pl&gl=PL&ceid=PL%3Apl'
page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, 'html.parser')

r = session.get(url)
r.html.render(sleep=1, scrolldown=1)

articles = r.html.find('article')

def crawl(req):
    for item in articles:
        try:
            newsitem = item.find('h3', first=True)
            
            #if you want titles and links for every article
            title = newsitem.text
            link = newsitem.absolute_links
            print(title, link)
            
            #if you only want links for every article
            link = newsitem.absolute_links
            print(link)
        except:
                pass

results = soup.find_all('h3')
for result in results:
    t = threading.Thread(target=crawl, args=(result,))
    threads.append(t)
    t.start()
    
    
    
