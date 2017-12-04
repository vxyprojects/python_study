import matplotlib.pyplot as plt
import getReplyKakaoSt
import re
import os;

# test1 = sinClass.sinWaveForm(amp = 1, endTime = 1)
# test1.plotWave()

#url 돌면서  인스탄스  계속 생성 하면서  처리 해준다
url = 'https://story.kakao.com/ch/banzzak2017'
url2 = 'https://story.kakao.com/ch/sister7'

# 고여사는 아래와 같은 스타일
# rnakfur.snsform.co.kr
#d
#todo 이상하네 12시에 안돌아가던게 지금은 다돌아가네?  이유를 모르겠음 낼도 12시정도에 돌려보자  안되는지
urList = [

#귀빈정
'https://story.kakao.com/ch/wemother23',
# 'https://story.kakao.com/ch/mylovemother1',
# 'https://story.kakao.com/ch/wemother1'
# 'https://story.kakao.com/ch/mothersalrim',
# 'https://story.kakao.com/ch/motheryori',
#'https://story.kakao.com/ch/motherchoice',#얘는 좀 다름
'https://story.kakao.com/ch/motherpyoyori',#위랑 같음
#위드유
'https://story.kakao.com/ch/qstory',
'https://story.kakao.com/ch/yoyoplus',
'https://story.kakao.com/ch/btime',
#민커뮤니티
'https://story.kakao.com/ch/recipeman'
'https://story.kakao.com/ch/ladies'
'https://story.kakao.com/ch/powermom7',#에벤에셀이 삼
'https://story.kakao.com/ch/sptalk',#두루모아가 삼
#채널인
'https://story.kakao.com/ch/goldd2gt08/profile',#올리벤더 가 현재 가지고있음
#꿈꾸는 이웃
'https://story.kakao.com/ch/yozum',
'https://story.kakao.com/ch/wifecook',
'https://story.kakao.com/ch/buyisgood',
'https://story.kakao.com/ch/mommycooking',
#맘스홈쇼핑
'https://story.kakao.com/ch/momlike',
'https://story.kakao.com/ch/today2121',

#리슨코리아 #todo 팔만 할듯한디 댓글수를 보니깐
'https://story.kakao.com/ch/livingquin',
# 'https://story.kakao.com/ch/superwomen',
# 'https://story.kakao.com/ch/bravomylife79'
#'https://story.kakao.com/ch/homeyunfood',
# 'https://story.kakao.com/ch/pleasefood79'
#퍼스트앤티
'https://story.kakao.com/ch/showjio',
'https://story.kakao.com/ch/qlalf3',

'https://story.kakao.com/ch/yoonbebe',
'https://story.kakao.com/ch/bebecare1004',#todo 주목해야함
'https://story.kakao.com/ch/09store',#todo 주목해야함
'https://story.kakao.com/ch/open3685',
'https://story.kakao.com/ch/daebak8381',
'https://story.kakao.com/ch/dokaebi',
'https://story.kakao.com/ch/reallyagirl',#디노맥스
'https://story.kakao.com/ch/decopang',
'https://story.kakao.com/ch/good3049',
'https://story.kakao.com/ch/ping2',
'https://story.kakao.com/ch/5mins',
'https://story.kakao.com/ch/momsi',
'https://story.kakao.com/ch/nmnmfood',
'https://story.kakao.com/ch/receipeunique',
'https://story.kakao.com/ch/recipestore',
'https://story.kakao.com/ch/note123',
'https://story.kakao.com/ch/prideofsalim',#- 레몬트리
'https://story.kakao.com/ch/howtocook',#todo 예외케이스 있는듯 - 레몬트리
'https://story.kakao.com/ch/shefsong',#todo 예외케이스 있는듯
'https://story.kakao.com/ch/lemonberbena',
'https://story.kakao.com/ch/mssada',
'https://story.kakao.com/ch/recipeman',
'https://story.kakao.com/ch/spsp',
'https://story.kakao.com/ch/cocojuny',
'https://story.kakao.com/ch/btbox',
'https://story.kakao.com/ch/beauty_story',
'https://story.kakao.com/ch/momn',
'https://story.kakao.com/ch/hubbytable',
'https://story.kakao.com/ch/wifecook',
'https://story.kakao.com/ch/tongtong777',
'https://story.kakao.com/ch/babycare8',
'https://story.kakao.com/ch/bongmom',
'https://story.kakao.com/ch/babycare8',#todo 왜 여기서 또뜨지?
'https://story.kakao.com/ch/coco77777',
'https://story.kakao.com/ch/limstory1',
'https://story.kakao.com/ch/cocker1102',
'https://story.kakao.com/ch/tongtong777',
'https://story.kakao.com/ch/100jubu', # ZeroDivisionError: division by zero 처리 필요
'https://story.kakao.com/ch/longkid',
'https://story.kakao.com/ch/0u82',
'https://story.kakao.com/ch/goldenbaby',# ZeroDivisionError: division by zero 처리 필요
'https://story.kakao.com/ch/15diet',
'https://story.kakao.com/ch/diethunter',# 여기서 에러 한번 났었음
'https://story.kakao.com/ch/kinglouis',
'https://story.kakao.com/ch/sky01',
'https://story.kakao.com/ch/ergolovers',
'https://story.kakao.com/ch/mom79',
'https://story.kakao.com/ch/ilike1',
'https://story.kakao.com/ch/lovejw', # 혼자 돌려도 문제
'https://story.kakao.com/ch/revedebebe',
'https://story.kakao.com/ch/sister7',
'https://story.kakao.com/ch/banzzak2017',
'https://story.kakao.com/ch/tomato',
'https://story.kakao.com/ch/koyalunch',
'https://story.kakao.com/ch/09ssadagu',#todo 안돌아감
'https://story.kakao.com/ch/dadoogmom',
'https://story.kakao.com/ch/moms1',
'https://story.kakao.com/ch/goldd2gt10',#todo 안돌아감
'https://story.kakao.com/ch/cookiej',
'https://story.kakao.com/ch/edutrend',
'https://story.kakao.com/ch/0u82',
'https://story.kakao.com/ch/5baby'
# 'https://story.kakao.com/ch/tongtong777' # 예외케이스있는듯 - 육아달인
## 'https://story.kakao.com/ch/15diet', # 여기 예외케이스 있는듯
];

# for oneList in urList:
#     instance = getReplyKakaoSt.ksCrawling(oneList)
#     #default를 5만큼 스크롤 다운으로 처리
#     # instance.scrollDown(120);# 대략 5월달까지 나옴
#     # instance.scrollDown(280);
#     instance.scrollDown(5);
#     instance.get_set_CrawlingData();
#     instance.craeat_excel();


#todo test
#todo 폴더를 만들어주고 넣어주는식 일단 폴더 만들어주는식으로 해야겠다  sns명_날짜 이런식으로
#todo 카스관리자명_날짜 이런식으로 나오게끔
# dirname = '/user/aaa'
# os.mkdir('/user/1');
# print(os.path.isdir('/사용자/swlee'));
# if not os.path.isdir('/user/aaa'):



# instance = getReplyKakaoSt.ksCrawling(url)
# instance.scrollDown();
# instance.get_set_CrawlingData();
# instance.craeat_excel();
#
#
# instance2 = getReplyKakaoSt.ksCrawling(url2)
# instance2.scrollDown();
# instance2.get_set_CrawlingData();
# instance2.craeat_excel();


# test2 = classTest.sinWaveForm(amp = 1, freq=1, endTime = 5)
# test3 = classTest.sinWaveForm(amp = 1, freq=4, endTime = 5)

# time = test2.calcDomain()
# resultTest2 = test2.calcSinValue(time)
# resultTest3 = test3.calcSinValue(time)
#
# plt.plot(time, resultTest2, time, resultTest3, time, resultTest2+resultTest3)
# plt.grid(True)
# plt.xlabel('time')
# plt.ylabel
# plt.show()

#
# text1 = "https://goo.gl/YuL4cF"
#
# regex = re.compile(r'^(https?):\/\/goo.gl\/[A-Za-z0-9_\-]+')
# paymentUrl = regex.search(text1)
#
#
# #뒤에 url 빼올수있다.
# paymentUrl = paymentUrl[0].split('/')
# print(paymentUrl[3])
