import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

def changpos(dir):
    if dir == "left":
        mc.player.setPos(pos.x-4,pos.y,pos.z)
    elif dir == "right":
        mc.player.setPos(pos.x+4,pos.y,pos.z)
    elif dir == "front":
        mc.player.setPos(pos.x,pos.y,pos.z+4)
    elif dir == "back":
        mc.player.setPos(pos.x,pos.y,pos.z-4)
    elif dir == "up":
        mc.player.setPos(pos.x,pos.y+4,pos.z)
    else :
        mc.player.setPos(pos.x,pos.y-4,pos.z)

def roof(x,y,z,L,wordn):
    reader = csv.reader(open('e:/2020class/QianRuShi/Soundrecog/倍塔狗语音识别 alpha_1.0/CSV/'+wordn+'.csv'))
    data=[]
    for r in reader:
        data.append(r)
    for i in range(10):
        for j in range(10):
            if (data[j][i]=='1'):
                mc.setBlock(x+i,y+5,z+j,158)
           # elif (data[j][i]=='2'):
           #     mc.setBlock(x+i,y+5,z+j,169)
                
           # elif (data[j][i]=='3'):
           #     mc.setBlock(x+i,y+5,z+j,158)
            else:
                mc.setBlock(x+i,y+5,z+j,169)
                mc.setBlock(x+i,y+6,z+j,50)


def PrintWords(x0,y0,z0,words):
    mc.player.setPos(1310,58,836)
    mc.setBlocks(x0,y0-10,z0,x0+200,y0+50,z0+200,0)
    wordy = words.split(".")
    numi = len(wordy)  #列数
    L0=9
    for i in range(numi):                 
        wordx=wordy[i]
        print(z0)
        for j in range(len(wordx)):
            #house(x0,y0,z0,L0)
            roof(x0,y0,z0,L0,wordx[j])
            x0=x0+L0+1
        z0=z0+L0+3
        x0=1273+3*L0+1

