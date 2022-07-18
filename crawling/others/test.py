import requests
import sys
from bs4 import BeautifulSoup

url = 'https://www.rocketpunch.com/search?keywords=data_scientist'
headers = {
"authority": "www.rocketpunch.com",
"method": "GET",
"path": "/api/search/template?keywords=data_scientist&q=",
"scheme": "https",
"accept": "*/*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
"cache-control": "no-cache",
"cookie": "csrftoken=hGI9Prc93HGYm8kr0KiOxYEI54m40XGSiqnHw5i7ivOWgkO55OyFZUhcSGUSvvdo; rocketpunch=mhp9o6n18gklx0gfqp4ju0y945vt0ghz; _ga=GA1.2.126093574.1657779506; _gid=GA1.2.593987535.1657779506; _fbp=fb.1.1657779505751.689946770; _clck=wv2g8f|1|f35|0; uvts=915b9402-c223-495a-4a8d-5eb2c3cce611; _clsk=1js47n7|1657784978537|2|1|n.clarity.ms/collect",
"pragma": "no-cache",
"referer": "https://www.rocketpunch.com/search?keywords=data_scientist",
"sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform":'"Windows"',
"sec-fetch-dest": "empty",
"sec-fetch-mode": "same-origin",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
"x-csrftoken": "hGI9Prc93HGYm8kr0KiOxYEI54m40XGSiqnHw5i7ivOWgkO55OyFZUhcSGUSvvdo"
}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")
print (soup)
card = soup.find("div", class_="company item")
#rint (card)

'''
url1 = 'https://www.wanted.co.kr/wd/92325'
r1 = requests.get(url)
soup1 = BeautifulSoup(r1.text, 'html.parser')
print (soup1)
job = soup1.find("div", class_='JobContent_deswcriptionWrapper__SM4UD')
print (job)
'''
