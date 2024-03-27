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
import os
import csv
import time


class Controller(object):
    def __init__(self, count):
        self.count = count
        self.alldata = [('timestamp', 'traffic')]

    def testprocess(self):
        res = os.popen('adb shell ps | grep com.wepie.gudu')
        pid_output = res.readlines()

        if pid_output:
            pid = pid_output[0].split()[1]
            print("PID:", pid)

            current_time = self.get_current_time()
            print("Current time:", current_time)

            traffic = os.popen('adb shell cat /proc/{}/net/dev'.format(pid))
            for line in traffic:
                if 'wlan0' in line:
                    line = '#'.join(line.split())
                    recv = line.split('#')[1]
                    transmit = line.split('#')[9]
                    print(recv,transmit)
                    alltraffic = int(recv) + int(transmit)

                    alltraffic = str(alltraffic / 1024) + 'k'
                    print(alltraffic)
                    self.alldata.append((current_time, alltraffic))
        else:
            print("Process not found.")

    def run(self):
        while self.count > 0:
            self.testprocess()
            self.count -= 1
            time.sleep(60)

    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        return current_time

    def save_data_to_csv(self):
        file_path = '/Users/rourou/Documents/traffic.csv'
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.alldata)


if __name__ == '__main__':
    controller = Controller(60)
    controller.run()
    controller.save_data_to_csv()