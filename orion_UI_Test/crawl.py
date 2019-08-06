import requests
from bs4 import BeautifulSoup
import re
sum = 0
url = 'https://book.douban.com/subject/1456692/comments/'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('span', 'short')
for item in pattern:
    print(item.string)

pattern_s = re.compile('<span class="user-stars allstar(.*?)rating"')

p = re.findall(pattern_s,r.text)
for star in p:
    sum +=int(star)
print(sum)