from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import scrapy
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from openpyxl import Workbook
import math
import datetime
import re

#url 돌면서  인스탄스  계속 생성 하면서  처리 해준다

# 고여사는 아래와 같은 스타일
# rnakfur.snsform.co.kr
#todo 이상하네 12시에 안돌아가던게 지금은 다돌아가네?  이유를 모르겠음 낼도 12시정도에 돌려보자  안되는지
urList = [
'https://www.facebook.com/dingo.beauty.kr/',
];

dMainResult = {};

testUrl ='https://www.facebook.com/dingo.beauty.kr/'

driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver');


driver.get(testUrl);

soup = BeautifulSoup(driver.page_source, "html.parser")



dMainResult['page_name'] = soup.find_all("span", {"class": "_profileName"})[0].text.strip()


g_data = soup.find_all("div", {"class": "_1dwg _1w_m"})
# _33vv span
# 날짜는  timestampContent 안에 있다
# _4arz 안에 span  data-hover="tooltip" 얘
#js_1tt 좋아요 수 근데 다 다르다
# UFIShareLink a 태그  안에  dialog 태그
# UFIShareLink
#js_24k 공유하기수 근데 다다르다

idx = 0;
#디폴트가  5번인데
while True:
    aReturnRows = [];
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    # ++idx;
    idx = idx + 1;
    # if idx == 5:
    if idx == 5:
        # print(idx);
        break