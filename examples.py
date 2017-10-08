from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import scrapy
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


# # Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
# # /Users/swlee/Downloads
driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver')

driver.get("https://story.kakao.com/ch/mom79")

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
    onerow_title = onerow_title[0].text.strip()


    onerow_reply =one_g_data.find_all('strong', attrs={"class": "_commentCount"})
    onerow_reply = onerow_reply[0].text.strip()
    dOneRow['product_name'] = onerow_title;
    dOneRow['proudct_reply_count'] = len(onerow_reply) == 0 and '0' or onerow_reply;
    lResult.append(dOneRow)

print(lResult);



