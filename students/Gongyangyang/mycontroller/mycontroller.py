import threading
from mchsv import *
from myhouse import *


threads = []

t1 = threading.Thread(target=Inwhichhouse) 
threads.append(t1)
t2 = threading.Thread(target=camera_det)
threads.append(t2)
if __name__=='__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
print ("退出")
