import os
import time
import csv




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

            self.alldata.append((curenttime, cpuvalue))

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
        file_path = '/Users/rourou/Documents/cpu.csv'
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

