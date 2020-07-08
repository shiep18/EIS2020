import baidusound as bd
from mcpi.minecraft import Minecraft




def coordinate_detection():
    mc=Minecraft.create("47.100.46.95",4784)
    entityId= mc.getPlayerEntityId("W")
    pos=mc.entity.getTilePos(entityId)
    x=pos.x
    y=pos.y
    z=pos.z


    if 1186<=z<=1191:
        #1号楼1,3,5,用户
        if 1291<=x<=1295:
            if y==5:
                print("1号楼101用户：")
                bd.record()
                result=bd.w2p()
                if "开" in result:
                    mc.setBlock(1293,9,1188,169)
                    print("灯已打开!")
                if "关" in result:
                    mc.setBlock(1293,9,1188,1)
                    print("灯已关闭!")
            if y==11:
                print("1号楼201用户：")
                bd.record()
                result=bd.w2p()
                if "开" in result:
                    mc.setBlock(1293,15,1188,169)
                    print("灯已打开!")
                if "关" in result:
                    mc.setBlock(1293,15,1188,1)
                    print("灯已关闭!")
            if y==17:
                print("1号楼301用户：")
                bd.record()
                result=bd.w2p()
                if "开" in result:
                    mc.setBlock(1293,21,1188,169)
                    print("灯已打开!")
                if "关" in result:
                    mc.setBlock(1293,21,1188,1)
                    print("灯已关闭!")
        #1号楼2,4,6用户
        if 1273<=x<=1279:
            if y==5:
                print("1号楼102用户：")
                bd.record()
                result=bd.w2p()
                if "开" in result:
                    mc.setBlock(1276,9,1189,169)
                    print("灯已打开!")
                if "关" in result:
                    mc.setBlock(1276,9,1189,1)
                    print("灯已关闭!")
            if y==11:
                print("1号楼202用户：")
                bd.record()
                result=bd.w2p()
                if "开" in result:
                    mc.setBlock(1276,15,1189,169)
                    print("灯已打开!")
                if "关" in result:
                    mc.setBlock(1276,15,1189,1)
                    print("灯已关闭!")
            if y==17:
                print("1号楼302用户：")
                bd.record()
                result=bd.w2p()
                if "开" in result:
                    mc.setBlock(1276,21,1189,169)
                    print("灯已打开!")
                if "关" in result:
                    mc.setBlock(1276,21,1189,1)
                    print("灯已关闭!")
        #2号楼7,9,11用户
        if 1215<=x<=1219:
            if y==5:
                print("2号楼101用户：")
                bd.record()
                result=bd.w2p()
                if "开" in result:
                    mc.setBlock(1217,9,1188,169)
                    print("灯已打开!")
                if "关" in result:
                    mc.setBlock(1217,9,1188,1)
                    print("灯已关闭!")
            if y==11:
                print("2号楼201用户：")
                bd.record()
                result=bd.w2p()
                if "开" in result:
                    mc.setBlock(1217,15,1188,169)
                    print("灯已打开!")
                if "关" in result:
                    mc.setBlock(1217,15,1188,1)
                    print("灯已关闭!")
            if y==17:
                print("2号楼301用户：")
                bd.record()
                result=bd.w2p()
                if "开" in result:
                    mc.setBlock(1217,21,1188,169)
                    print("灯已打开!")
                if "关" in result:
                    mc.setBlock(1217,21,1188,1)
                    print("灯已关闭!")
        #2号楼8,10,12用户
        if 1197<=x<=1203:
            if y==5:
                print("2号楼102用户：")
                bd.record()
                result=bd.w2p()
                if "开" in result:
                    mc.setBlock(1200,9,1189,169)
                    print("灯已打开!")
                if "关" in result:
                    mc.setBlock(1200,9,1189,1)
                    print("灯已关闭!")
            if y==11:
                print("2号楼202用户：")
                bd.record()
                result=bd.w2p()
                if "开" in result:
                    mc.setBlock(1200,15,1189,169)
                    print("灯已打开!")
                if "关" in result:
                    mc.setBlock(1200,15,1189,1)
                    print("灯已关闭!")
            if y==17:
                print("2号楼302用户：")
                bd.record()
                result=bd.w2p()
                if "开" in result:
                    mc.setBlock(1200,21,1189,169)
                    print("灯已打开!")
                if "关" in result:
                    mc.setBlock(1200,21,1189,1)
                    print("灯已关闭!")
        
    

