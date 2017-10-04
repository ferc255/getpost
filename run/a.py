import urllib
import urllib.request
from bs4 import BeautifulSoup
"""
import request
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}

url = "https://linkedin.com/company/1005"

r = requests.get(url, headers=headers)
print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
"""
"""
hostname = urllib.parse.urlparse('http://docs.google.com').hostname
html_page = urllib.request.urlopen("http://vk.com")
soup = BeautifulSoup(html_page, 'lxml')
for link in soup.findAll('a'):
    print(link.get('href'))
"""


print("jjjjjjjjjjjjjjjjjjjjjjjjj")

"""
url = 'http://www.bbc.co.uk'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {}
headers = { 'User-Agent' : user_agent }

data = {}
req = urllib.request.build_opener()
req.addheaders = [('User-agent', 'Mozilla/5.0')]
req.open('http://vk.com')
q = req.read()
"""

user_agent = 'Mozilla/5.0 (Windows)'#; U; Windows NT 5.1; it; rv:1.8.1.11) '
url = 'http://vk.com'
req = urllib.request.Request(url, headers={'User-Agent': user_agent})
resp = urllib.request.urlopen(req)
print(resp.getcode())
html = resp.read()


soup = BeautifulSoup(html, 'lxml')
for link in soup.findAll('a'):
    if (link.get('href')):
        print(link['href'])
