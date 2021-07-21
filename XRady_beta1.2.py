#!/usr/bin/python3
# coding=utf-8
# 多线程threading模块学习项目
# 长亭开发的Xray扫描器被动代理与Rad浏览器爬虫的批量联动脚本

import subprocess
import threading
import time
import sys
import os

banner = '''
Usage: Xrady.py [File Name]
e.g. python Xrady.py url.txt

将该脚本与Xray文件夹、Rad浏览器爬虫文件夹放在一起，扫描器与爬虫路径自行更改.
xray跟随主程序退出而退出
'''

# 后台运行Xray扫描器被动代理模式
def xray():
    times_Save = (time.strftime('%m%d%H%M%S',time.localtime(time.time())))	#xray保存的结果以时间命名保存至脚本目录
    xrayScan = subprocess.Popen(["xray_windows_amd64.exe\\xray_windows_amd64.exe","webscan","--listen","127.0.0.1:7777","--html-output","%s.html"%times_Save],stdout=subprocess.PIPE)
    xrayScan


    #xray_out = xrayScan.communicate()
    #xray_out
        

# 运行Rad浏览器爬虫，打印内容输出显示
def rad(run_rad, url):
    rad_cmd = run_rad + url
    os.system(rad_cmd)
    print('_'*50)
    print('[+]URL装载完毕，Next！')
    print('_'*50)

def run(fileName):
    systemVersion = sys.platform
    if systemVersion == 'win32':
        run_rad = "rad_windows_amd64.exe\\rad_windows_amd64.exe -http-proxy 127.0.0.1:7777 -t "
    elif systemVersion == 'darwin':
        run_rad = "rad_windows_amd64.exe\\rad_windows_amd64.exe -http-proxy 127.0.0.1:7777 -t "     # 自己改吧，没开Linux虚拟机也没mac，懒得试了
    domainFile = open(fileName,'r')
    domainUrl = domainFile.readlines()
    for url in domainUrl:
        rad(run_rad, url)


def main(argv):
    print(banner)
    t1 = threading.Thread(target=xray)
    t1.setDaemon(True)  # 把子线程设置为守护线程，必须在start()之前设置
    t1.start()
    time.sleep(5)   # 等xray的进程完全启动
    argvs_list = sys.argv[1:]
    run(argvs_list[0])
    size = threading.active_count()
    print('-'*50)
    print('总占用线程数为: %s 个\n'%str(size))
    print('人是会思考的芦苇')
    print('--帕斯卡尔')
    print('-'*50)
    time.sleep(9)


if __name__ == '__main__':
	main(sys.argv)