# -*- coding: UTF-8 -*-
'''
@project:machineLearning-me
@author:wangfy
@time:2018/10/16 21:14
'''


from numpy import *
import ch2.kNN as kNN
import matplotlib

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

fig = plt.figure()
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
ax = fig.add_subplot(111)
#定义三个类别的空列表
type1_x = []
type1_y = []
type2_x = []
type2_y = []
type3_x = []
type3_y = []

#循环获得每个列表中的值
for i in range(len(datingLabels)):
    if datingLabels[i] == 1:  # 不喜欢
        type1_x.append(datingDataMat[i][0])
        type1_y.append(datingDataMat[i][1])

    if datingLabels[i] == 2:  # 魅力一般
        type2_x.append(datingDataMat[i][0])
        type2_y.append(datingDataMat[i][1])

    if datingLabels[i] == 3:  # 极具魅力
        type3_x.append(datingDataMat[i][0])
        type3_y.append(datingDataMat[i][1])

type1 = ax.scatter(type1_x, type1_y, s=20, c='red')
type2 = ax.scatter(type2_x, type2_y, s=40, c='green')
type3 = ax.scatter(type3_x, type3_y, s=50, c='blue')

type1 = ax.scatter(type1_x, type1_y, s=20, c='red')
type2 = ax.scatter(type2_x, type2_y, s=40, c='green')
type3 = ax.scatter(type3_x, type3_y, s=50, c='blue')
ax.legend((type1, type2, type3), (u'不喜欢', u'魅力一般', u'极具魅力'), loc=2)
#ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*array(datingLabels),15.0*array(datingLabels))

plt.xlabel(u'x  每年获取的飞行常客里程数')
plt.ylabel(u'y  玩视频游戏所耗时间半分比')
plt.show()

# from numpy import *
# import ch2.kNN as kNN
# import matplotlib
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
# datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
# # ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
# ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*array(datingLabels), 15.0*array(datingLabels))
# plt.xlabel('Percentage of Time Spent Playing Video Games')
# plt.ylabel('Liters of Ice Cream Consumed Per Week')
# plt.show()
