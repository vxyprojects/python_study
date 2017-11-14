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
import getReplyFb


#url 돌면서  인스탄스  계속 생성 하면서  처리 해준다

# 고여사는 아래와 같은 스타일
# rnakfur.snsform.co.kr
#todo 이상하네 12시에 안돌아가던게 지금은 다돌아가네?  이유를 모르겠음 낼도 12시정도에 돌려보자  안되는지
#d
urList = [
'https://www.facebook.com/dingo.beauty.kr/',
'https://www.facebook.com/doeateveryone/'
];




for oneList in urList:
    instance = getReplyFb.fbCrawling(oneList)
    #default를 5만큼 스크롤 다운으로 처리
    # instance.scrollDown(120);# 대략 5월달까지 나옴
    # instance.scrollDown(280);
    instance.scrollDown(5);
    instance.get_set_CrawlingData();
    instance.craeat_excel();