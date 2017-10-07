from selenium import webdriver
import time
import scrapy
from selenium.webdriver.support.ui import WebDriverWait

# # Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
# # /Users/swlee/Downloads
driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver')

driver.get("https://story.kakao.com/ch/mom79")

sChannel_name = driver.find_element_by_class_name('_profileName');
sChannel_id = driver.find_element_by_class_name('user_id');


dMainResult = {};
dMainResult['channel_name'] = sChannel_name.text;
dMainResult['channel_id'] = sChannel_id.text;

print('dMainResult')
print(dMainResult)


idx = 0;
dOneRow = {};


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

# p_element = driver.find_elements_by_tag_name("p")
# print(p_element[1].text)


# 테스트 사이드바 스토리라는 글귀
# sTest = driver.find_element_by_class_name('tit_story');
# print(sTest.text);


#
# all_product_title = driver.find_elements_by_xpath("//strong[@class='tit_channel']")
# for one_title in all_product_title:
#     print(one_title.text)
#
# all_product_reply = driver.find_elements_by_xpath("//strong[@class='_commentCount']")
# for one_title_reply in all_product_reply:
#     if one_title_reply.text == '':
#         print('0');
#     print(one_title_reply.text)



# section _activity 에서 돌아가면서  나와야한다 그래서 댓글이라는 단어가 없으면 0  있으면 댓글 개수를 긁어야한다 .
# <div data-kant-group="feed.u" class="_activityBody ">

all_product_sectors = driver.find_elements_by_xpath("//div[@class='_activityBody ']")

# print(type(all_product_sectors))
# print(len(all_product_sectors))

# driver.implicitlywait(10)
# WebDriverWait(driver, 20)
# driver.wait = WebDriverWait(driver, 10)

# browser.implicitly_wait(3)


# 23개  확실한데
testidx = 0;
for one_product_sector in all_product_sectors:
    # print(one_product_sector)
    # print('product_name')
    # tit_channel
    testidx = testidx+1;
    product_name = one_product_sector.find_element_by_class_name('tit_channel')
    print(testidx)
    is_product_reply = one_product_sector.find_element_by_class_name('_btnViewComments')
    print(product_name.text)
    # print(is_product_reply.text)

    # product_reply = one_product_sector.find_element_by_class_name('_commentCount')


# count = driver.find_element_by_xpath("//strong[@class='tit_channel']");
# print('count');
# print(type(count));

# e = driver.find_element_by_class_name('tit_channel');

# e = driver.find_element_by_class_name('tit_channel');
# e = driver.find_element_by_class_name('desc_info');


# p = driver.find_element_by_class_name('_profileName');
# p = driver.find_element_by_class_name('user_id');
# print('e')
# print(e)
# print('e.size')
# print(e.size)


# print(p)
# print('p')
# print(p.text)
# print(type(p.text));

# e = '살림의여왕';
# print('e');
# print(e);
# print(e.text)
# print(e.value)

# Element.text

# find_element_by_id('')
# de=e.find_element('By.CLASS_NAME' ,'tit_channel')

# print('len')
# print('de')
# print(de)
# print(len(e))
# print(e.value_of_css_property())
# e

# int count = selenium.getXpathCount("//span[@class='firstLanguage']").intValue();
# for (int i =1; i <= count; i ++){
# System.out.println(selenium.getText("//span["+i+"]"));
# }

# aReturnRows['sTitle'] = driver.find_element_by_id('lst-ib')
# aReturnRows['sReply'] = driver.find_element_by_id('lst-ib')
# aReturnRows['sfavorite'] = driver.find_element_by_id('lst-ib')
# aReturnRows.append(aReturnRows)
