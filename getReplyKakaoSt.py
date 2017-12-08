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


class ksCrawling:
    def __init__(self, url,save_root_dir):
        self.dMainResult = {};
        self.lResult = [];
        self.save_root_dir = save_root_dir;
        # url -- 을 계속 적으로 넣어준다.
        self.driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver');
        self.d =self.driver;
        #url = https://story.kakao.com/ch/banzzak2017
        self.d.get(url);

        # 갑자기 왜 이게 안먹히는지  이유를 모르겠다 self.d.find_element_by_class_name html 구조가 바뀐건지 머로 막아놓은건지 정확한 이유 아직 모름
        # self.sChannel_name = self.d.find_element_by_class_name('_profileName');
        # self.sChannel_id = self.d.find_element_by_class_name('user_id').text;
        # self.dMainResult['channel_name'] = self.d.find_element_by_class_name('_profileName').text;




    def scrollDown(self ,checkIdex):

        idx = 0;
        #디폴트가  5번인데
        while True:
            aReturnRows = [];
            self.d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            # ++idx;
            idx = idx + 1;
            # if idx == 5:
            if idx == checkIdex:
                # print(idx);
                break
        # return np.arange(0.0, self.endTime, self.sampleTime)


    def get_set_CrawlingData(self):
        #html 이 뿌리기전에 아래가 돌아가서 문제
        time.sleep(7)
        soup = BeautifulSoup(self.d.page_source, "html.parser")

        # todo 구매링크
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


            # todo 예외 케이스가 좀 있을듯 ... 음 고여사 같은 경우 google 이아니라  snsform 이고 등등 몇가지케이스 있는듯 확인후 진행하자
            # 몇가지 형태 의 케이스가 있는경우 그 형태로 주소를 만들어주는식으로 하자
            # onerow_content = one_g_data.find_all('div', attrs={"class": "_content"})
            # print(onerow_content)
            # regex = re.compile(r'^(https?):\/\/goo.gl\/[A-Za-z0-9_\-]+')
            # paymentUrl = regex.search(onerow_content)
            # # # 뒤에 url 빼올수있다.
            # paymentUrl = paymentUrl[0].split('/')
            # print(paymentUrl[3])


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
                    if '+' in oneObject[oneObjectIdx]:
                        oneObject[oneObjectIdx] = oneObject[oneObjectIdx].replace("+", "");

                    sumReply = sumReply + int(oneObject[oneObjectIdx].replace(",", ""));

        # print(self.dMainResult['channel_name']);ㄴ
        sheet['A' + str(iResultIdx + 1)] = self.dMainResult['channel_name'];
        sheet['B' + str(iResultIdx + 1)] = '댓글평균'
        sheet['C' + str(iResultIdx + 1)] = str(math.ceil(sumReply / iTotalRow))

        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')
        nowTime = now.strftime('%H:%M:%S')
        path = self.save_root_dir + '_' + nowDate;
        #폴더에 생성
        if not os.path.isdir(self.save_root_dir+'_'+nowDate):
            os.mkdir(path);

        book.save(path+'/'+self.dMainResult['channel_name'] + '_' + nowDate + '_' + nowTime + '.xlsx');


