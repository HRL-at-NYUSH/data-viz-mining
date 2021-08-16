def get_list(j):
    i=j
    strs = "model_list = ['"
    while i<=j+30:
        strs = strs+str(i)+".py','"
        i+=1
    strs = strs+"']"
    return strs
a = '''#!/usr/bin/python
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
    '''
b = '''
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
    #import playsound

# wait for the sound to finish playing?
   # blocking = True
   # playsound.playsound("SAMPLE.mp3", block=blocking)
'''
start = 9000
x = ''
while start<=10000:
    x = x +a + get_list(start)+b
    start = start+30
with open('out.py','w',encoding='utf-8')as f:
    f.write(x)
