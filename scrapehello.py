
from bs4 import BeautifulSoup

f = open("hello.html")
html = f.read()
soup = BeautifulSoup(html, 'html.parser')
    
    
# searching by class
all_goodbye_items = soup.find_all(id="goodbye-list", class_='goodbye')
    
print('goodbye items:', all_goodbye_items)
print('------')
    
print('All goodbye items:')
for item in all_goodbye_items:
    print(item.string)
print('------')
    
img_tag = soup.find('img')
print('The img width:')
print(img_tag['width'])
print('------')

print('The img url')
print(img_tag['src'])

