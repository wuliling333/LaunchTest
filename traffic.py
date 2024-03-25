"""
adb devices 连接手机
查询正在打开的应用的包名
adb shell dumpsys window | grep mCurrentFocus
获取包名的PID
adb shell ps | grep com.wepie.gudu
查询PID下的流量消耗
adb shell cat /proc/“pid"/net/dev
"""

import csv
import os
import time

# 控制类
class Controller(object):
    def __init__(self, count):
        self.count = count
        self.alldata = [('timestamp', 'traffic')]

    # 单次测试过程
    def testprocess(self):
         # 获取PID
         res=os.popen('adb shell ps | grep com.wepie.gudu')
         # 对取到的数据进行切片出处理获取PID
         pid=res.readlines()[0].split('      ')[1].split('  ')[0]

         print(pid)
         # 查看流量
         traffic=os.popen('adb shell cat /proc/' + pid + '/net/dev')
         # 从traffic中遍历
         for line in traffic:
            #  找到有"wlan"的行数
            if 'wlan0' in line:
                # '#'.join(...): 在这一步中，'#' 是一个字符串，它作为分隔符，
                # 将之前拆分的单词列表重新连接起来。join() 方法会以 '#' 作为分隔符，将单词列表中的元素连接成一个新的字符串
                line = '#'.join(line.split())
                recv = line.split('#')[1]
                transmit = line.split('#')[9]
                #计算所以流量的和
                alltrffic = int(recv) + int(transmit)
                alltrffic = str(alltrffic/1024)+'k'

                curenttime = self.getCurentTime()

                self.alldata.append((curenttime, alltrffic))

    # 多次执行测试过程
    def run(self):
        while self.count > 0:
            self.testprocess()
            self.count = self.count - 1
            time.sleep(60)

    # 获取当前的时间戳
    def getCurentTime(self):
        curentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        return curentTime

    # 数据的存储
    def SaveDataToCSV(self):
        file_path='/Users/rourou/Documents/traffic.csv'
        with open(file_path, 'w', newline='') as csvfile:
            # 创建初始化写入对象
            writer = csv.writer(csvfile)
            # 写入数值
            writer.writerows(self.alldata)
            csvfile.close()

if __name__ == '__main__':
    controller = Controller(180)
    controller.run()
    controller.SaveDataToCSV()
