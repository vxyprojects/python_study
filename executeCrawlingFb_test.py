
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


#url 돌면서  인스탄스  계속 생성 하면서  처리 해준다

# 고여사는 아래와 같은 스타일
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
];

save_root_dirname = '/Users/swlee/Documents/python/example/fb'
# eys.ARROW_DOWN

# 클릭하는것 까지 처리 함
url = 'https://m.facebook.com//goeatnow/videos/1761097247520508/'
# url = 'https://www.google.co.kr/'

driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver');
d =driver;
d.get(url);
button = driver.find_elements_by_xpath("//div[@class='widePic']")[0]
# button = driver.find_elements_by_xpath("//div[@class='widePic']")[0]
# button = driver.find_elements_by_xpath("//input[@class='gsfi']")[0]
# button.click()
# time.sleep(3)
actions = ActionChains(d)
# actions.send_keys(Keys.NUMPAD1);
# actions.move_to_element(button).send_keys(Keys.NUMPAD1).perform();
# actions.move_to_element(button).context_click()
# time.sleep(3);
# actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform();
# actions.send_keys(Keys.DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform();
# actions.send_keys(Keys.DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform();
actions.move_to_element(button).click().context_click().send_keys(Keys.DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform();
# actions.move_to_element(button).context_click().send_keys(Keys.DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.NUMPAD1).perform();
# actions.context_click().send_keys(Keys.DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.NUMPAD1).perform();
# #todo send_keys(가 안먹는다 ...)

# #imbeded js
# d =driver;
# d.execute_script('alert("a")');

# js_code = """
#     var eventName = "keypress";
#     var keycode = 13;
#     var evt = document.createEvent("KeyboardEvent");
#     evt.initKeyboardEvent(eventName, true, true, window, false, false, false, false, keycode, keycode);
#     this.dispatchEvent(evt);
# """
# evaluateJavaScript(js_code)

# from spidermonkey import Runtime
# rt = Runtime()
# cx = rt.new_context()
# result = cx.eval_script("alert('aa')")



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