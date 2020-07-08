import tkinter as tk
import time
import mcpi.minecraft as minecraft
import mcpi.block as block
from pykeyboard import PyKeyboard
import math as m
from pymouse import PyMouse
import pymysql
conn = pymysql.connect('localhost', 'root', '', 'mysql')
cursor = conn.cursor()
k = PyKeyboard()
mouse = PyMouse()
mc = minecraft.Minecraft.create("47.100.46.95",4782)

mouse.move(862, 845)
time.sleep(0.5)
mouse.click(862, 845, 1)
time.sleep(0.5)
mouse.move(768, 246)
time.sleep(0.5)
mouse.click(768, 246, 1)


button = [[273,195],[273,202],[273,210],[273,219],[258,227],[243.216],[243,204],[258,187]]
roadx = [77,63,92]
roadz = [81,51,66]
houseposition = [[92,97],[63,81],[63,66],[63,51],[92,51],[92,66],[92,81]]
#0为村口的位置


def windows():
    for i in range(1,9):
        for j in range(1,6):
            sql ="SELECT `0%s` FROM `floor` WHERE `floor\class` = %f"%(str(i),int(j))
            try:
                cursor.execute(sql)
                conn.commit()
            except:
                conn.rollback()
                conn.close()
            a = cursor.fetchone()
            if a[0] == 'ON':
                openwindows(100*j+i)
            elif a[0] == 'OFF':
                closewindows(100*j+i)
            
    
    
def doors():
    sql ="SELECT `door_state` FROM `door`"
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        conn.close()
    a = cursor.fetchone()
    if a[0] == 'ON':
        opendoors()
    elif a[0] == 'OFF':
        closedoors()
    
def openwindows(a):
    pos = [[274,193],[274,196],[274,200],[274,203],[274,207],[274,211],[274,217],[274,220],[260,228],[257,228],[242,218],[242,215],[242,211],[242,206],[242,203],[242,199],[256,186],[259,186]]
    if a == "all":
        for c in range(1,9):
            for d in range(1,6):
                if c in (1,2,3,4):
                    sql = "UPDATE `floor` SET `0%s` ='ON' WHERE `floor\class` = %f"%(str(c),int(d))
                    try:
                        cursor.execute(sql)
                        conn.commit()
                    except:
                        conn.rollback()
                        conn.close()
                    mc.setBlocks(pos[(c-1)*2][0],-19+((d-1)*4),pos[(c-1)*2][1],pos[(c-1)*2][0],-18+((d-1)*4),pos[(c-1)*2][1],0)
                    mc.setBlocks(pos[(c-1)*2+1][0],-19+((d-1)*4),pos[(c-1)*2+1][1],pos[(c-1)*2+1][0],-18+((d-1)*4),pos[(c-1)*2+1][1],0)
                    mc.setBlocks(pos[(c-1)*2][0]+1,-19+((d-1)*4),pos[(c-1)*2][1]+1,pos[(c-1)*2][0]+1,-18+((d-1)*4),pos[(c-1)*2][1]+1,102)
                    mc.setBlocks(pos[(c-1)*2+1][0]+1,-19+((d-1)*4),pos[(c-1)*2+1][1]+1,pos[(c-1)*2+1][0]+1,-18+((d-1)*4),pos[(c-1)*2+1][1]+1,102)
                elif c == 5:
                    if d >= 2:
                        sql = "UPDATE `floor` SET `0%s` ='ON' WHERE `floor\class` = %f"%(str(c),int(d))
                        try:
                            cursor.execute(sql)
                            conn.commit()
                        except:
                            conn.rollback()
                            conn.close()
                        mc.setBlocks(pos[(c-1)*2][0],-19+((d-1)*4),pos[(c-1)*2][1],pos[(c-1)*2][0],-18+((d-1)*4),pos[(c-1)*2][1],0)
                        mc.setBlocks(pos[(c-1)*2+1][0],-19+((d-1)*4),pos[(c-1)*2+1][1],pos[(c-1)*2+1][0],-18+((d-1)*4),pos[(c-1)*2+1][1],0)
                        mc.setBlocks(pos[(c-1)*2][0]-1,-19+((d-1)*4),pos[(c-1)*2][1]+1,pos[(c-1)*2][0]-1,-18+((d-1)*4),pos[(c-1)*2][1]+1,102)
                        mc.setBlocks(pos[(c-1)*2+1][0]-1,-19+((d-1)*4),pos[(c-1)*2+1][1]+1,pos[(c-1)*2+1][0]-1,-18+((d-1)*4),pos[(c-1)*2+1][1]+1,102)
                elif c in (6,7):
                    sql = "UPDATE `floor` SET `0%s` ='ON' WHERE `floor\class` = %f"%(str(c),int(d))
                    try:
                        cursor.execute(sql)
                        conn.commit()
                    except:
                        conn.rollback()
                        conn.close()
                    mc.setBlocks(pos[5*2+((c-6)*3)][0],-19+((d-1)*4),pos[5*2+((c-6)*3)][1],pos[5*2+((c-6)*3)][0],-18+((d-1)*4),pos[5*2+((c-6)*3)][1],0)
                    mc.setBlocks(pos[5*2+1+((c-6)*3)][0],-19+((d-1)*4),pos[5*2+1+((c-6)*3)][1],pos[5*2+1+((c-6)*3)][0],-18+((d-1)*4),pos[5*2+1+((c-6)*3)][1],0)
                    mc.setBlocks(pos[5*2+2+((c-6)*3)][0],-19+((d-1)*4),pos[5*2+2+((c-6)*3)][1],pos[5*2+2+((c-6)*3)][0],-18+((d-1)*4),pos[5*2+2+((c-6)*3)][1],0)
                    mc.setBlocks(pos[5*2+((c-6)*3)][0]-1,-19+((d-1)*4),pos[5*2+((c-6)*3)][1]-1,pos[5*2+((c-6)*3)][0]-1,-18+((d-1)*4),pos[5*2+((c-6)*3)][1]-1,102)
                    mc.setBlocks(pos[5*2+1+((c-6)*3)][0]-1,-19+((d-1)*4),pos[5*2+1+((c-6)*3)][1]-1,pos[5*2+1+((c-6)*3)][0]-1,-18+((d-1)*4),pos[5*2+1+((c-6)*3)][1]-1,102)
                    mc.setBlocks(pos[5*2+2+((c-6)*3)][0]-1,-19+((d-1)*4),pos[5*2+2+((c-6)*3)][1]-1,pos[5*2+2+((c-6)*3)][0]-1,-18+((d-1)*4),pos[5*2+2+((c-6)*3)][1]-1,102)
                elif c == 8:
                    sql = "UPDATE `floor` SET `0%s` ='ON' WHERE `floor\class` = %f"%(str(c),int(d))
                    try:
                        cursor.execute(sql)
                        conn.commit()
                    except:
                        conn.rollback()
                        conn.close()
                    mc.setBlocks(pos[16][0],-19+((d-1)*4),pos[16][1],pos[16][0],-18+((d-1)*4),pos[16][1],0)
                    mc.setBlocks(pos[17][0],-19+((d-1)*4),pos[17][1],pos[17][0],-18+((d-1)*4),pos[17][1],0)
                    mc.setBlocks(pos[16][0]+1,-19+((d-1)*4),pos[16][1]-1,pos[16][0]+1,-18+((d-1)*4),pos[16][1]-1,102)
                    mc.setBlocks(pos[17][0]+1,-19+((d-1)*4),pos[17][1]-1,pos[17][0]+1,-18+((d-1)*4),pos[17][1]-1,102)
    else:
        d = int(a/100)
        c = a - (d*100)
        if c in (1,2,3,4):
            sql = "UPDATE `floor` SET `0%s` ='ON' WHERE `floor\class` = %f"%(str(c),int(d))
            try:
                cursor.execute(sql)
                conn.commit()
            except:
                conn.rollback()
                conn.close()
            mc.setBlocks(pos[(c-1)*2][0],-19+((d-1)*4),pos[(c-1)*2][1],pos[(c-1)*2][0],-18+((d-1)*4),pos[(c-1)*2][1],0)
            mc.setBlocks(pos[(c-1)*2+1][0],-19+((d-1)*4),pos[(c-1)*2+1][1],pos[(c-1)*2+1][0],-18+((d-1)*4),pos[(c-1)*2+1][1],0)
            mc.setBlocks(pos[(c-1)*2][0]+1,-19+((d-1)*4),pos[(c-1)*2][1]+1,pos[(c-1)*2][0]+1,-18+((d-1)*4),pos[(c-1)*2][1]+1,102)
            mc.setBlocks(pos[(c-1)*2+1][0]+1,-19+((d-1)*4),pos[(c-1)*2+1][1]+1,pos[(c-1)*2+1][0]+1,-18+((d-1)*4),pos[(c-1)*2+1][1]+1,102)
        elif c == 5:
            if d >= 2:
                sql = "UPDATE `floor` SET `0%s` ='ON' WHERE `floor\class` = %f"%(str(c),int(d))
                try:
                    cursor.execute(sql)
                    conn.commit()
                except:
                    conn.rollback()
                    conn.close()
                mc.setBlocks(pos[(c-1)*2][0],-19+((d-1)*4),pos[(c-1)*2][1],pos[(c-1)*2][0],-18+((d-1)*4),pos[(c-1)*2][1],0)
                mc.setBlocks(pos[(c-1)*2+1][0],-19+((d-1)*4),pos[(c-1)*2+1][1],pos[(c-1)*2+1][0],-18+((d-1)*4),pos[(c-1)*2+1][1],0)
                mc.setBlocks(pos[(c-1)*2][0]-1,-19+((d-1)*4),pos[(c-1)*2][1]+1,pos[(c-1)*2][0]-1,-18+((d-1)*4),pos[(c-1)*2][1]+1,102)
                mc.setBlocks(pos[(c-1)*2+1][0]-1,-19+((d-1)*4),pos[(c-1)*2+1][1]+1,pos[(c-1)*2+1][0]-1,-18+((d-1)*4),pos[(c-1)*2+1][1]+1,102)
        elif c in (6,7):
            sql = "UPDATE `floor` SET `0%s` ='ON' WHERE `floor\class` = %f"%(str(c),int(d))
            try:
                cursor.execute(sql)
                conn.commit()
            except:
                conn.rollback()
                conn.close()
            mc.setBlocks(pos[5*2+((c-6)*3)][0],-19+((d-1)*4),pos[5*2+((c-6)*3)][1],pos[5*2+((c-6)*3)][0],-18+((d-1)*4),pos[5*2+((c-6)*3)][1],0)
            mc.setBlocks(pos[5*2+1+((c-6)*3)][0],-19+((d-1)*4),pos[5*2+1+((c-6)*3)][1],pos[5*2+1+((c-6)*3)][0],-18+((d-1)*4),pos[5*2+1+((c-6)*3)][1],0)
            mc.setBlocks(pos[5*2+2+((c-6)*3)][0],-19+((d-1)*4),pos[5*2+2+((c-6)*3)][1],pos[5*2+2+((c-6)*3)][0],-18+((d-1)*4),pos[5*2+2+((c-6)*3)][1],0)
            mc.setBlocks(pos[5*2+((c-6)*3)][0]-1,-19+((d-1)*4),pos[5*2+((c-6)*3)][1]-1,pos[5*2+((c-6)*3)][0]-1,-18+((d-1)*4),pos[5*2+((c-6)*3)][1]-1,102)
            mc.setBlocks(pos[5*2+1+((c-6)*3)][0]-1,-19+((d-1)*4),pos[5*2+1+((c-6)*3)][1]-1,pos[5*2+1+((c-6)*3)][0]-1,-18+((d-1)*4),pos[5*2+1+((c-6)*3)][1]-1,102)
            mc.setBlocks(pos[5*2+2+((c-6)*3)][0]-1,-19+((d-1)*4),pos[5*2+2+((c-6)*3)][1]-1,pos[5*2+2+((c-6)*3)][0]-1,-18+((d-1)*4),pos[5*2+2+((c-6)*3)][1]-1,102)
        elif c == 8:
            sql = "UPDATE `floor` SET `0%s` ='ON' WHERE `floor\class` = %f"%(str(c),int(d))
            try:
                cursor.execute(sql)
                conn.commit()
            except:
                conn.rollback()
                conn.close()
            mc.setBlocks(pos[16][0],-19+((d-1)*4),pos[16][1],pos[16][0],-18+((d-1)*4),pos[16][1],0)
            mc.setBlocks(pos[17][0],-19+((d-1)*4),pos[17][1],pos[17][0],-18+((d-1)*4),pos[17][1],0)
            mc.setBlocks(pos[16][0]+1,-19+((d-1)*4),pos[16][1]-1,pos[16][0]+1,-18+((d-1)*4),pos[16][1]-1,102)
            mc.setBlocks(pos[17][0]+1,-19+((d-1)*4),pos[17][1]-1,pos[17][0]+1,-18+((d-1)*4),pos[17][1]-1,102)
        
        
    
        
    
    
def closewindows(a):
    
    pos = [[274,193],[274,196],[274,200],[274,203],[274,207],[274,211],[274,217],[274,220],[260,228],[257,228],[242,218],[242,215],[242,211],[242,206],[242,203],[242,199],[256,186],[259,186]]
    if a == "all":
        for c in range(1,9):
            for d in range(1,6):
                if c in (1,2,3,4):
                    sql = "UPDATE `floor` SET `0%s` ='OFF' WHERE `floor\class` = %f"%(str(c),int(d))
                    try:
                        cursor.execute(sql)
                        conn.commit()
                    except:
                        conn.rollback()
                        conn.close()
                    mc.setBlocks(pos[(c-1)*2][0],-19+((d-1)*4),pos[(c-1)*2][1],pos[(c-1)*2][0],-18+((d-1)*4),pos[(c-1)*2][1],102)
                    mc.setBlocks(pos[(c-1)*2+1][0],-19+((d-1)*4),pos[(c-1)*2+1][1],pos[(c-1)*2+1][0],-18+((d-1)*4),pos[(c-1)*2+1][1],102)
                    mc.setBlocks(pos[(c-1)*2][0]+1,-19+((d-1)*4),pos[(c-1)*2][1]+1,pos[(c-1)*2][0]+1,-18+((d-1)*4),pos[(c-1)*2][1]+1,0)
                    mc.setBlocks(pos[(c-1)*2+1][0]+1,-19+((d-1)*4),pos[(c-1)*2+1][1]+1,pos[(c-1)*2+1][0]+1,-18+((d-1)*4),pos[(c-1)*2+1][1]+1,0)
                if c == 5:
                    if d >= 2:
                        sql = "UPDATE `floor` SET `0%s` ='OFF' WHERE `floor\class` = %f"%(str(c),int(d))
                        try:
                            cursor.execute(sql)
                            conn.commit()
                        except:
                            conn.rollback()
                            conn.close()
                        mc.setBlocks(pos[(c-1)*2][0],-19+((d-1)*4),pos[(c-1)*2][1],pos[(c-1)*2][0],-18+((d-1)*4),pos[(c-1)*2][1],102)
                        mc.setBlocks(pos[(c-1)*2+1][0],-19+((d-1)*4),pos[(c-1)*2+1][1],pos[(c-1)*2+1][0],-18+((d-1)*4),pos[(c-1)*2+1][1],102)
                        mc.setBlocks(pos[(c-1)*2][0]-1,-19+((d-1)*4),pos[(c-1)*2][1]+1,pos[(c-1)*2][0]-1,-18+((d-1)*4),pos[(c-1)*2][1]+1,0)
                        mc.setBlocks(pos[(c-1)*2+1][0]-1,-19+((d-1)*4),pos[(c-1)*2+1][1]+1,pos[(c-1)*2+1][0]-1,-18+((d-1)*4),pos[(c-1)*2+1][1]+1,0)
                elif c in (6,7):
                    sql = "UPDATE `floor` SET `0%s` ='OFF' WHERE `floor\class` = %f"%(str(c),int(d))
                    try:
                        cursor.execute(sql)
                        conn.commit()
                    except:
                        conn.rollback()
                        conn.close()
                    mc.setBlocks(pos[5*2+((c-6)*3)][0],-19+((d-1)*4),pos[5*2+((c-6)*3)][1],pos[5*2+((c-6)*3)][0],-18+((d-1)*4),pos[5*2+((c-6)*3)][1],102)
                    mc.setBlocks(pos[5*2+1+((c-6)*3)][0],-19+((d-1)*4),pos[5*2+1+((c-6)*3)][1],pos[5*2+1+((c-6)*3)][0],-18+((d-1)*4),pos[5*2+1+((c-6)*3)][1],102)
                    mc.setBlocks(pos[5*2+2+((c-6)*3)][0],-19+((d-1)*4),pos[5*2+2+((c-6)*3)][1],pos[5*2+2+((c-6)*3)][0],-18+((d-1)*4),pos[5*2+2+((c-6)*3)][1],102)
                    mc.setBlocks(pos[5*2+((c-6)*3)][0]-1,-19+((d-1)*4),pos[5*2+((c-6)*3)][1]-1,pos[5*2+((c-6)*3)][0]-1,-18+((d-1)*4),pos[5*2+((c-6)*3)][1]-1,0)
                    mc.setBlocks(pos[5*2+1+((c-6)*3)][0]-1,-19+((d-1)*4),pos[5*2+1+((c-6)*3)][1]-1,pos[5*2+1+((c-6)*3)][0]-1,-18+((d-1)*4),pos[5*2+1+((c-6)*3)][1]-1,0)
                    mc.setBlocks(pos[5*2+2+((c-6)*3)][0]-1,-19+((d-1)*4),pos[5*2+2+((c-6)*3)][1]-1,pos[5*2+2+((c-6)*3)][0]-1,-18+((d-1)*4),pos[5*2+2+((c-6)*3)][1]-1,0)
                elif c == 8:
                    sql = "UPDATE `floor` SET `0%s` ='OFF' WHERE `floor\class` = %f"%(str(c),int(d))
                    try:
                        cursor.execute(sql)
                        conn.commit()
                    except:
                        conn.rollback()
                        conn.close()
                    mc.setBlocks(pos[16][0],-19+((d-1)*4),pos[16][1],pos[16][0],-18+((d-1)*4),pos[16][1],102)
                    mc.setBlocks(pos[17][0],-19+((d-1)*4),pos[17][1],pos[17][0],-18+((d-1)*4),pos[17][1],102)
                    mc.setBlocks(pos[16][0]+1,-19+((d-1)*4),pos[16][1]-1,pos[16][0]+1,-18+((d-1)*4),pos[16][1]-1,0)
                    mc.setBlocks(pos[17][0]+1,-19+((d-1)*4),pos[17][1]-1,pos[17][0]+1,-18+((d-1)*4),pos[17][1]-1,0) 
    else:        
        d = int(a/100)
        c = a - (d*100)
        
        if c in (1,2,3,4):
            sql = "UPDATE `floor` SET `0%s` ='OFF' WHERE `floor\class` = %f"%(str(c),int(d))
            try:
                cursor.execute(sql)
                conn.commit()
            except:
                conn.rollback()
                conn.close()
            mc.setBlocks(pos[(c-1)*2][0],-19+((d-1)*4),pos[(c-1)*2][1],pos[(c-1)*2][0],-18+((d-1)*4),pos[(c-1)*2][1],102)
            mc.setBlocks(pos[(c-1)*2+1][0],-19+((d-1)*4),pos[(c-1)*2+1][1],pos[(c-1)*2+1][0],-18+((d-1)*4),pos[(c-1)*2+1][1],102)
            mc.setBlocks(pos[(c-1)*2][0]+1,-19+((d-1)*4),pos[(c-1)*2][1]+1,pos[(c-1)*2][0]+1,-18+((d-1)*4),pos[(c-1)*2][1]+1,0)
            mc.setBlocks(pos[(c-1)*2+1][0]+1,-19+((d-1)*4),pos[(c-1)*2+1][1]+1,pos[(c-1)*2+1][0]+1,-18+((d-1)*4),pos[(c-1)*2+1][1]+1,0)
        if c == 5:
            if d >= 2:
                sql = "UPDATE `floor` SET `0%s` ='OFF' WHERE `floor\class` = %f"%(str(c),int(d))
                try:
                    cursor.execute(sql)
                    conn.commit()
                except:
                    conn.rollback()
                    conn.close()
                mc.setBlocks(pos[(c-1)*2][0],-19+((d-1)*4),pos[(c-1)*2][1],pos[(c-1)*2][0],-18+((d-1)*4),pos[(c-1)*2][1],102)
                mc.setBlocks(pos[(c-1)*2+1][0],-19+((d-1)*4),pos[(c-1)*2+1][1],pos[(c-1)*2+1][0],-18+((d-1)*4),pos[(c-1)*2+1][1],102)
                mc.setBlocks(pos[(c-1)*2][0]-1,-19+((d-1)*4),pos[(c-1)*2][1]+1,pos[(c-1)*2][0]-1,-18+((d-1)*4),pos[(c-1)*2][1]+1,0)
                mc.setBlocks(pos[(c-1)*2+1][0]-1,-19+((d-1)*4),pos[(c-1)*2+1][1]+1,pos[(c-1)*2+1][0]-1,-18+((d-1)*4),pos[(c-1)*2+1][1]+1,0)
        elif c in (6,7):
            sql = "UPDATE `floor` SET `0%s` ='OFF' WHERE `floor\class` = %f"%(str(c),int(d))
            try:
                cursor.execute(sql)
                conn.commit()
            except:
                conn.rollback()
                conn.close()
            mc.setBlocks(pos[5*2+((c-6)*3)][0],-19+((d-1)*4),pos[5*2+((c-6)*3)][1],pos[5*2+((c-6)*3)][0],-18+((d-1)*4),pos[5*2+((c-6)*3)][1],102)
            mc.setBlocks(pos[5*2+1+((c-6)*3)][0],-19+((d-1)*4),pos[5*2+1+((c-6)*3)][1],pos[5*2+1+((c-6)*3)][0],-18+((d-1)*4),pos[5*2+1+((c-6)*3)][1],102)
            mc.setBlocks(pos[5*2+2+((c-6)*3)][0],-19+((d-1)*4),pos[5*2+2+((c-6)*3)][1],pos[5*2+2+((c-6)*3)][0],-18+((d-1)*4),pos[5*2+2+((c-6)*3)][1],102)
            mc.setBlocks(pos[5*2+((c-6)*3)][0]-1,-19+((d-1)*4),pos[5*2+((c-6)*3)][1]-1,pos[5*2+((c-6)*3)][0]-1,-18+((d-1)*4),pos[5*2+((c-6)*3)][1]-1,0)
            mc.setBlocks(pos[5*2+1+((c-6)*3)][0]-1,-19+((d-1)*4),pos[5*2+1+((c-6)*3)][1]-1,pos[5*2+1+((c-6)*3)][0]-1,-18+((d-1)*4),pos[5*2+1+((c-6)*3)][1]-1,0)
            mc.setBlocks(pos[5*2+2+((c-6)*3)][0]-1,-19+((d-1)*4),pos[5*2+2+((c-6)*3)][1]-1,pos[5*2+2+((c-6)*3)][0]-1,-18+((d-1)*4),pos[5*2+2+((c-6)*3)][1]-1,0)
        elif c == 8:
            sql = "UPDATE `floor` SET `0%s` ='OFF' WHERE `floor\class` = %f"%(str(c),int(d))
            try:
                cursor.execute(sql)
                conn.commit()
            except:
                conn.rollback()
                conn.close()
            mc.setBlocks(pos[16][0],-19+((d-1)*4),pos[16][1],pos[16][0],-18+((d-1)*4),pos[16][1],102)
            mc.setBlocks(pos[17][0],-19+((d-1)*4),pos[17][1],pos[17][0],-18+((d-1)*4),pos[17][1],102)
            mc.setBlocks(pos[16][0]+1,-19+((d-1)*4),pos[16][1]-1,pos[16][0]+1,-18+((d-1)*4),pos[16][1]-1,0)
            mc.setBlocks(pos[17][0]+1,-19+((d-1)*4),pos[17][1]-1,pos[17][0]+1,-18+((d-1)*4),pos[17][1]-1,0)        
        
    
    
def opendoors():
    #正面
    mc.setBlocks(263,-19,228,264,-20,228,0)
    mc.setBlocks(262,-19,229,262,-20,229,102)
    mc.setBlocks(265,-19,229,265,-20,229,102)
    mc.setBlocks(259,-19,228,257,-20,228,0)
    mc.setBlocks(260,-19,229,260,-20,229,102)
    mc.setBlocks(256,-19,229,256,-20,229,102)
    mc.setBlocks(252,-19,228,253,-20,228,0)
    mc.setBlocks(251,-19,229,251,-20,229,102)
    mc.setBlocks(254,-19,229,254,-20,229,102)
    #背面
    mc.setBlocks(252,-19,186,252,-20,186,0)
    mc.setBlocks(251,-19,185,251,-20,185,102)
    mc.setBlocks(253,-19,185,253,-20,185,102)
    mc.setBlocks(265,-19,186,265,-20,186,0)
    mc.setBlocks(264,-19,185,264,-20,185,102)
    mc.setBlocks(266,-19,185,266,-20,185,102)

    
    
    
    
    
    

def closedoors():
    #正面
    mc.setBlocks(263,-19,228,264,-20,228,102)
    mc.setBlocks(262,-19,229,262,-20,229,0)
    mc.setBlocks(265,-19,229,265,-20,229,0)
    mc.setBlocks(259,-19,228,257,-20,228,102)
    mc.setBlocks(260,-19,229,260,-20,229,0)
    mc.setBlocks(256,-19,229,256,-20,229,0)
    mc.setBlocks(252,-19,228,253,-20,228,102)
    mc.setBlocks(251,-19,229,251,-20,229,0)
    mc.setBlocks(254,-19,229,254,-20,229,0)
    #背面
    mc.setBlocks(252,-19,186,252,-20,186,102)
    mc.setBlocks(251,-19,185,251,-20,185,0)
    mc.setBlocks(253,-19,185,253,-20,185,0)
    mc.setBlocks(265,-19,186,265,-20,186,102)
    mc.setBlocks(264,-19,185,264,-20,185,0)
    mc.setBlocks(266,-19,185,266,-20,185,0)
    

    


  


    
    
    




    
    
   
    
    
            
            
            
            


