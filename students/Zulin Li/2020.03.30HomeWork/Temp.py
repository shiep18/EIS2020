import mcpi.minecraft as minecraft
import mcpi.block as block
#导入模块：游戏本体、方块
mc = minecraft.Minecraft.create()
'''
pos = mc.player.getTilePos()#玩家位置
print(pos.x,pos.y,pos.z)
'''
mc.setBlock(17, 9, 0,1)
mc.player.setTilePos([17,10,0])
e=152
def SetBuild(num):
    i=79
    b=22
    y=41
    o=220
    r=152
    temp=[
                 [1,1,1,1,1],
                  [1,i,i,i,1],
                  [1,i,i,i,1],
                  [1,i,i,i,1],
                 [1,1,b,1,1],
                 [1,1,b,1,1],
                 [1,1,b,1,1],
                 [1,1,b,1,1],
               [1,49,b,49,1],
                 [1,1,b,1,1],
                 [1,1,b,1,1],
                 [1,1,b,1,1],
                 [1,1,b,1,1],
               [1,49,b,49,1],
                 [1,1,y,1,1],
                 [1,1,y,1,1],
                 [1,1,y,1,1],
                 [1,1,y,1,1],
               [1,49,y,49,1],
                 [1,1,y,1,1],
                 [1,1,y,1,1],
                 [1,1,y,1,1],
                 [1,1,y,1,1],
               [1,49,y,49,1],
                 [1,1,o,1,1],
                 [1,1,o,1,1],
                 [1,1,o,1,1],
                 [1,1,o,1,1],
               [1,49,o,49,1],
                 [1,1,o,1,1],
                 [1,1,o,1,1],
                 [1,1,o,1,1],
                 [1,1,o,1,1],
               [1,49,o,49,1], 
                 [1,1,r,1,1],
                 [1,1,r,1,1],
                 [1,1,r,1,1],
                 [1,1,r,1,1],
               [1,49,r,49,1],
                 [1,1,r,1,1],
                 [1,1,r,1,1],
                 [1,1,r,1,1],
                 [1,1,r,1,1],
               [1,49,r,49,1],
                 [1,1,1,1,1]
                 ]
    for i in range(0,len(temp)):
        for j in range(0,5):
            mc.setBlock(15+j, 10+i, 15,temp[i][j])
    for k in range(num+1,len(temp)-4):
        mc.setBlock(15+2, 13+k,15,0)

if __name__=='__main__':
    SetBuild(12)
