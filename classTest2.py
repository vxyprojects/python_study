import matplotlib.pyplot as plt
import classTest

# test1 = sinClass.sinWaveForm(amp = 1, endTime = 1)
# test1.plotWave()

test2 = classTest.sinWaveForm(amp = 1, freq=1, endTime = 5)
test3 = classTest.sinWaveForm(amp = 1, freq=4, endTime = 5)

time = test2.calcDomain()
resultTest2 = test2.calcSinValue(time)
resultTest3 = test3.calcSinValue(time)

plt.plot(time, resultTest2, time, resultTest3, time, resultTest2+resultTest3)
plt.grid(True)
plt.xlabel('time')
plt.ylabel
plt.show()
