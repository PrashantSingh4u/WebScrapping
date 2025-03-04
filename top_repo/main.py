import requests #importing requests module
from bs4 import BeautifulSoup
topics_url = "https://github.com/topics"
response = requests.get(topics_url)

print(response.status_code)
pagecontent = response.text
print(pagecontent[:1000])  # the first 1000 characters

with open('webpage.html', 'w', encoding='utf-8') as f:
    f.write(pagecontent)

doc = BeautifulSoup(pagecontent, 'html.parser')

selection_class = 'f3 lh-condensed mb-0 mt-1 Link--primary'
p_tags = doc.find_all('p',{'class': selection_class})
print(len(p_tags))
print(p_tags [:5])