import mcpi.minecraft as minecraft
import mcpi.block as block
from HouseClass import *
from CsvToHouse import *
mc = minecraft.Minecraft.create()
mc.setBlock(17, 9, 20,1)
mc.player.setTilePos([17,10,20])
house=ReadCsv()
for i in range(0,len(house)):
    house[i][0]=House(house[i][0],house[i][1],house[i][2],house[i][3],house[i][4],house[i][5],house[i][6])
    house[i][0].SetHouse()
    house[i][0].getHouseMessage()
    
while True:
    for i in range(0,len(house)):
        pos=mc.player.getTilePos()
        house[i][0].InsideHouse(pos.x,pos.y,pos.z)
