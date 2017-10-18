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

# # Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
# # /Users/swlee/Downloads
driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver')

# driver.get("https://story.kakao.com/ch/mom79")
# 타이틀을 안적어준다
# driver.get("https://story.kakao.com/ch/15diet")
# driver.get("https://story.kakao.com/ch/0u82")

# 타이틀을 안적어주는게 있다
driver.get("https://story.kakao.com/ch/banzzak2017")

sChannel_name = driver.find_element_by_class_name('_profileName');
sChannel_id = driver.find_element_by_class_name('user_id');


dMainResult = {};
dMainResult['channel_name'] = sChannel_name.text;
dMainResult['channel_id'] = sChannel_id.text;

# print('dMainResult')
# print(dMainResult)


idx = 0;
while True:
    aReturnRows = [];
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    # ++idx;
    idx = idx+1;
    if idx == 5:
        # print(idx);
        break


soup = BeautifulSoup(driver.page_source, "html.parser")
g_data = soup.find_all("div", {"class": "_activityBody "})
lResult =[];
for one_g_data in g_data:
    dOneRow = {};
    onerow_title =one_g_data.find_all('strong', attrs={"class": "tit_channel"})
    #todo  15초는  타이틀을 안적어준다 해당의 경우 처리 해줘야한다
    # print(onerow_title)
    # print(len(onerow_title))
    if len(onerow_title) >0:
        onerow_title = onerow_title[0].text.strip()
    else:
        ##todo  내용에서 첫줄 뽑아오는게 좋다
        onerow_title = 'no title'
    onerow_reply =one_g_data.find_all('strong', attrs={"class": "_commentCount"})
    onerow_reply = onerow_reply[0].text.strip()
    dOneRow['product_name'] = onerow_title;
    dOneRow['proudct_reply_count'] = len(onerow_reply) == 0 and '0' or onerow_reply;
    lResult.append(dOneRow)

# print(lResult);
# 엑셀사용
book = Workbook()
sheet = book.active
iResultIdx = 0;

# 23
# print(len(lResult));
# print(lResult);
iTotalRow = len(lResult);
sumReply = 0;
for oneObject in lResult:
    #row
    # print(oneObject);
    iResultIdx = iResultIdx + 1;
    for oneObjectIdx in oneObject:
        # print(oneObjectIdx);
        # print(oneObject[oneObjectIdx]);
        # print(iResultIdx);
        # print(oneObject[oneObjectIdx])
        sheet['A'+str(iResultIdx)] = 'DATE'
        if oneObjectIdx == 'product_name':
            sheet['B' + str(iResultIdx)] = oneObject[oneObjectIdx]
        elif oneObjectIdx == 'proudct_reply_count':
            sheet['C' + str(iResultIdx)] = oneObject[oneObjectIdx]
            sumReply = sumReply +int(oneObject[oneObjectIdx]);
            # oneObject[oneObjectIdx]

# print('sumReply');
# print(sumReply);
sheet['A'+str(iResultIdx+1)] = dMainResult['channel_name'];
sheet['B'+str(iResultIdx+1)] = '댓글평균'
sheet['C'+str(iResultIdx+1)] = str(math.ceil(sumReply/iTotalRow))

# # sheet['A1'] = DATE
# # sheet['B1'] = 56
# # sheet['C1'] = 56
# # sheet['A2'] = 43
# now = time.strftime("%x")
# sheet['A3'] = now

now = datetime.datetime.now()
nowDate = now.strftime('%Y-%m-%d')
nowTime = now.strftime('%H:%M:%S')
book.save(dMainResult['channel_name']+'_'+nowDate+'_'+nowTime+'.xlsx');