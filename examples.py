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




# d= driver.find_element_by_class_name('tit_channel')
# print('d')
# # print(d[1].text)
# print(type(d))

# 테스트 사이드바 스토리라는 글귀
# sTest = driver.find_element_by_class_name('tit_story');
# print(sTest.text);


#todo 테스트
tIdx = 0;
all_product_title = driver.find_elements_by_xpath("//strong[@class='tit_channel']")
for one_title in all_product_title:
    tIdx = tIdx +1;
    # print(tIdx)
    # print(one_title.text)

# all_product_reply = driver.find_elements_by_xpath("//strong[@class='_commentCount']")
# for one_title_reply in all_product_reply:
#     if one_title_reply.text == '':
#         print('0');
#     print(one_title_reply.text)



# section _activity 에서 돌아가면서  나와야한다 그래서 댓글이라는 단어가 없으면 0  있으면 댓글 개수를 긁어야한다 .
# <div data-kant-group="feed.u" class="_activityBody ">



# WebDriverWait(driver, 20)
# driver.wait = WebDriverWait(driver, 10)

# print('111')
# driver.implicitly_wait(10)
# print('222')
# print('111')
# 3초멈추는것은 먹힘
# time.sleep(3)
# print('222')

soup = BeautifulSoup(driver.page_source, "html.parser")
g_data = soup.find_all("div", {"class": "_activityBody "})
lResult =[];
for one_g_data in g_data:
    dOneRow = {};
    onerow_title =one_g_data.find_all('strong', attrs={"class": "tit_channel"})
    onerow_title = onerow_title[0].text.strip()


    onerow_reply =one_g_data.find_all('strong', attrs={"class": "_commentCount"})
    onerow_reply = onerow_reply[0].text.strip()
    # print(onerow_title[0].text.strip())
    # print('tt')
    # # print(tt[0].text.strip())
    # print(tt[0])
    # print('---------')
    # print('---------')
    # print(tt)
    # print('---------')
    # print('---------')
    #클래스 타입
    # print(type(tt))
    #왜 체크 안되는지 모르겠다 .
    # print(type(tt[0]))
    dOneRow['product_name'] = onerow_title;
    dOneRow['proudct_reply_count'] = len(onerow_reply) == 0 and '0' or onerow_reply;
    lResult.append(dOneRow)



all_product_sectors = driver.find_elements_by_xpath("//div[@class='_activityBody ']")
#todo  23개  확실한데  내 생각에  렌더링 되기전에 여기가  돌아서 그런 느낌인데 wait 를 사용 해줘야할듯 하다
testidx = 0;
lResult =[];
for one_product_sector in all_product_sectors:
    dOneRow = {};
    testidx = testidx+1;
    # wait = WebDriverWait(browser, 10)
    # wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="hplogo"]')))
    product_name = one_product_sector.find_element_by_class_name('tit_channel')
    # print(testidx);
    # print(product_name.text);

    is_product_reply_count = one_product_sector.find_element_by_class_name('_commentCount')
    # if len(is_product_reply_count.text) == 0:
    # 댓글이 없는경우 if 문 안으로 들어옴
    #     print(product_name.text);
    #     print(type(is_product_reply_count))
    # print('type(is_product_reply_count)')
    #todo 아래 class에 0 값이  추가가 안되는데  왜 안되는지  모르겠다
    # is_product_reply_count.text = '0';
    dOneRow['product_name'] = product_name.text;
    dOneRow['proudct_reply_count'] = len(is_product_reply_count.text) == 0 and '0' or is_product_reply_count.text ;
    lResult.append(dOneRow)
    # product_reply = one_product_sector.find_element_by_class_name('_commentCount')

# print('lResult')
# print(lResult)



# todo test 내용
    # product_contents = one_product_sector.find_element_by_class_name('_content')
    # print(product_contents.text);