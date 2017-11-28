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


class fbCrawling:
    def __init__(self, url):
        self.dMainResult = {};
        self.lResult = [];
        self.aExcelResult = [];
        # url -- 을 계속 적으로 넣어준다.
        self.driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver');
        self.d =self.driver;
        #url = https://story.kakao.com/ch/banzzak2017
        self.d.get(url);
        self.baseUrl= 'https://m.facebook.com/';
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
        soup = BeautifulSoup(self.d.page_source, "html.parser")
        # print('len(soup)')
        # print(len(soup))
        # print(soup.find_all("span", {"class": "_33vv"})[0].text)
        # print(len(soup.find_all("span", {"class": "_33vv"})[0].text))
        # print(len(soup.find_all("span", {"class": "_33vv"})[0].text))
        # print('len(soup.find_all("span", {"class": "_33vv"})[0].text')
        # print(soup.find_all("span", {"class": "_33vv"})[0].text.strip())

        self.dMainResult['page_name'] = soup.find_all("span", {"class": "_33vv"})[0].text.strip()


        # print('len(self.dMainResult["page_name"])')
        # print(len(self.dMainResult['page_name'] ))
        # print('len(self.dMainResult)')
        # print(len(self.dMainResult))


        g_data = soup.find_all("div", {"class": "userContentWrapper"})

        # 엑셀을 만들기위한 전체 배열

        for one_g_data in g_data:
            dOneRow = {};
            # 날짜
            onerow_date = one_g_data.find_all('span', attrs={"class": "timestampContent"});
            onerow_date = onerow_date[0].text.strip()

            # 링크
            onerow_share_count = one_g_data.find_all('a', attrs={"class": "UFIShareLink"});

            if one_g_data.find_all('a', attrs={"class": "_5pcq"}) is not None:
                videourl =one_g_data.find_all('a', attrs={"class": "_5pcq"})
                makeVideourl = self.baseUrl+videourl[0]['href'];
                dOneRow['video_src'] = makeVideourl;
            else:
                makeVideourl = 'null';
                dOneRow['video_src'] = makeVideourl;


            # a_5pcq
            # video div
            # if one_g_data.find_all('a', attrs={"class": "_5pcq"}) is not None:
            #     onerow_video = one_g_data.find_all('a', attrs={"class": "_5pcq"})['src'];
            #     # onerow_video = one_g_data.find('video')['src'];
            #     # onerow_video = onerow_video.replace("blob:", "");
            #     # onerow_video = onerow_video.replace("www.", "m.");
            #     # dOneRow['video_src'] = onerow_video;
            #     print('onerow_video')
            #     print(onerow_video)

            if len(onerow_share_count) > 0:
                onerow_share_count = onerow_share_count[0].text.strip()
            else:
                onerow_share_count = '0';

            # 계시글 내용
            user_content = one_g_data.find('div', attrs={"class": "userContent"});
            if user_content is not None and len(user_content) is not 0:
                user_content = user_content.findChildren();
                user_content = user_content[0].text.strip()
            else:
                user_content = 'not content';

            # 좋아요
            onerow_like_count = one_g_data.find('div', attrs={"class": "UFILikeSentenceText"});
            if onerow_like_count is not None and len(onerow_like_count) is not 0:
                onerow_like_count = onerow_like_count.findChildren();
                onerow_like_count = onerow_like_count[0].text.strip();
            else:
                onerow_like_count = '0';
            # todo 숫자만 뽑아서 평균치 뽑아낸다 .
            dOneRow['content_date'] = onerow_date;
            dOneRow['content'] = user_content;

            # dOneRow['video_src'] = user_content;
            #김정문님이 좋아합니다 이렇게 나오는케이스 가있다
            # 좋아요 수
            if onerow_like_count is not None and onerow_like_count is not '0':
                # 0-9
                regex = re.compile(r'[0-9,]+명이')
                regexLike = regex.search(onerow_like_count)
                if regexLike is not None :
                    regexLike = regexLike[0].replace("명이", "");
                else:
                    regexLike ='3';

                    # regexLike = int(regexLike.replace(",", ""));
            else:
                regexLike = '0';

            dOneRow['content_like_count'] = regexLike;

            # 공유 숫자
            if onerow_share_count is not '0' and onerow_share_count is not None:
                onerow_share_count = onerow_share_count.split(' ')[1].replace("회", "")
                # onerow_share_count = int(onerow_share_count.replace(",", ""));
            else:
                onerow_share_count = '0';

            dOneRow['content_share_count'] = onerow_share_count;
            self.aExcelResult.append(dOneRow);

        # print(self.lResult);
        # return  lResult;
            # return self.amp * np.sin(2 * np.pi * self.freq * time + self.startTime) + self.bias

    def craeat_excel(self):
        iTotalRow = len(self.aExcelResult);
        book = Workbook()
        sheet = book.active
        iResultIdx = 0;
        sum_content_share_count = 0;
        sum_content_like_count = 0;

        for oneObject in self.aExcelResult:
            iResultIdx = iResultIdx + 1;
            for oneObjectIdx in oneObject:
                if oneObjectIdx == 'content_date':
                    sheet['A' + str(iResultIdx)] = oneObject[oneObjectIdx]
                elif oneObjectIdx == 'content':
                    sheet['B' + str(iResultIdx)] = oneObject[oneObjectIdx]
                elif oneObjectIdx == 'content_like_count':
                    sheet['C' + str(iResultIdx)] = oneObject[oneObjectIdx]
                    sum_content_like_count = sum_content_like_count + int(oneObject[oneObjectIdx].replace(",", ""));
                elif oneObjectIdx == 'content_share_count':
                    sheet['D' + str(iResultIdx)] = oneObject[oneObjectIdx]
                    sum_content_share_count = sum_content_share_count + int(oneObject[oneObjectIdx].replace(",", ""));
                elif oneObjectIdx == 'video_src':
                    sheet['E' + str(iResultIdx)] = oneObject[oneObjectIdx]

        sheet['A' + str(iResultIdx + 1)] = self.dMainResult['page_name'];
        sheet['B' + str(iResultIdx + 1)] = '좋아요 평균'
        sheet['C' + str(iResultIdx + 1)] = str(math.ceil(sum_content_like_count / iTotalRow))
        sheet['D' + str(iResultIdx + 1)] = '공유하기 평균'
        sheet['E' + str(iResultIdx + 1)] = str(math.ceil(sum_content_share_count / iTotalRow))

        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')
        nowTime = now.strftime('%H:%M:%S')
        book.save(self.dMainResult['page_name'] + '_' + nowDate + '_' + nowTime + '.xlsx');
