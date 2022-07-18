import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')        ## Head-less 설정
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
chromedriver = '../data/chromedriver.exe'

base_url = "https://www.saramin.co.kr/zf_user/search?searchword="
driver = webdriver.Chrome(chromedriver, options=options)
driver.get(base_url)
time.sleep(10);
html = driver.page_source
#rint (html)
driver.quit()
