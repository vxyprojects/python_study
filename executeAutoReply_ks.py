import matplotlib.pyplot as plt
import getReplyKakaoSt
import re
import os;
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
import os;
from selenium.webdriver import ActionChains;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.chrome.options import Options

urList = [

# 'https://story.kakao.com/ch/ggogga7', #광주업체
];



loginUrl = 'https://accounts.kakao.com/login?continue=https://ch.kakao.com';


# email
#password

options = Options()
options.add_argument("--disable-notifications")
# self.driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver');
driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver', chrome_options=options);

#todo 이걸 파일을 읽어서 처리 하도록 해야함 보안적으로
id = 'dltkddnr1216@naver.com'
passw = '';

url='https://accounts.kakao.com/login?continue=https://ch.kakao.com';
driver.get(url);
username = driver.find_element_by_id('email')
username.send_keys(id)

password = driver.find_element_by_id('password')
password.send_keys(passw)



form = driver.find_element_by_id('login-form')
form.submit();
time.sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")
dMainResult = {};

# dMainResult['page_name'] = soup.find_all("span", {"class": "channel-list-item"})[0].text.strip()
# g_data = soup.find_all("span", {"class": "channel-list-item"})
# base_ks_url = 'https://story.kakao.com/ch/';
base_manager_ks_url = 'https://ch.kakao.com/channels/';

g_data = soup.find_all("div", {"class": "member-wrap"})
# another_driver =webdriver.Chrome('/Users/swlee/Downloads/chromedriver');

for one_g_data in g_data:
    aTag=one_g_data.find_all('a')
    # print(aTag[0]['href']);
    #/channels/@
    channelId = aTag[0]['href'].replace("/channels/", "")
    # print(channelId);
    connectKsMakeUrl = base_manager_ks_url+ channelId;
    # print(connectKsMakeUrl)
    #todo 테스트 용 if
    # if connectKsMakeUrl == 'https://story.kakao.com/ch/childhealth':
    if connectKsMakeUrl == 'https://ch.kakao.com/channels/@childhealth':
        # another_driver.get(connectKsMakeUrl);
        #todo 여기서 배열을 만들어주고 그 배열을 또 이용해서 다시 돌리는것도 좋지만 생각하니깐 두번 돌리는거 같아서 그렇게는 진행하지 말자
        #todo another가 아닌 로그인 드라이버를 이용해서 카스매니저에 접속하자
        driver.get(connectKsMakeUrl);
        managerSoup = BeautifulSoup(driver.page_source, "html.parser")
        for_reply_boards = managerSoup.find_all('div',{'class' : 'activity-item story-box'})

        # idx=0;
        # while True:
        #     aReturnRows = [];
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(1)
        #     # ++idx;
        #     idx = idx + 1;
        #     # if idx == 5:
        #     if idx == 1:
        #         # print(idx);
        #         break


        #todo more 이 있는지 없는지
        #todo more 이 없어질때까지 눌러준다.


        for i in range(0,3):
            # for_reply_boards[i];
            # print(for_reply_boards[i])
            # print(for_reply_boards[i])
            # print(for_reply_boards[i].find('ul', attrs={"class": "comments"}))
            # print(for_reply_boards[i].find('div', attrs={"class": "comment-count"}).text.strip())
            # for_reply_boards[i].find('div', attrs={"class": "comment-count"}).text.strip().replace("댓글 ", "");
            # print(for_reply_boards[i].find('div', attrs={"class": "comment-count"}).text.strip().replace("댓글 ", ""))
            #comment - count
            # int(for_reply_boards[i].find('div', attrs={"class": "comment-count"}).text.strip().replace("댓글 ", ""));
            if int(for_reply_boards[i].find('div', attrs={"class": "comment-count"}).text.strip().replace("댓글 ", "")) >2:
                # more
                moreButton = for_reply_boards[i].find('a', attrs={"class": "more"})
                # moreButton = for_reply_boards[i].find('div', attrs={"class": "more-area"})
                print('here?')

                # driver.find_element_by_xpath("//form[@class='ui form']/button").click()


                # print(moreButton);
                # print(type(moreButton));
                # moreButton.click();
                # actions = ActionChains(driver)
                # actions.move_to_element(moreButton).click()

            #todo 더보기가 있는경우는 무조건 두개가 나와있음
            # 2개를 빼고  30씩자르고 마지막에 남은 개수가 있음 총 74개면 2개를 뺀 72개 이고 2번 더보기 누르고  12개가 남아있다

            # moreButton.click()
            # print(moreButton);


            # comments = for_reply_boards[i].find('ul', attrs={"class": "comments"})
            # for oneComment in comments:
            #     # print(oneComment);
            #     #todo 더보기가 보이는경우는 더보기를 다 눌러야한다.
            #     print(oneComment.find_all('span',{'class' : 'user-name'}));




# g_data = soup.find_all("div", {"class": "userContentWrapper"})



# channel-list-item story-box
# member-wrap
# h3 a 태그의 href 들이 카카오 스토리 url 이다 .


# /channels/@mom79
# 'https://story.kakao.com/ch/'mom79
# https://story.kakao.com/ch/momom10


#todo 그냥 맨처음 돌아가는 용으로
#todo 시간마다 도는애 n자를 보고 반응형 하는 기술
#todo 재고수량 부족하다는 두번째 푸쉬 보내는

# def login(self, id, pssword, url):
    # 사용자 ID
    # username = self.d.find_element_by_id('email')
    # username.send_keys(id)
    # # 사용자 PASSWORD
    # password = self.d.find_element_by_id('pass')
    # password.send_keys(pssword)
    # # 'loginForm' element id # submit
    # form = self.d.find_element_by_id('login_form')
    # form.submit()
    # time.sleep(2);
    # # time.sleep(3);
    # # get back
    # self.d.get(url);
    # actions = ActionChains(self.d)
    # actions.send_keys(Keys.ESCAPE).perform();


# payLinkModeOn = 'F'; # T OR F
# save_root_dirname = '/Users/swlee/Documents/python/example/fb'
# for oneList in urList:
#     instance = getReplyKakaoSt.ksCrawling(oneList,save_root_dirname,payLinkModeOn)
#     # instance = getReplyKakaoSt.ksCrawling(oneList,save_root_dirname)
#     #default를 5만큼 스크롤 다운으로 처리
#     # instance.scrollDown(120);# 대략 5월달까지 나옴
#     # instance.scrollDown(280);
#     instance.scrollDown(5);
#
#     instance.get_set_CrawlingData();
#     instance.craeat_excel();



