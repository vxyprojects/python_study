
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
import selenium.webdriver.common.action_chains
from selenium.webdriver.common.keys import Keys

# import org.openqa.selenium.interactions.Actions;
from selenium import webdriver
from selenium.webdriver import ActionChains


# rnakfur.snsform.co.kr
urList = [
# 'https://www.facebook.com/dingo.beauty.kr/',
# 'https://www.facebook.com/doeateveryone/'
##
# 'https://www.facebook.com/mukbanglove/',
# 'https://www.facebook.com/goodplus/',
# 'https://www.facebook.com/greedplayeat/',
# 'https://www.facebook.com/goeatnow/',
##
#todo test
# 'https://m.facebook.com//goeatnow/videos/1761097247520508/'

# 'https://www.facebook.com/tastynews1/',
# 'https://www.facebook.com/noweatgo/',
# 'https://www.facebook.com/dessert39/',#얘는 아닌듯
];

save_root_dirname = '/Users/swlee/Documents/python/example/fb'

# 클릭하는것 까지 처리 함
# url = 'https://m.facebook.com//goeatnow/videos/1761097247520508/'
url = 'https://m.facebook.com//greedplayeat/videos/1486588684791739/'

driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver');


#todo 상혁이가 했던거 url 뽑아내서 그거 html 에 append 시키고 걔를 클릭 하도록
#todo 테스트 코드
#todo 버튼을 만들어줘서 어펜드 시켜놓고선 그 버튼 클릭해서 다운 또는 얼럿뜨는지 확인 그냥 url 고정으로 넣어주고 진행 해봐도 될듯 하다 
d =driver;
d.get(url);
# button = driver.find_elements_by_xpath("//div[@class='widePic']")[0]
button = driver.find_elements_by_xpath("//div[@class='widePic']")[0]

#todo datastore는 뽑아냄
soup = BeautifulSoup(d.page_source, "html.parser")
srcClass = soup.find('div', attrs={"class": "_53mw _4gbu"});
# print(srcClass[0]);
src=srcClass['data-store']
# print('src')
# print(src)
# https:\/\/video-icn1-1.xx.fbcdn.net\/v\/t42.1790-2\/23572497_1770510766582506_10659924145078272_n.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InN2ZV9zZCJ9&oh=d0699ba05a8518317f2b03c72ad934fc&oe=5A374A23
startString = '"src":';
endString = '"width":';
startPoint = src.find(startString)
endPoint = src.find(endString)

srcUrl=src[startPoint+len(startString):endPoint-1]
srcUrl=srcUrl.replace('"', "")
srcUrl=srcUrl.replace("\\", "")
print(srcUrl);
#todo 정규식으로 url 뽑아내야한다.
#regex = re.compile(r'/^(http(s?))*$/')
# \/\/
# regex = re.compile(r'/^((http(s?))\:\\/\\/)([0-9a-zA-Z\-]+\.)+[a-zA-Z]{2,6}(\:[0-9]+)?(\/\S*)?$/')
# regex = re.compile(r'/^(http(s?))+$/')
# # regex = re.compile(r'[0-9,]+명이')
# srcUrl = regex.search(src)
#
# print('srcUrl')
# print(srcUrl)
# "src":
#,"width"







#이게 먹힘 이유는 정확히 모름
new_html = "<span class='caps'>Moshi3</span>"
d.execute_script("""
var new_html= arguments[0];
var new_elem = document.createElement('div');
new_elem.innerHTML += ' ' + new_html;
document.querySelector('body').appendChild(new_elem);
""", new_html)

# 아래 처럼 하는건 안먹힘
# d.execute_script("""
# var new_html= <span class='caps'>Moshi2</span>;
# var new_elem = document.createElement('div');
# new_elem.innerHTML += ' ' + new_html;
# document.querySelector('body').appendChild(new_elem);
# """)



# chrome Save video as

# for oneList in urList:
#     instance = getReplyFb.fbCrawling(oneList,save_root_dirname)
#     # default를 5만큼 스크롤 다운으로 처리
#     # instance.scrollDown(120);# 대략 5월달까지 나옴
#     # instance.scrollDown(280);
#     # instance.scrollDown(5);
#     instance.get_set_CrawlingData();
#     instance.craeat_excel();
    #todo download 함수








######################test 코드

# js_code = """
#     var eventName = "keypress";
#     var keycode = 13;
#     var evt = document.createEvent("KeyboardEvent");
#     evt.initKeyboardEvent(eventName, true, true, window, false, false, false, false, keycode, keycode);
#     this.dispatchEvent(evt);
# """
# evaluateJavaScript(js_code)




# # actions.move_to_element(button).context_click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform();
#
# actions.move_to_element(button).context_click().send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform();
# actions.move_to_element(button).context_click().send_keys(Keys.ENTER).perform();
# actions.move_to_element(button).context_click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).build().perform();
# actions.move_to_element(button).context_click().perform();
# actions.send_keys(Keys.ARROW_DOWN).perform();
# actions.send_keys(Keys.ARROW_DOWN).perform();
# .send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).
# actions.context_click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform();
# actions.context_click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform();
# actions.move_to_element(button).context_click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform();
# actions.move_to_element(button).context_click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform();
# .sendKeys(Keys.ARROW_DOWN)
# Actions action = new Actions(driver).contextClick(element);
# action.build().perform();



# 'https://www.facebook.com/dingo.beauty.kr/',
# 'https://www.facebook.com/doeateveryone/',
# 'https://www.facebook.com/ummaworld/',
# 'https://www.facebook.com/%EB%8B%A4%EC%8B%9C%EB%B3%B4%EA%B3%A0-%EC%8B%B6%EC%96%B4%EC%A7%80%EB%8A%94-%EC%9E%AC%EB%B0%8C%EB%8A%94-%EB%8F%99%EC%98%81%EC%83%81-175874952913301/',
# # 'https://www.facebook.com/myarenatalk/' #todo 에외케이스가 존재한는듯
# # 'https://www.facebook.com/movie.soony/',#todo 예외케이스가 존재하는듯
# 'https://www.facebook.com/%EB%AA%B0%EB%9E%98%EC%B9%B4%EB%A9%94%EB%9D%BC-1955326091422367/',
# 'https://www.facebook.com/hothanpage/',
# 'https://www.facebook.com/todayblackbox/',
# 'https://www.facebook.com/%EC%8B%A4%EC%8B%9C%EA%B0%84-%EB%B2%A0%EC%8A%A4%ED%8A%B8-481044045330828/',
# 'https://www.facebook.com/%EC%96%B4%EC%A0%9C-%EB%86%93%EC%B9%9C-%EA%B7%B8%EC%98%88%EB%8A%A5-262935653892987/',
# 'https://www.facebook.com/THISISGag/',
# 'https://www.facebook.com/hahaha99990/',
# 'https://www.facebook.com/%EA%BF%80%EC%9E%BC%EC%9D%B4%EC%95%BC%EA%B8%B0-129496704317620/',
# 'https://www.facebook.com/Mr.gag/',
# 'https://www.facebook.com/humorbombbomb/',
# 'https://www.facebook.com/jojjang2/',
# 'https://www.facebook.com/min4rin/',
# 'https://www.facebook.com/everyfunnyshow/',
# 'https://www.facebook.com/%ED%9B%88%EB%85%80%ED%9B%88%EB%82%A8-607788719417060/',
# 'https://www.facebook.com/%EC%9D%B4%EA%B1%B0%EC%8A%A8-%EC%9D%BC%EB%B0%98%EC%9D%B8%EB%93%A4%EC%9D%98-%EC%8B%A4%EC%A0%9C%ED%9B%84%EA%B8%B0-326832394424319/',
# 'https://www.facebook.com/%EB%AA%B0%EB%9E%98%EC%B9%B4%EB%A9%94%EB%9D%BC-1955326091422367/',
# 'https://www.facebook.com/%EB%AF%B8%EC%B9%9C%EB%93%AF%EC%9D%B4-%EC%9B%83%EA%B2%A8%EC%A4%84%EA%B2%A4%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B-1342110162534549/',
# 'https://www.facebook.com/%EC%97%AC%EC%9E%90%EC%9D%98-%ED%99%94%EC%9E%A5%EB%B9%A8-738653119539669/'



#imbeded append js test
# script = "var new_html = '<span class='caps'>Moshi2</span>'\n"
# script += "var new_elem = document.createElement('div')\n"
# script += "new_elem.innerHTML += ' ' + new_html\n"
# script += "document.querySelector('body').appendChild(new_elem)\n"
# script2= "var new_elem = document.createElement('div')\n"
# script3= "new_elem.innerHTML += ' ' + new_html\n"
# script4= "document.querySelector('body').appendChild(new_elem)\n"
# print('script')
# print(script)
# d.execute_script('var new_html = "<span class="caps">Moshi2</span>";');


# d.execute_script('return var new_html = "<span class="caps">Moshi2</span>";');
# d.execute_script('return var new_html = "<span class="caps">Moshi2</span>";');
# d.execute_script('var new_html = "<span class="caps">Moshi2</span>""');
# d.execute_script('new_html = "<span class="caps">Moshi2</span>""');
# d.execute_script(script2);
# d.execute_script(script3);
# d.execute_script(script4);

# videourl =one_g_data.find_all('a', attrs={"class": "_5pcq"})
# makeVideourl = self.baseUrl+videourl[0]['href'];
# src = driver.find_elements_by_xpath("//div[@class='_53mw _4gbu']")[0]
# button = driver.find_elements_by_xpath("//input[@class='gsfi']")[0]
# button.click()
# time.sleep(3)
# actions = ActionChains(d)
# actions.send_keys(Keys.NUMPAD1);
# actions.move_to_element(button).send_keys(Keys.NUMPAD1).perform();
# actions.move_to_element(button).context_click()
# time.sleep(3);
# actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform();
# actions.send_keys(Keys.DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform();
# actions.send_keys(Keys.DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform();
# actions.move_to_element(button).click().context_click().send_keys(Keys.DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform();
# actions.move_to_element(button).context_click().send_keys(Keys.DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.NUMPAD1).perform();
# actions.context_click().send_keys(Keys.DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.NUMPAD1).perform();
# #todo send_keys(가 안먹는다 ...)

# #imbeded js
# d.execute_script('alert("a")');