from HouseClass import *
import csv,time

def ReadCsv():
    csv_reader=csv.reader(open('set.csv',encoding='utf-8'))
    L=[]
    for row in csv_reader:
        L.append(row)
    return L

def CsvToNum(L=[]):
    num=0
    for i in L:
        num=num*10+int(i)
    return num

with open('set.csv', "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()   #清空文件

P=[]
print('The code is running......')

while True:
    L=ReadCsv()
    if L != []:
        print(L)
        for i in L:
            P.append(CsvToNum(i))
            print(CsvToNum(i))
        print(P)
        break
mc.postToChat('House is building ......')
time.sleep(5)
mc.player.setTilePos([505,0,500])
house1=House('BigHouse1',P[0],P[1],P[2],P[3],P[4],P[5])
house1.SetHouse()
