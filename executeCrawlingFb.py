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


soup = BeautifulSoup(driver.page_source, "html.parser")
# print('soup')
# print(soup)
# d = soup.find_all("span", {"class": "_33vv"})
# print(d)
# print(d[0].text.strip())
dMainResult['page_name'] = soup.find_all("span", {"class": "_33vv"})[0].text.strip()

# print(dMainResult['page_name']);

# g_data = soup.find_all("div", {"class": "_1dwg _1w_m"})
g_data = soup.find_all("div", {"class": "userContentWrapper"})

# print('len(g_data)')
# print(len(g_data))

#엑셀을 만들기위한 전체 배열
aExcelResult =[];
for one_g_data in g_data:
    dOneRow = {};
    #날짜
    onerow_date = one_g_data.find_all('span', attrs={"class": "timestampContent"});
    onerow_date = onerow_date[0].text.strip()

    #링크
    onerow_share_count = one_g_data.find_all('a', attrs={"class": "UFIShareLink"});

    if len(onerow_share_count) > 0:
        onerow_share_count = onerow_share_count[0].text.strip()
    else :
        onerow_share_count = '0';

    #계시글 내용
    user_content = one_g_data.find('div', attrs={"class": "userContent"});

    if user_content is not None:
        user_content = user_content.findChildren();
        user_content = user_content[0].text.strip()
    else:
        user_content = 'not content';

    #좋아요
    onerow_like_count = one_g_data.find('div', attrs={"class": "UFILikeSentenceText"});
    if onerow_like_count is not None:
        onerow_like_count = onerow_like_count.findChildren();
        onerow_like_count = onerow_like_count[0].text.strip();
    else:
        onerow_like_count = '0';
    #todo 숫자만 뽑아서 평균치 뽑아낸다 .
    dOneRow['content_date'] = onerow_date;
    dOneRow['content'] = user_content;
    #todo explode 사용
    dOneRow['content_like_count'] = onerow_like_count;
    #todo explode 사용 뒤글자 지운다
    dOneRow['content_share_count'] = onerow_share_count;
    aExcelResult.append(dOneRow);

    # print('onerow_like_count')
    # print(onerow_like_count)



book = Workbook()
sheet = book.active
iResultIdx = 0;
for oneObject in aExcelResult:
    iResultIdx = iResultIdx + 1;
    for oneObjectIdx in oneObject:
        if oneObjectIdx == 'content_date':
            sheet['A' + str(iResultIdx)] = oneObject[oneObjectIdx]
        elif oneObjectIdx == 'content':
            sheet['B' + str(iResultIdx)] = oneObject[oneObjectIdx]
        elif oneObjectIdx == 'content_like_count':
            sheet['C' + str(iResultIdx)] = oneObject[oneObjectIdx]
        elif oneObjectIdx == 'content_share_count':
            sheet['D' + str(iResultIdx)] = oneObject[oneObjectIdx]

now = datetime.datetime.now()
nowDate = now.strftime('%Y-%m-%d')
nowTime = now.strftime('%H:%M:%S')
book.save(dMainResult['page_name'] + '_' + nowDate + '_' + nowTime + '.xlsx');