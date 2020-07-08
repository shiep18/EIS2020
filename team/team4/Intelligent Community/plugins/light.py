import requests
import os
import random
from threading import Thread
import mcpi.minecraft as minecraft
import time

from robot.sdk.AbstractPlugin import AbstractPlugin


class Plugin(AbstractPlugin):
    SLUG = "light"
    
    def __init__(self,SKILL):
        self.mc=minecraft.Minecraft.create('47.100.46.95',4784)

    def floor1_restaurant(self, query):
        if '开' in query:
            self.mc.setBlock(1226,8,1240,169)
            self.mc.setBlock(1229,8,1240,169)
            self.mc.setBlock(1232,8,1240,169)
        elif '关' in query:
            self.mc.setBlock(1226,8,1240,1)
            self.mc.setBlock(1229,8,1240,1)
            self.mc.setBlock(1232,8,1240,1)
            
    def floor1_carbarn(self, query):
        if '开' in query:
            self.mc.setBlock(1244,7,1240,169)
            self.mc.setBlock(1247,7,1240,169)
            self.mc.setBlock(1250,7,1240,169)
        elif '关' in query:
            self.mc.setBlock(1244,7,1240,1)
            self.mc.setBlock(1247,7,1240,1)
            self.mc.setBlock(1250,7,1240,1)

    def floor2_living_room(self, query):
        if '开' in query:
            self.mc.setBlock(1231,13,1240,169)
            self.mc.setBlock(1234,13,1240,169)
        elif '关' in query:
            self.mc.setBlock(1231,13,1240,1)
            self.mc.setBlock(1234,13,1240,1)

    def floor2_corridor(self, query):
        if '开' in query:
            self.mc.setBlock(1239,13,1243,169)
        elif '关' in query:
            self.mc.setBlock(1239,13,1243,1)
            
    def floor2_bedroom(self, query):
        if '开' in query:
            self.mc.setBlock(1243,12,1242,169)
            self.mc.setBlock(1243,12,1236,169)
            self.mc.setBlock(1248,12,1239,169)
            self.mc.setBlock(1253,12,1236,169)
            self.mc.setBlock(1253,12,1242,169)
        elif '关' in query:
            self.mc.setBlock(1243,12,1242,1)
            self.mc.setBlock(1243,12,1236,1)
            self.mc.setBlock(1248,12,1239,1)
            self.mc.setBlock(1253,12,1236,1)
            self.mc.setBlock(1253,12,1242,1)

    def floor3(self, query):
        if '开' in query:
            self.mc.setBlock(1234,19,1237,169)
            self.mc.setBlock(1234,19,1241,169)
            self.mc.setBlock(1238,19,1237,169)
            self.mc.setBlock(1243,19,1237,169)
            self.mc.setBlock(1243,19,1242,169)
            self.mc.setBlock(1238,19,1243,169)
        elif '关' in query:
            self.mc.setBlock(1234,19,1237,1)
            self.mc.setBlock(1234,19,1241,1)
            self.mc.setBlock(1238,19,1237,1)
            self.mc.setBlock(1243,19,1237,1)
            self.mc.setBlock(1243,19,1242,1)
            self.mc.setBlock(1238,19,1243,1)
        
    def handle(self, query):
        if "餐厅" in query:
            self.floor1_restaurant(query)
        elif "车库" in query:
            self.floor1_carbarn(query)
        elif "客厅" in query:
            self.floor2_living_room(query)
        elif "卧室" in query:
            self.floor2_bedroom(query)
        elif "三楼" in query:
            self.floor3(query)
        elif "走廊" in query:
            self.floor2_corridor(query)
        elif "关灯" in query or "开灯" in query:
            self.floor1_restaurant(query)
            self.floor1_carbarn(query)
            self.floor2_living_room(query)
            self.floor2_bedroom(query)
            self.floor3(query)
            self.floor2_corridor(query)
            
        return None

    def isValid(self, query):
        return any(word in query for word in ["开", "灯","关"])
