#!/usr/bin/python
# encoding=utf-8
import datetime
import os
import threading

def execCmd(cmd):
    try:
        print("命令%s开始运行%s" % (cmd, datetime.datetime.now()))
        os.system(cmd)
        print("命令%s结束运行%s" % (cmd, datetime.datetime.now()))
    except:
        print('%s\t 运行失败' % (cmd))


if __name__ == '__main__':
    # 需要执行的命令列表
    model_list = ['5100.py', '5200.py','5300.py', '5400.py','5500.py', '5600.py','5700.py','5800.py','5900.py','6000.py']
    cmds = ['python proc_'+i for i in model_list]

    # 线程池
    threads = []

    print("程序开始运行%s" % datetime.datetime.now())

    for cmd in cmds:
        th = threading.Thread(target=execCmd, args=(cmd,))
        th.start()
        threads.append(th)

    # 等待线程运行完毕
    for th in threads:
        th.join()

    print("程序结束运行%s" % datetime.datetime.now())


