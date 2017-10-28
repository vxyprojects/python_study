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


class ksCrawling:
    def __init__(self, url):
        self.dMainResult = {};
        self.lResult = [];
        # url -- 을 계속 적으로 넣어준다.
        self.driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver');
        self.d =self.driver;
        #url = https://story.kakao.com/ch/banzzak2017
        self.d.get(url);

        # 갑자기 왜 이게 안먹히는지  이유를 모르겠다 self.d.find_element_by_class_name html 구조가 바뀐건지 머로 막아놓은건지 정확한 이유 아직 모름
        # self.sChannel_name = self.d.find_element_by_class_name('_profileName');
        # self.sChannel_id = self.d.find_element_by_class_name('user_id').text;
        # self.dMainResult['channel_name'] = self.d.find_element_by_class_name('_profileName').text;




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

        # 구매링크
        # self.e = webdriver.Chrome('/Users/swlee/Downloads/chromedriver');
        # test = self.e.get('https://goo.gl/#analytics/goo.gl/WpGJw7/all_time')
        # paymentPage = BeautifulSoup(self.e.page_source, "html.parser")
        # payLinkCount = paymentPage.find_all('div', attrs={"class": "count"})

        g_data = soup.find_all("div", {"class": "_activityBody "})
        self.dMainResult['channel_name'] = soup.find_all("span", {"class": "_profileName"})[0].text.strip()
        self.dMainResult['channel_id'] = soup.find_all("span", {"class": "user_id"})[0].text.strip()

        # print(g_data);
        lResult = [];
        for one_g_data in g_data:
            dOneRow = {};
            onerow_title = one_g_data.find_all('strong', attrs={"class": "tit_channel"});

            # text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."
            #
            # regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
            # matchobj = regex.search(text)


            # todo  15초는  타이틀을 안적어준다 해당의 경우 처리 해줘야한다
            # print(onerow_title)
            # print(len(onerow_title))
            if len(onerow_title) > 0:
                onerow_title = onerow_title[0].text.strip()
            else:
                ##todo  내용에서 첫줄 뽑아오는게 좋다
                # onerow_content ='';
                onerow_content = one_g_data.find_all('div', attrs={"class": "_content"})

                # print(onerow_content)

                # e ='';
                # br로 자르자 한번 필터해준뒤 br로 짜르자 br로 짜르자
                # >> > split_jusik = my_jusik.split(' ')
                # IndexError: list index out of range
                # 값이 없는게 있는듯?
                if len(onerow_content)> 0:
                    # 여기에서 엑셀에 들어갈수없는 값들은  다 지워줘야한다
                    #in _bind_value raise ValueError(Cannot convert {0!r} to Excel.format(value)) python
                    onerow_title = onerow_content[0].text.strip()[0:30]
                    # onerow_title = 'no title'
                else:
                    onerow_title = 'no title'
            onerow_reply = one_g_data.find_all('strong', attrs={"class": "_commentCount"})
            #날짜
            oneRowdate = one_g_data.find_all('a', attrs={"class": "_linkPost"})
            oneRowdate=oneRowdate[0].text.strip()
            onerow_reply = onerow_reply[0].text.strip()
            dOneRow['product_reg_date'] = oneRowdate;
            dOneRow['product_name'] = onerow_title;
            dOneRow['proudct_reply_count'] = len(onerow_reply) == 0 and '0' or onerow_reply;
            self.lResult.append(dOneRow)

        # print(self.lResult);
        # return  lResult;
            # return self.amp * np.sin(2 * np.pi * self.freq * time + self.startTime) + self.bias

    def craeat_excel(self):
        book = Workbook()
        sheet = book.active
        iResultIdx = 0;

        iTotalRow = len(self.lResult);
        # print(self.lResult);
        sumReply = 0;
        for oneObject in self.lResult:
            # row
            # print(oneObject);
            iResultIdx = iResultIdx + 1;
            for oneObjectIdx in oneObject:
                # sheet['A' + str(iResultIdx)] = 'DATE'
                if oneObjectIdx == 'product_reg_date':
                    sheet['A' + str(iResultIdx)] = oneObject[oneObjectIdx]
                elif oneObjectIdx == 'product_name':
                    sheet['B' + str(iResultIdx)] = oneObject[oneObjectIdx]
                elif oneObjectIdx == 'proudct_reply_count':
                    sheet['C' + str(iResultIdx)] = oneObject[oneObjectIdx]
                    sumReply = sumReply + int(oneObject[oneObjectIdx]);


        # print(self.dMainResult['channel_name']);
        sheet['A' + str(iResultIdx + 1)] = self.dMainResult['channel_name'];
        sheet['B' + str(iResultIdx + 1)] = '댓글평균'
        sheet['C' + str(iResultIdx + 1)] = str(math.ceil(sumReply / iTotalRow))

        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')
        nowTime = now.strftime('%H:%M:%S')
        book.save(self.dMainResult['channel_name'] + '_' + nowDate + '_' + nowTime + '.xlsx');
