# coding=utf-8
# coding=gbk
# @author: rourou
# @file: memory.py
# @time: 2024/3/25 14:46
# @desc:
import os
import time
import csv
# 先在控制台中输入命令到指定的文件夹
"""内存   在控制台运行adb shell top /Users/rourou/Documents/memoinfo"""


# 控制类
class Controller(object):
    def __int__(self):
        self.alldata = [('id','vss','rss')]
    # 读取数据
    def readfile(self):
        file_path = '/Users/rourou/Documents/memoinfo'
        with open(file_path, 'r', newline='') as csvfile:
            #
            content = csvfile.read()
            csvfile.close()
            return content
    # 分析数据
    def analyzedata(self):
        content = self.readfile()
        i = 1
        for line in content:
            if 'com'in line:
                line = '#'.join(line.split())
                vss = line.split('#')[5]
                rss = line.split('#')[6]
                self.alldata.append((i,vss,rss))
                i = i+1


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
    controller.analyzedata()
    controller.SaveDataToCSV()
