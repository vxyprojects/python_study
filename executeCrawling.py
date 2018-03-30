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
#todo divide 제로  sumReply / iTotalRow 각각 변수 다 찍어보자 돌면서 글면 바로 알수있을것이다
urList = [
'https://story.kakao.com/ch/sinnanday',# 신난데이
'https://story.kakao.com/ch/womanface', #엠누리 - 베베팡쪽관련 업체
'https://story.kakao.com/ch/pretty2', #베베팡 테스트채널
'https://story.kakao.com/ch/madewomen',#베베팡 테스트채널
# 'https://story.kakao.com/ch/thgml3', #소희언니네
# 'https://story.kakao.com/ch/kitchen1', #키토 테스트 채널
# 'https://story.kakao.com/ch/super50',#베베팡
# 'https://story.kakao.com/ch/jbsang',#써니픽쪽 테스트
# 'https://story.kakao.com/ch/jubu123', #todo 예외사항이있다 .
# 'https://story.kakao.com/ch/todaysale21',
# 'https://story.kakao.com/ch/umjigong2',
# 'https://story.kakao.com/ch/bebeplay2',
# 'https://story.kakao.com/ch/chicebrown',
# 'https://story.kakao.com/ch/gosumanmul',
# 'https://story.kakao.com/ch/tokyosancheck',
# 'https://story.kakao.com/ch/kidsberry',
# 'https://story.kakao.com/ch/liveing09',#친한언니네
# 'https://story.kakao.com/ch/hot09',
# 'https://story.kakao.com/ch/smart_0369',
# 'https://story.kakao.com/ch/ggogga7', #광주업체
# 'https://story.kakao.com/ch/timesale24', #와우벤처스
# 'https://story.kakao.com/ch/tongknsale2', #여기 잘가르쳐줌
# 'https://story.kakao.com/ch/mombanchan',
# 'https://story.kakao.com/ch/jjansoonmom',#짠순이엄마
# 'https://story.kakao.com/ch/locoduck',#로코그룹
# # 디노맥스 -육아박사
# 'https://story.kakao.com/ch/petitc',
# # 육아공식 - 백운e21',
# # 디노맥스 -육아박사
# 'https://story.kakao.com/ch/petitc',
# # 육아공식 - 백운
# 'https://story.kakao.com/ch/babycare8',
# 'https://story.kakao.com/ch/babycare8',
# 'https://story.kakao.com/ch/babycare3', #todo 예외케이스
# 'https://story.kakao.com/ch/mssada',
# 'https://story.kakao.com/ch/babycare6',
#
# # 리얼커머스-다솔 - 쇼핑왕루이
#  'https://story.kakao.com/ch/kinglouis',
#
# 'https://story.kakao.com/ch/healingtravel7',
# # 헬로메이트
# 'https://story.kakao.com/ch/100jubu',
# # cocker1102
# 'https://story.kakao.com/ch/ssuujin',
# #귀빈정
# 'https://story.kakao.com/ch/wemother23',
# 'https://story.kakao.com/ch/mylovemother1',
# 'https://story.kakao.com/ch/wemother1',
# 'https://story.kakao.com/ch/mothersalrim',
# 'https://story.kakao.com/ch/motheryori',
# 'https://story.kakao.com/ch/motherchoice',#얘는 좀 다름
# 'https://story.kakao.com/ch/motherpyoyori',#위랑 같음
# #위드유
# 'https://story.kakao.com/ch/qstory',
# 'https://story.kakao.com/ch/yoyoplus',
# 'https://story.kakao.com/ch/btime',
# #민커뮤니티
# 'https://story.kakao.com/ch/ladies',
# 'https://story.kakao.com/ch/powermom7',#에벤에셀이 삼
# 'https://story.kakao.com/ch/sptalk',#두루모아가 삼
# #채널인
# 'https://story.kakao.com/ch/goldd2gt08',#올리벤더 가 현재 가지고있음
# #꿈꾸는 이웃
# 'https://story.kakao.com/ch/yozum',
# 'https://story.kakao.com/ch/wifecook',
# 'https://story.kakao.com/ch/buyisgood',
# 'https://story.kakao.com/ch/mommycooking',
# #맘스홈쇼핑
# 'https://story.kakao.com/ch/momlike',
# 'https://story.kakao.com/ch/today2121',
# #
# # #리슨코리아 #todo 팔만 할듯한디 댓글수를 보니깐
# 'https://story.kakao.com/ch/livingquin',
# # 'https://story.kakao.com/ch/superwomen',
# # 'https://story.kakao.com/ch/bravomylife79'
# #'https://story.kakao.com/ch/homeyunfood',
# # 'https://story.kakao.com/ch/pleasefood79'
# # #퍼스트앤티
# # 'https://story.kakao.com/ch/showjio',
# 'https://story.kakao.com/ch/qlalf3',
# #
# 'https://story.kakao.com/ch/yoonbebe',
# 'https://story.kakao.com/ch/bebecare1004',#todo 주목해야함
# 'https://story.kakao.com/ch/09store',#todo 주목해야함
# 'https://story.kakao.com/ch/open3685',
# 'https://story.kakao.com/ch/daebak8381',
# 'https://story.kakao.com/ch/dokaebi',
# 'https://story.kakao.com/ch/reallyagirl',#디노맥스
# ##'https://story.kakao.com/ch/decopang', #성분에디터 - 퀸즈 - 꾸미고팡 todo 예외케이스 인코딩문제
# 'https://story.kakao.com/ch/good3049',
# 'https://story.kakao.com/ch/ping2',#todo 구매링크까지 나오게 했을ㄸ 문제됨
# 'https://story.kakao.com/ch/5mins',
# 'https://story.kakao.com/ch/momsi',
# 'https://story.kakao.com/ch/nmnmfood',
# 'https://story.kakao.com/ch/receipeunique',
# 'https://story.kakao.com/ch/recipestore',
# 'https://story.kakao.com/ch/note123',

# 'https://story.kakao.com/ch/prideofsalim',#- 레몬트리
# ## 'https://story.kakao.com/ch/howtocook', ##todo 구매링크까지 나오게 했을ㄸ 문제됨    sumPayLink = sumPayLink + int(oneObject[oneObjectIdx].replace(",", ""));
# ### ValueError: invalid literal for int() with base 10: ''
# 'https://story.kakao.com/ch/shefsong',
# 'https://story.kakao.com/ch/lemonberbena',
# 'https://story.kakao.com/ch/luckybebe',
# 'https://story.kakao.com/ch/recipeman',
# 'https://story.kakao.com/ch/spsp',
# 'https://story.kakao.com/ch/cocojuny',
# 'https://story.kakao.com/ch/btbox',
# 'https://story.kakao.com/ch/beauty_story',
# 'https://story.kakao.com/ch/momn',
# 'https://story.kakao.com/ch/hubbytable',
# 'https://story.kakao.com/ch/bongmom',
# 'https://story.kakao.com/ch/coco77777',
# 'https://story.kakao.com/ch/limstory1',
# 'https://story.kakao.com/ch/cocker1102',
# 'https://story.kakao.com/ch/tongtong777',
# 'https://story.kakao.com/ch/longkid',
# 'https://story.kakao.com/ch/salebysale',#티엔고우코리아
# 'https://story.kakao.com/ch/goldenbaby',
# 'https://story.kakao.com/ch/15diet',
# 'https://story.kakao.com/ch/diethunter',
# 'https://story.kakao.com/ch/sky01',
# 'https://story.kakao.com/ch/ergolovers',
# 'https://story.kakao.com/ch/mom79',
# 'https://story.kakao.com/ch/missy5drey',
# 'https://story.kakao.com/ch/namom',
# 'https://story.kakao.com/ch/ilike1',
# 'https://story.kakao.com/ch/lovejw',
# 'https://story.kakao.com/ch/revedebebe',
# 'https://story.kakao.com/ch/sister7',
# 'https://story.kakao.com/ch/banzzak2017',
# 'https://story.kakao.com/ch/tomato',
# 'https://story.kakao.com/ch/koyalunch',
# 'https://story.kakao.com/ch/09ssadagu',
# 'https://story.kakao.com/ch/dadoogmom',
# 'https://story.kakao.com/ch/moms1',
# 'https://story.kakao.com/ch/goldd2gt10',
# 'https://story.kakao.com/ch/cookiej',
# 'https://story.kakao.com/ch/edutrend',
# 'https://story.kakao.com/ch/0u82',
# 'https://story.kakao.com/ch/nextfox1234',
# 'https://story.kakao.com/ch/5baby',
# 'https://story.kakao.com/ch/supermoney',
# 'https://story.kakao.com/ch/baby_10',
# 'https://story.kakao.com/ch/babyhotdeal',
# 'https://story.kakao.com/ch/kidssister',
# 'https://story.kakao.com/ch/baby_commerce',#앱커머스
# 'https://story.kakao.com/ch/minimini',
# 'https://story.kakao.com/ch/kidsstore',
# 'https://story.kakao.com/ch/nextfox5',
# 'https://story.kakao.com/ch/masterbaby',
# 'https://story.kakao.com/ch/living-talk',
# 'https://story.kakao.com/ch/yori1004',#엄마손
# 'https://story.kakao.com/ch/firstsalrim',#꿈꾸는이웃
# 'https://story.kakao.com/ch/homeworker',#그녀의살림창고
# 'https://story.kakao.com/ch/babykids',#엄마의일기
# 'https://story.kakao.com/ch/ssadagu09',#싸다구홈쇼핑
# 'https://story.kakao.com/ch/ggokkasazukka',#제이앤제이컴퍼니
# 'https://story.kakao.com/ch/myhomediy',#꿈꾸는이웃
# 'https://story.kakao.com/ch/angelstory',
# 'https://story.kakao.com/ch/nextfox1',
# 'https://story.kakao.com/ch/daebakgoodday',
# 'https://story.kakao.com/ch/housekeeper',#케이엘비전
# 'https://story.kakao.com/ch/chungdamgirl'#네이처톡
];
save_root_dirname = '/Users/swlee/Documents/python/example/ks'
payLinkModeOn = 'T'; # T OR F
# payLinkModeOn = 'F'; # T OR F
# save_root_dirname = '/Users/swlee/Documents/python/example/fb'
for oneList in urList:
    instance = getReplyKakaoSt.ksCrawling(oneList,save_root_dirname,payLinkModeOn)
    # instance = getReplyKakaoSt.ksCrawling(oneList,save_root_dirname)
    #default를 5만큼 스크롤 다운으로 처리
    # instance.scrollDown(120);# 대략 5월달까지 나옴
    # instance.scrollDown(280);
    # instance.scrollDown(5);
    # instance.scrollDown(4);
    instance.scrollDown(2);
    # instance.scrollDown(3);

    instance.get_set_CrawlingData();
    instance.craeat_excel();



# if not os.path.isdir(dirname):
#     os.mkdir(dirname);



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
