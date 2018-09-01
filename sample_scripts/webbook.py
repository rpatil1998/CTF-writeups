import requests
from bs4 import BeautifulSoup

r=requests.get("http://34.216.132.109:8083/fp/")
html_doc=r.text
cookies=r.cookies
print(cookies)
count=0

while True:
	count+=1
	print(count)
	soup=BeautifulSoup(html_doc,'html.parser')
	action=soup.find('form').get('action')
	r2=requests.get("http://34.216.132.109:8083"+action,cookies=cookies)
	cookies=r2.cookies
	html_doc=r2.text
	if "flag" in html_doc:
		print html_doc
	