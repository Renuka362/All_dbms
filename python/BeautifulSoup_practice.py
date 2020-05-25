from bs4 import BeautifulSoup

import requests

result = requests.get('https://www.flipkart.com').text


soup = BeautifulSoup(result,"html.parser")

with open('soup.html','w') as html_file:
    
    html_file.write(result)
    

match = soup.find('div',class_='_3dGepu')

print(match)
    
































"""
from bs4 import BeautifulSoup
import requests
 
with open('portfolio-website/assignment-12/assignment12.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')
    
#print(soup.prettify())    

match = soup.find('div', class_='get').h1.text
#print(match.prettify())
print(match)
"""

