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

class ksCrawling:
    def __init__(self, url):
        # url -- 을 계속 적으로 넣어준다.
        self.driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver');
        self.d =self.driver;
        self.d.get("https://story.kakao.com/ch/banzzak2017");
        self.sChannel_name = self.d.find_element_by_class_name('_profileName');
        self.sChannel_id = self.d.find_element_by_class_name('user_id');
        self.dMainResult == {};
        self.lResult = [];



    def scrollDown(self):

        idx = 0;
        while True:
            aReturnRows = [];
            self.d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            # ++idx;
            idx = idx + 1;
            if idx == 5:
                # print(idx);
                break
        # return np.arange(0.0, self.endTime, self.sampleTime)


        def get_set_CrawlingData(self):
            soup = BeautifulSoup(self.d.page_source, "html.parser")
            g_data = soup.find_all("div", {"class": "_activityBody "})
            lResult = [];
            for one_g_data in g_data:
                dOneRow = {};
                onerow_title = one_g_data.find_all('strong', attrs={"class": "tit_channel"})
                # todo  15초는  타이틀을 안적어준다 해당의 경우 처리 해줘야한다
                # print(onerow_title)
                # print(len(onerow_title))
                if len(onerow_title) > 0:
                    onerow_title = onerow_title[0].text.strip()
                else:
                    ##todo  내용에서 첫줄 뽑아오는게 좋다
                    onerow_title = 'no title'
                onerow_reply = one_g_data.find_all('strong', attrs={"class": "_commentCount"})
                onerow_reply = onerow_reply[0].text.strip()
                dOneRow['product_name'] = onerow_title;
                dOneRow['proudct_reply_count'] = len(onerow_reply) == 0 and '0' or onerow_reply;
                lResult.append(dOneRow)
            # return self.amp * np.sin(2 * np.pi * self.freq * time + self.startTime) + self.bias

    def craeat_excel(self, time):
        book = Workbook()
        sheet = book.active
        iResultIdx = 0;

        iTotalRow = len(self.lResult);
        sumReply = 0;
        for oneObject in self.lResult:
            # row
            # print(oneObject);
            iResultIdx = iResultIdx + 1;
            for oneObjectIdx in oneObject:
                sheet['A' + str(iResultIdx)] = 'DATE'
                if oneObjectIdx == 'product_name':
                    sheet['B' + str(iResultIdx)] = oneObject[oneObjectIdx]
                elif oneObjectIdx == 'proudct_reply_count':
                    sheet['C' + str(iResultIdx)] = oneObject[oneObjectIdx]
                    sumReply = sumReply + int(oneObject[oneObjectIdx]);

        sheet['A' + str(iResultIdx + 1)] = self.dMainResult['channel_name'];
        sheet['B' + str(iResultIdx + 1)] = '댓글평균'
        sheet['C' + str(iResultIdx + 1)] = str(math.ceil(sumReply / iTotalRow))

        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')
        nowTime = now.strftime('%H:%M:%S')
        book.save(self.dMainResult['channel_name'] + '_' + nowDate + '_' + nowTime + '.xlsx');
