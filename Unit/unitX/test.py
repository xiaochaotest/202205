'''
adb shell getevent获取坐标，将获取到的16进制坐标转为10进制（https://tool.oschina.net/hexconvert/）
'''
import os
import time
import threading

class ZhuanZhang():
    def zhuanzhang(self):
        # 选择转账人
        #os.system('adb -s C7YVB20413007239 shell input tap 960 366')
        #time.sleep(1)
        os.system("adb -s C7YVB20413007239 shell input tap 977 732")
        time.sleep(1)
        os.system("adb -s C7YVB20413007239 shell input tap 257 947")

        # 输入转账金额
        time.sleep(1)
        os.system("adb -s C7YVB20413007239 shell input tap 520 1538")
        time.sleep(1)
        os.system("adb -s C7YVB20413007239 shell input text \"0.01\"")

        # 下一步骤
        time.sleep(1)
        os.system("adb -s C7YVB20413007239 shell input tap 437 1321")

        # 下一步123
        time.sleep(1)
        os.system("adb -s C7YVB20413007239 shell input tap 454 1654")

        # 输入密码
        time.sleep(1)
        os.system("adb -s C7YVB20413007239 shell input text \"963852\"")

        time.sleep(1)
        os.system("adb -s C7YVB20413007239 shell input tap 306 1273")
        time.sleep(1)


if __name__ == '__main__':
    for i in range(300):
        ZhuanZhang().zhuanzhang()
        i += 1
        print("已成功转账：", i, "笔")