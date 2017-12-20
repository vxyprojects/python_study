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

class fbCrawling:
    def __init__(self, url,save_root_dir):
        self.dMainResult = {};
        self.lResult = [];
        self.aExcelResult = [];
        self.save_root_dir = save_root_dir;
        #alert issue
        options = Options()
        options.add_argument("--disable-notifications")
        # self.driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver');
        self.driver = webdriver.Chrome('/Users/swlee/Downloads/chromedriver',chrome_options=options);
        self.d =self.driver;
        self.movie_url=''
        # 로그인을 하니깐 다운로드가 안되네  바꿈
        self.d.get(url);
        # self.d.get('https://facebook.com/');
        self.baseUrl= 'https://m.facebook.com/';



    def login(self,id,pssword,url):
        # 사용자 ID
        username = self.d.find_element_by_id('email')
        username.send_keys(id)
        # 사용자 PASSWORD
        password = self.d.find_element_by_id('pass')
        password.send_keys(pssword)
        # 'loginForm' element id # submit
        form = self.d.find_element_by_id('login_form')
        form.submit()
        time.sleep(2);
        # time.sleep(3);
        #get back
        self.d.get(url);
        # actions = ActionChains(self.d)
        # actions.send_keys(Keys.ESCAPE).perform();


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
        self.dMainResult['page_name'] = soup.find_all("span", {"class": "_33vv"})[0].text.strip()
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
                contain = -1;
                count_check = 0;

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

                    # if int(oneObject[oneObjectIdx].replace(",", "")) > 0:
                    if int(oneObject[oneObjectIdx].replace(",", "")) > -1:
                        count_check = int(oneObject[oneObjectIdx].replace(",", ""));
                elif oneObjectIdx == 'video_src':
                    sheet['E' + str(iResultIdx)] = oneObject[oneObjectIdx]
                    # print(oneObject[oneObjectIdx].find('videos'))
                    if oneObject[oneObjectIdx].find('videos') is not -1 :
                        self.movie_url = oneObject[oneObjectIdx];
                        # print(self.movie_url)
                        contain = oneObject[oneObjectIdx].find('videos');

                #moviecase and want checkcount
                # if contain is not -1 and count_check > 0:
                if contain is not -1 and count_check > -1:
                    # a=0;
                    # print('aaaaaaaaa')
                    # 해당 케이스인경우는 페이지 만들어서 다운로드
                    #todo 왜 클릭이 되는지 모르겠음 예전 예제 보면서 차이 알아내야함
                    fbCrawling.get_auto_movie(self)

        sheet['A' + str(iResultIdx + 1)] = self.dMainResult['page_name'];
        sheet['B' + str(iResultIdx + 1)] = '좋아요 평균'
        sheet['C' + str(iResultIdx + 1)] = str(math.ceil(sum_content_like_count / iTotalRow))
        sheet['D' + str(iResultIdx + 1)] = '공유하기 평균'
        sheet['E' + str(iResultIdx + 1)] = str(math.ceil(sum_content_share_count / iTotalRow))

        now = datetime.datetime.now()
        nowDate = now.strftime('%Y-%m-%d')
        nowTime = now.strftime('%H:%M:%S')
        path = self.save_root_dir + '_' + nowDate;
        # 폴더에 생성
        if not os.path.isdir(self.save_root_dir + '_' + nowDate):
            os.mkdir(path);
        book.save(path+'/'+self.dMainResult['page_name'] + '_' + nowDate + '_' + nowTime + '.xlsx');

    def get_auto_movie(self):

        print(self.movie_url);
        #로그인을 하니깐 다운로드가 안되네
        self.d.get(self.movie_url);
        # self.d.get('https://m.facebook.com//goeatnow/videos/1761097247520508/');
        #rending time
        time.sleep(4);
        soup = BeautifulSoup(self.d.page_source, "html.parser")
        srcclass = soup.find('div', attrs={"class": "_53mw _4gbu"});
        src=srcclass['data-store']
        # https:\/\/video-icn1-1.xx.fbcdn.net\/v\/t42.1790-2\/23572497_1770510766582506_10659924145078272_n.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6InN2ZV9zZCJ9&oh=d0699ba05a8518317f2b03c72ad934fc&oe=5A374A23
        start_string = '"src":';
        end_string = '"width":';
        start_point = src.find(start_string)
        end_point = src.find(end_string)
        #
        src_url = src[start_point+len(start_string):end_point-1]
        src_url = src_url.replace('"', "")
        src_url = src_url.replace("\\", "")
        print(src_url)
        new_html = '<a id="a_down" class="a_down" download="" href="'+src_url+'">다운</a>'
        self.d.execute_script("""
        var new_html= arguments[0];
        var new_elem = document.createElement('div');
        new_elem.innerHTML += ' ' + new_html;
        document.querySelector('body').appendChild(new_elem);
        """, new_html)
        time.sleep(10)
        # print(self.d.find_element_by_class_name('a_down'));
        # print(self.d.find_element_by_class_name('a_down').text);
        # .text
        self.d.find_element_by_class_name('a_down').click()