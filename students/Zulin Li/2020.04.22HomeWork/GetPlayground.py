import csv
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
def ReadCsv():
    csv_reader=csv.reader(open('Playground.csv',encoding='utf-8'))
    L=[]
    for row in csv_reader:
        L.append(row)
    return L

def GetPlayground():
    K=ReadCsv()
    for i in range(10):
        for j in range(10):
            mc.setBlock(530+i,-1,500+j,int(K[i][j]))  # 底部

if __name__=='__main__':
    mc.player.setTilePos([535, 8, 505])
    GetPlayground()