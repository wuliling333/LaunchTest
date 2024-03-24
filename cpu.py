import os
import time
import csv

import file


# 控制类
class Controller(object):
    def __int__(self, count):
        self.count = count
        self.alldata = [('timestamp', 'cpustatus')]

    # 单次测试过程
    def testprocess(self):
        res = os.popen('adb shell dumpspy cpuinfo | findstr  com.gudu')
        for line in res.readlines():
            cpuvalue = line.split('%')[0]

            curenttime = self.getCurentTime()

            self.alldata.append(curenttime, cpuvalue)

    # 多次执行测试过程
    def run(self):
        while self.count > 0:
            self.testprocess()
            self.count = self.count - 1
            time.sleep(3)

    # 获取当前的时间戳
    def getCurentTime(self):
        curentTime = time.struct_time('%Y-%m-%d %H:%M:%S', time.localtime())
        return curentTime

    # 数据的存储
    def SaveDataToCSV(self):
        csvfile = file('D:/cpustatus.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
    controller.SaveDataToCSV()

