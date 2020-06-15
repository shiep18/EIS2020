from PIL import Image
import pymysql
from pyzbar import pyzbar
from MyQR import myqr
from xpinyin import Pinyin
import cv2
import os

def getbooksplace(name):
    conn = pymysql.connect('localhost', 'root', '', 'library')
    cursor = conn.cursor()   
    sql = "SELECT * FROM books WHERE bookname = '%s'" % name
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        place = row[1]
    place=place.split("-")
    return place

def getPinYin(result):
    pin = Pinyin()
    return pin.get_pinyin(result)
def scanqr(bookname):
    conn = pymysql.connect('localhost', 'root', '', 'library')
    cursor = conn.cursor()   
    sql = "SELECT * FROM books WHERE state2 = 1 and state1 = 1" 
    cursor.execute(sql)
    results = cursor.fetchall()
    floor1=0
    floor2=0
    floor3=0
    #生成二维码
    for row in results:
        place = row[1]
        place=place.split("-")
        myqr.run(words=getPinYin(row[0]),save_name='floor'+place[0]+'\\'+getPinYin(row[0])+'.jpg')
        img=cv2.imread('floor'+place[0]+'\\'+getPinYin(row[0])+'.jpg')
        cv2.imwrite('floor'+place[0]+'\\'+getPinYin(row[0])+'.jpg',cv2.resize(img,(300,300)))
        if place[0] == '01':
            floor1=floor1+1
        elif place[0] == '02':
            floor2=floor2+1
        elif place[0] == '03':
            floor3=floor3+1
    #将二维码集合到一张图内
    allimg01 = Image.new('RGB', (20+400*floor1, 400), (255, 255, 255))
    allimg02 = Image.new('RGB', (20+400*floor2, 400), (255, 255, 255))
    allimg03 = Image.new('RGB', (20+400*floor3, 400), (255, 255, 255))
    floor1=0
    floor2=0
    floor3=0
    for row in results:
        place = row[1]
        place=place.split("-")
        if place[0] == '01':
            img=Image.open('floor'+place[0]+'\\'+getPinYin(row[0])+'.jpg')
            allimg01.paste(img,(20+floor1*380,20))
            floor1=floor1+1
            os.remove('floor'+place[0]+'\\'+getPinYin(row[0])+'.jpg')
        elif place[0] == '02':
            img=Image.open('floor'+place[0]+'\\'+getPinYin(row[0])+'.jpg')
            allimg02.paste(img,(20+floor2*380,20))
            floor2=floor2+1
            os.remove('floor'+place[0]+'\\'+getPinYin(row[0])+'.jpg')
        elif place[0] == '03':
            img=Image.open('floor'+place[0]+'\\'+getPinYin(row[0])+'.jpg')
            allimg03.paste(img,(20+floor3*380,20))
            floor3=floor3+1
            os.remove('floor'+place[0]+'\\'+getPinYin(row[0])+'.jpg')
    allimg01.save('floor01\\allimg01.jpg')
    allimg02.save('floor02\\allimg02.jpg')
    allimg03.save('floor03\\allimg03.jpg')
    bookplace = getbooksplace(bookname)
    allimg=Image.open('floor'+bookplace[0]+'\\'+'allimg'+bookplace[0]+'.jpg')
    test = pyzbar.decode(allimg)
    for tests in test:
        testdate = tests.data.decode('utf-8')
        if getPinYin(bookname) == testdate:
            return 1
    return 0