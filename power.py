# coding=utf-8
# coding=gbk
# @author: rourou
# @file: power.py
# @time: 2024/3/25 14:32
# @desc:
import os
import time
import csv

"""耗电量  adb shell dumpsys battery """


# 控制类
class Controller(object):
    def __int__(self, count):
        self.count = count
        self.alldata = [('timestamp', 'power')]

    # 单次测试过程
    def testprocess(self):
        os.popen('adb shell dumpsys battery set status 1')
        res = os.popen(('adb shell dumpsys battery'))
        # 获取电量的lever
        for line in res.readlines():
            if "level" in line:
                power = line.split(':')[1]
                curenttime = self.getCurentTime()
                self.alldata.append((curenttime, power))

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
        file_path = '/Users/rourou/Documents/power.csv'
        with open(file_path, 'w', newline='') as csvfile:
            # 创建初始化写入对象
            writer = csv.writer(csvfile)
            # 写入数值
            writer.writerows(self.alldata)
            csvfile.close()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
    controller.SaveDataToCSV()
