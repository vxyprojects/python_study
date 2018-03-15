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
import chardet



class ksCrawling:
    def __init__(self, url,save_root_dir,payLinkOn):
        self.dMainResult = {};
        self.lResult = [];
        self.save_root_dir = save_root_dir;
        # url -- 을 계속 적으로 넣어준다.
        self.driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver');
        self.d =self.driver;
        #구매링크모드키냐안키냐
        self.payLinkOn = payLinkOn;
        self.d.get(url);
        self.google_short_url_base = 'https://goo.gl/#analytics/goo.gl/';
        # 갑자기 왜 이게 안먹히는지  이유를 모르겠다 self.d.find_element_by_class_name html 구조가 바뀐건지 머로 막아놓은건지 정확한 이유 아직 모름
        # self.sChannel_name = self.d.find_element_by_class_name('_profileName');
        # self.sChannel_id = self.d.find_element_by_class_name('user_id').text;
        # self.dMainResult['channel_name'] = self.d.find_element_by_class_name('_profileName').text;




    def scrollDown(self ,checkIdex):

        idx = 0;
        # 디폴트가  5번인데
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


    def get_set_CrawlingData(self):
        #html 이 뿌리기전에 아래가 돌아가서 문제
        # time.sleep(3)
        time.sleep(5)
        soup = BeautifulSoup(self.d.page_source, "html.parser")

        g_data = soup.find_all("div", {"class": "_activityBody "})
        self.dMainResult['channel_name'] = soup.find_all("span", {"class": "_profileName"})[0].text.strip()
        self.dMainResult['channel_id'] = soup.find_all("span", {"class": "user_id"})[0].text.strip()

        # print(g_data);
        lResult = [];
        for one_g_data in g_data:
            dOneRow = {};
            onerow_title = one_g_data.find_all('strong', attrs={"class": "tit_channel"});


            # todo 예외 케이스가 좀 있을듯 ... 음 고여사 같은 경우 google 이아니라  snsform 이고 등등 몇가지케이스 있는듯 확인후 진행하자
            # todo 얘외케이스  http://bit.ly/2lbXmsB  육아공식
            # 몇가지 형태 의 케이스가 있는경우 그 형태로 주소를 만들어주는식으로 하자
            onerow_content = one_g_data.find_all('div', attrs={"class": "_content"})

            if self.payLinkOn is 'T':
                #구매링크 작업
                payLinkCount = ''
                #원래는 100으로함
                # if onerow_content[0].text.strip()[0:300].find('goo.gl') is not -1:
                if onerow_content[0].text.strip()[0:700].find('goo.gl') is not -1:
                    #todo https:// 가 있는케이스
                    #todo    없는 케이스
                    #regex = re.compile(r'^(https?):\/\/goo.gl\/[A-Za-z0-9_\-]+')
                    # regex = re.compile(r'^(https?:\/\/)goo.gl\/[A-Za-z0-9_\-]+$')
                    # regex = re.compile(r'^(https?:\/\/)goo.gl\/[A-Za-z0-9_\-]+')
                    # regex = re.compile(r'^(https?):\/\/goo.gl\/([A-Za-z0-9_\-]+)')
                    # regex = re.compile(r'^https?:\/\/goo\.gl\/\w{6,}$')
                    # regex = re.compile(r'(https?:\/\/)goo.gl\/[A-Za-z0-9_\-]+')  # 먹히네
                    # regex = re.compile(r'https?:\/\/goo\.gl\/\w{6,}')
                    regex = re.compile(r'goo.gl\/[A-Za-z0-9_\-]+')  # 먹히네
                    # payment_url = regex.search(onerow_content[0].text.strip()[0:250])
                    payment_url = regex.search(onerow_content[0].text.strip()[0:700])
                    # print(payment_url);
                    if payment_url is not None:
                        payment_url=payment_url[0].replace("https", "")
                        payment_url=payment_url.replace("http", "")
                        # payment_url = payment_url[0].split('/')
                        payment_url = payment_url.split('/')
                        payment_url = payment_url[1];
                    #todo 붙어서 나오는케이스  뒷부분에서 http 나 goo 가있는케이스들은 지워주면?
                    # if payment_url.find('goo') is not -1:
                    #     payment_url= .replace("http", "")
                    # payment_url.find('htt')
                    # print(payment_url)
                        make_short_url=self.google_short_url_base + payment_url +'/all_time';
                        self.e = webdriver.Chrome('/Users/swlee/Downloads/chromedriver');
                        self.e.get(make_short_url)
                        time.sleep(2);
                        paymentPage = BeautifulSoup(self.e.page_source, "html.parser")
                        payLinkCount = paymentPage.find_all('div', attrs={"class": "count"})
                    if len(payLinkCount) >0 :
                        payLinkCount = payLinkCount[0].text.strip()
                    else :
                        payLinkCount = 'notaccurate';
                else :
                    payLinkCount = 'none';

                # print(payLinkCount)
                dOneRow['payment_count'] = payLinkCount;


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

            #todo 인코딩 확인 해야하는 부분
            # encoding = chardet.detect(dOneRow['product_name'])
            # # print(encoding);
            # print(encoding['encoding'])
            #
            # # if isinstance(dOneRow['product_name'], str):
            # #     print ("ordinary string")
            # # elif isinstance(dOneRow['product_name'], ):
            # #     print
            # #     "unicode string"
            # # else:
            # #     print
            # #     "not a string"
            #todo 꾸미고팡 땜에 추가한것
            dOneRow['product_name'] = dOneRow['product_name'].replace("[얇은 종아리를 위한 종아리 붓기 빼는 스트레칭] ", "")
            dOneRow['proudct_reply_count'] = len(onerow_reply) == 0 and '0' or onerow_reply;
            # print(dOneRow);
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
        sumPayLink = 0;
        sumpayLinkNoneCaseIndexCheck = 0;
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

                #구매링크부분 작업
                elif oneObjectIdx == 'payment_count':
                    sheet['E' + str(iResultIdx)] = oneObject[oneObjectIdx]
                    #todo oneObject[oneObjectIdx] is 'notaccurate' 한글로 정해놓으면 false 떨어짐
                    # sumpayLinkNoneCaseIndexCheck
                    if oneObject[oneObjectIdx] is 'none' or oneObject[oneObjectIdx] is 'notaccurate':
                        sumpayLinkNoneCaseIndexCheck = sumpayLinkNoneCaseIndexCheck + 1;
                    else:
                        sumPayLink = sumPayLink + int(oneObject[oneObjectIdx].replace(",", ""));


        sheet['A' + str(iResultIdx + 1)] = self.dMainResult['channel_name'];
        sheet['B' + str(iResultIdx + 1)] = '댓글평균'
        sheet['C' + str(iResultIdx + 1)] = str(math.ceil(sumReply / iTotalRow))
        #구매링크부분 작업
        if self.payLinkOn is 'T':

            if sumPayLink >0 :
                sheet['E' + str(iResultIdx + 1)] = str(math.ceil(sumPayLink/ iTotalRow-sumpayLinkNoneCaseIndexCheck))
            else :
                sheet['E' + str(iResultIdx + 1)] = 'none';

        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')
        nowTime = now.strftime('%H:%M:%S')
        path = self.save_root_dir + '_' + nowDate;
        #폴더에 생성
        if not os.path.isdir(self.save_root_dir+'_'+nowDate):
            os.mkdir(path);

        book.save(path+'/'+self.dMainResult['channel_name'] + '_' + nowDate + '_' + nowTime + '.xlsx');


