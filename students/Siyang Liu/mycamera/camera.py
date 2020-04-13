import mcpi.minecraft as minecraft
import mcpi.block as block
from movedetect import *
from myhouse import *
import threading

threads = []
t1 = threading.Thread(target = Inwhichhouse)
threads.append(t1)
t2 = threading.Thread(target = movedetect)
threads.append(t2)
if __name__=='__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()

print ("Excess.")