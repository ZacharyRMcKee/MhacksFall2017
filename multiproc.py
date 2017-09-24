from multiprocessing import Process
import os
import time
def f():
    os.system('aplay alarm.wav')

if __name__ == '__main__':
    p = Process(target=f)
    p.start()
    i = 1
    while(True):
        time.sleep(0.1)
        i += 1
        print(i)
    p.join()
