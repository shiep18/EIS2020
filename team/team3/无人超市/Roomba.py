from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc=Minecraft.create("47.100.46.95",4783)
entityId= mc.getPlayerEntityId("fhz")
p=1
k=0
while True:
    f = open(r"C:\Users\Administrator.PC-20170611QCUM\Desktop\test\111.txt",'r')
    b = f.read()
    ##a=b[0]
    f.close() 
    while b=='True':
        f = open(r"C:\Users\Administrator.PC-20170611QCUM\Desktop\test\111.txt",'r')
        b = f.read()
        #a=b[0]
        f.close()
        pos=mc.entity.getTilePos(entityId)
        blockId=mc.getBlock(pos.x+1,pos.y,pos.z)
        blockId1=mc.getBlock(pos.x,pos.y,pos.z+1)
        blockId2=mc.getBlock(pos.x-1,pos.y,pos.z)
        #print(blockId1)
        
        blockId3=mc.getBlock(pos.x,pos.y,pos.z-1)
        #blockId4=mc.getBlock(pos.x+1,pos.y,pos.z+1)
        #blockId5=mc.getBlock(pos.x-1,pos.y,pos.z-1)

        if pos.z>=141:
            pos=mc.entity.getTilePos(entityId)
            mc.player.setTilePos(pos.x,pos.y,pos.z-1)
            time.sleep(0.2)
            print(pos)
            if pos.x>=83:
                k=-1
                p=0
            if pos.x<83:
                k=1
                p=0
                    
        if pos.z<=87:
            pos=mc.entity.getTilePos(entityId)
            mc.player.setTilePos(pos.x,pos.y,pos.z+1)
            time.sleep(0.2)
            if pos.x>=83:
                k=-1
                p=0
            if pos.x<83:
                k=1
                p=0

        if pos.x<=43:
            pos=mc.entity.getTilePos(entityId)
            mc.player.setTilePos(pos.x+1,pos.y,pos.z)
            time.sleep(0.2)
            if pos.z>=115:
                k=0
                p=-1
            if pos.z<115:
                k=0
                p=1
           
        if pos.x>=119:
            pos=mc.entity.getTilePos(entityId)
            mc.player.setTilePos(pos.x-1,pos.y,pos.z)
            time.sleep(0.2)
            if pos.z>=115:
                k=0
                p=-1
            if pos.z<115:
                k=0
                p=1
                
                

    ####################
        if k==0 and p==1:
            #left corner
            if blockId!=0 and blockId1!=0:
                for i in range(2):
                    mc.player.setTilePos(pos.x-1,pos.y,pos.z)
                    time.sleep(0.2)

            #right corner
            if blockId2!=0 and blockId1!=0:
                for i in range(2):
                    mc.player.setTilePos(pos.x+1,pos.y,pos.z)
                    time.sleep(0.2)

            #common        
            if blockId1!=0 and blockId==0 and blockId2==0:
                for i in range(2):
                    mc.player.setTilePos(pos.x+1,pos.y,pos.z)
                    time.sleep(0.2)
            if blockId1==0:
                pos=mc.entity.getTilePos(entityId)
                mc.player.setTilePos(pos.x+k,pos.y,pos.z+p)
                time.sleep(0.2)
    ################################
        if k==0 and p==-1:
            #left corner
            if blockId2!=0 and blockId3!=0:
                for i in range(2):
                    mc.player.setTilePos(pos.x+1,pos.y,pos.z)
                    time.sleep(0.2)

            #right corner
            if blockId!=0 and blockId3!=0:
                for i in range(2):
                    mc.player.setTilePos(pos.x-1,pos.y,pos.z)
                    time.sleep(0.2)

            #common        
            if blockId3!=0 and blockId==0 and blockId2==0:
                if pos.x>=80:
                    for i in range(2):
                        mc.player.setTilePos(pos.x-1,pos.y,pos.z)
                        time.sleep(0.2)
                if pos.x<80:
                    for i in range(2):
                        mc.player.setTilePos(pos.x+1,pos.y,pos.z)
                        time.sleep(0.2)
                
            if blockId3==0:
                pos=mc.entity.getTilePos(entityId)
                mc.player.setTilePos(pos.x+k,pos.y,pos.z+p)
                time.sleep(0.2)

    ################################                
        if k==1 and p==0:
            #left corner
            
            if blockId!=0 and blockId3!=0:
                for i in range(2):
                    mc.player.setTilePos(pos.x,pos.y,pos.z+1)
                    time.sleep(0.2)

             #right corner
            if blockId1!=0 and blockId!=0:
                for i in range(2):
                    mc.player.setTilePos(pos.x,pos.y,pos.z-1)
                    time.sleep(0.2)

            #common        
            if blockId!=0 and blockId1==0 and blockId3==0:
                for i in range(2):
                    mc.player.setTilePos(pos.x,pos.y,pos.z+1)
                    time.sleep(0.2)
            if blockId==0:
                pos=mc.entity.getTilePos(entityId)
                mc.player.setTilePos(pos.x+k,pos.y,pos.z+p)
                time.sleep(0.2)

            ###########################
        if k==-1 and p==0:

              #left corner
            if blockId1!=0 and blockId2!=0:
                for i in range(2):
                    mc.player.setTilePos(pos.x,pos.y,pos.z-1)
                    time.sleep(0.2)
                for j in range(2):
                    mc.player.setTilePos(pos.x-1,pos.y,pos.z)
                    time.sleep(0.2)
             #right corner
            if blockId2!=0 and blockId3!=0:
                for i in range(2):
                    mc.player.setTilePos(pos.x,pos.y,pos.z+1)
                    time.sleep(0.2)

            #common        
            if blockId2!=0 and blockId1==0 and blockId3==0:
                if pos.z<110:
                    for i in range(2):
                        mc.player.setTilePos(pos.x,pos.y,pos.z+1)
                        time.sleep(0.2)
                if pos.z>=110:
                    for i in range(2):
                        mc.player.setTilePos(pos.x,pos.y,pos.z-1)
                        time.sleep(0.2)
            if blockId2==0:
                pos=mc.entity.getTilePos(entityId)
                mc.player.setTilePos(pos.x+k,pos.y,pos.z+p)
                time.sleep(0.2)
                    
            
    
    

        

