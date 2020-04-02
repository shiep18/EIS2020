#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Autor:ZLL
import mcpi.minecraft as minecraft
import mcpi.block as block
from Command import *

def MoveIt(cmd):
    if cmd[0] == 'w':
        mc.player.setTilePos([pos.x + cmd[1], pos.y, pos.z])
    elif cmd[0] == 's':
        mc.player.setTilePos([pos.x - cmd[1], pos.y, pos.z])
    elif cmd[0] == 'a':
        mc.player.setTilePos([pos.x, pos.y, pos.z + cmd[1]])
    elif cmd[0] == 'd':
        mc.player.setTilePos([pos.x, pos.y, pos.z - cmd[1]])

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()#玩家位置，联机
Cmd=RecodeSound()
MoveIt(Cmd)








