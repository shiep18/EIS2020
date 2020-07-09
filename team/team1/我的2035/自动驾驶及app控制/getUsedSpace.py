#!/usr/bin/python3
#coding=utf8
import os
import sys

if sys.version_info.major == 2:
    print('Please run this program with python3!')
    sys.exit(0)

def getDiskSpace():
    p = os.popen("df -h")
    i = 0
    while True:
        i += 1
        line = p.readline()
        if i == 2:
            remain_space = line.split()[-3]
            if "G" in remain_space:
                remain_space = float(remain_space.strip("G"))*1000
            else:
                remain_space = 0.0
            return int(remain_space)

if __name__ == '__main__':#使用例程
    print(getDiskSpace())
