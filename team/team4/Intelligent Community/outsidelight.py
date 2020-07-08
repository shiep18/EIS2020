from mcpi.minecraft import Minecraft
import mcpi.block as block

mc=Minecraft.create("47.100.46.95",4784)
entityId= mc.getPlayerEntityId("W")

level = 1

#控制1号楼一楼灯亮
def OnLight1_1():
    #一楼右侧地灯亮
    mc.setBlock(1281,4,1182,169)
    #一楼左侧地灯亮
    mc.setBlock(1289,4,1183,169)
    #一楼左上侧灯亮
    mc.setBlock(1287,9,1185,169)
    #一楼右上侧灯亮
    mc.setBlock(1282,9,1186,169)

#控制1号楼一楼灯灭
def OffLight1_1():
    mc.setBlock(1281,4,1182,155,2)
    mc.setBlock(1289,4,1183,155,2)
    mc.setBlock(1287,9,1185,155,2)
    mc.setBlock(1282,9,1186,155,2)

#控制1号楼二楼灯亮   
def OnLight1_2():
    mc.setBlock(1286,15,1185,169)
    mc.setBlock(1286,15,1184,169)

#控制1号楼二楼灯灭    
def OffLight1_2():
    mc.setBlock(1286,15,1185,155,2)
    mc.setBlock(1286,15,1184,155,2)

#控制1号楼三楼灯亮    
def OnLight1_3():
    mc.setBlock(1286,21,1185,169)
    mc.setBlock(1286,21,1184,169)
    mc.setBlock(1285,21,1185,169)
    mc.setBlock(1285,21,1184,169)

#控制1号楼三楼灯灭 
def OffLight1_3():
    mc.setBlock(1286,21,1185,155,2)
    mc.setBlock(1286,21,1184,155,2)
    mc.setBlock(1285,21,1185,155,2)
    mc.setBlock(1285,21,1184,155,2)

#控制2号楼一楼灯亮
def OnLight2_1():
    mc.setBlock(1213,4,1184,169)
    mc.setBlock(1205,4,1184,169)
    mc.setBlock(1211,9,1187,169)
    mc.setBlock(1207,9,1187,169)

#控制2号楼一楼灯灭
def OffLight2_1():
    mc.setBlock(1213,4,1184,155,2)
    mc.setBlock(1205,4,1184,155,2)
    mc.setBlock(1211,9,1187,155,2)
    mc.setBlock(1207,9,1187,155,2)

#控制2号楼二楼灯亮   
def OnLight2_2():
    mc.setBlock(1212,15,1184,169)
    mc.setBlock(1209,15,1187,169)
    mc.setBlock(1206,15,1185,169)

#控制2号楼二楼灯灭    
def OffLight2_2():
    mc.setBlock(1212,15,1184,155,2)
    mc.setBlock(1209,15,1187,155,2)
    mc.setBlock(1206,15,1185,155,2)

#控制2号楼三楼灯亮    
def OnLight2_3():
    mc.setBlock(1209,21,1185,169)
    mc.setBlock(1210,21,1185,169)
    mc.setBlock(1209,21,1184,169)
    mc.setBlock(1210,21,1184,169)

#控制2号楼三楼灯灭 
def OffLight2_3():
    mc.setBlock(1209,21,1185,155,2)
    mc.setBlock(1210,21,1185,155,2)
    mc.setBlock(1209,21,1184,155,2)
    mc.setBlock(1210,21,1184,155,2)
    

def lightctrl():
    pos=mc.entity.getTilePos(entityId)
    if pos.y ==4:
        OffLight1_1()
        OffLight1_2()
        OffLight1_3()
        OffLight2_1()
        OffLight2_2()
        OffLight2_3()
    #控制1号楼
    if pos.x>=1281 and pos.x<=1289 and pos.z>=1179 and pos.z<=1188 and pos.y >=5 and pos.y <9:
        level = 1
        if level == 1:
            OnLight1_1()
            OffLight1_2()
            OffLight1_3()
            level = 10
    if pos.x>=1281 and pos.x<=1289 and pos.z>=1179 and pos.z<=1188 and pos.y >=9 and pos.y <15 :
        level = 2
        if level == 2:
            OffLight1_1()
            OnLight1_2()
            OffLight1_3()
            level = 10
    if pos.x>=1281 and pos.x<=1289 and pos.z>=1179 and pos.z<=1188 and pos.y >=15:
        level = 3
        if level == 3:
            OffLight1_1()
            OffLight1_2()
            OnLight1_3()
            level = 10
    #控制二号楼        
    if pos.x>=1205 and pos.x<=1213 and pos.z>=1178 and pos.z<=1188 and pos.y >=5 and pos.y <9:
        level = 1
        if level == 1:
            OnLight2_1()
            OffLight2_2()
            OffLight2_3()
            level = 10
    if pos.x>=1205 and pos.x<=1213 and pos.z>=1178 and pos.z<=1188 and pos.y >=9 and pos.y <15 :
        level = 2
        if level == 2:
            OffLight2_1()
            OnLight2_2()
            OffLight2_3()
            level = 10
    if pos.x>=1205 and pos.x<=1213 and pos.z>=1178 and pos.z<=1188 and pos.y >=15:
        level = 3
        if level == 3:
            OffLight2_1()
            OffLight2_2()
            OnLight2_3()
            level = 10
    
        

