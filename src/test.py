import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('--headless')        ## Head-less 설정
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=options)


base_url = "https://www.rocketpunch.com/jobs"
data_scientist = "데이터 사이언티스트"

driver.get(base_url)
