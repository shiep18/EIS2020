from mcpi.minecraft import Minecraft

def get_light_state():
    mc=Minecraft.create("47.100.46.95",4784)
    entityId= mc.getPlayerEntityId("W")
    room=[]
    A=str(mc.getBlock(1293,9,1188))#1
    B=str(mc.getBlock(1276,9,1189))#2
    C=str(mc.getBlock(1293,15,1188))#3
    D=str(mc.getBlock(1276,15,1189))#4
    E=str(mc.getBlock(1293,21,1188))#5
    F=str(mc.getBlock(1276,15,1189))#6
    G=str(mc.getBlock(1217,9,1188))#7
    H=str(mc.getBlock(1200,9,1189))#8
    I=str(mc.getBlock(1217,15,1188))#9
    J=str(mc.getBlock(1200,15,1189))#10
    K=str(mc.getBlock(1217,21,1188))#11
    L=str(mc.getBlock(1200,21,1189))#12
    room=[A,B,C,D,E,F,G,H,I,J,K,L]
    #print(room)
    f=open(r'C:\Users\23004\AppData\Roaming\.homeassistant\custom_components\light_state.txt','w')
    for i in range(len(room)):
        s = str(room[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        #print(s)
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        #print(s)
        f.write(s)
    f.close()
    

        
