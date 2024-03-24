import csv
import os
import time
import string
import file


# 控制类
class Controller(object):
    def __int__(self, count):
        self.count = count
        self.alldata = [('timestamp', 'traffic')]

    # 单次测试过程
    def testprocess(self):
            # 获取PID
         res=os.popen('adb shell ps | findstr com.gudu')
         pid=res.readlines()[0].split('    ')[1].split('  ')[0]
         print(pid)
            # 查看流量
         traffic=os.popen('adb shell cat/proc/',+pid+'/net/dev')
         for i in traffic:
            if 'eth0' in line:
                line = '#'.join(line.split())
                recv = line.split('#')[1]
                transmit = line.split('#')[9]
                    #计算所以流量的和
                alltrffic = string.atoi(recv)+string.atoi(transmit)
                alltrffic = str(alltrffic/1024)+'k'

                curenttime = self.getCurentTime()

                self.alldata.append((curenttime, alltrffic))

    # 多次执行测试过程
    def run(self):
        while self.count > 0:
            self.testprocess()
            self.count = self.count - 1
            time.sleep(3)

    # 获取当前的时间戳
    def getCurentTime(self):
        curentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        return curentTime

    # 数据的存储
    def SaveDataToCSV(self):
        csvfile = file('D:/traffic.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
    controller.SaveDataToCSV()
