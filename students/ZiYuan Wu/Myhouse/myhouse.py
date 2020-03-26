import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

def roof(x,y,z,L,wordn):
    reader = csv.reader(open('e:/2020class/QianRuShi/minecraft_m3_all/myhouse/'+wordn+'.csv'))
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


        
def house(x,y,z,L):
    mc.setBlocks(x,y-1,z,x+L,y+5,z+L,5,block.TNT.id)
    mc.setBlocks(x+1,y,z+1,x+L-1,y+4,z+L-1,0)   #建一个火柴盒
    mc.setBlocks(x+3,y+1,z,x+4,y+2,z,block.GLASS.id)#窗
    mc.setBlocks(x+6,y,z,x+6,y+1,z,64)              #门
    
def PrintWords(x0,y0,z0,words):
    mc.setBlocks(x0,y0-10,z0,x0+200,y0+50,z0+200,0)
    wordy = words.split(".")
    numi = len(wordy)  #列数
    L0=9
    for i in range(numi):                 
        wordx=wordy[i].split()
        print(z0)
        x0=-184+1
        for j in range(len(wordx)):
            house(x0,y0,z0,L0)
            roof(x0,y0,z0,L0,wordx[j])
            x0=x0+L0+5
        z0=z0+L0+5
    
words = "W E L C O M E . T O M Y. H O U S E S. I [ C H I N A . I [ S U E P ." #空格隔离,'.'表示换行
PrintWords(-184,21,178,words) #输入起始位置及展示字母




