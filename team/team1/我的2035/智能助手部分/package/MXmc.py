from mcpi.minecraft import Minecraft
import time


print("MXMc")

class MXMc():
    def __init__(self):
        self.follow_flag = False


    def creat(self, address="localhost", port=4711):
        Minecraft.create(address, port)

