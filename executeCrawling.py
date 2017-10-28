import matplotlib.pyplot as plt
import getReplyKakaoSt

# test1 = sinClass.sinWaveForm(amp = 1, endTime = 1)
# test1.plotWave()

#url 돌면서  인스탄스  계속 생성 하면서  처리 해준다
url = 'https://story.kakao.com/ch/banzzak2017'
url2 = 'https://story.kakao.com/ch/sister7'

urList = [
'https://story.kakao.com/ch/banzzak2017',
'https://story.kakao.com/ch/sister7',
# 'https://story.kakao.com/ch/15diet', # 여기 예외케이스 있는듯
'https://story.kakao.com/ch/tomato',
'https://story.kakao.com/ch/koyalunch',
'https://story.kakao.com/ch/lovejw',
'https://story.kakao.com/ch/goldenbaby',
'https://story.kakao.com/ch/09ssadagu',
'https://story.kakao.com/ch/dadoogmom',
'https://story.kakao.com/ch/moms1',
'https://story.kakao.com/ch/goldd2gt10',
'https://story.kakao.com/ch/cookiej',
'https://story.kakao.com/ch/edutrend',
'https://story.kakao.com/ch/0u82'
];

for oneList in urList:
    # print(oneList);
    instance = getReplyKakaoSt.ksCrawling(oneList)
    instance.scrollDown();
    instance.get_set_CrawlingData();
    instance.craeat_excel();


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