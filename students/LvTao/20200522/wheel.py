class wheel():
    def __init__(self):
        self.spd=0
    def setcolor():
        print("I will set color")
    def setspeed(self,spd):
        self.spd=spd
        print("I will run on speed",spd)
    def run(self):
       print("runing on speed",self.spd)

wheels=[]

for i in range(4):
    wheelnew=wheel()
    wheelnew.setspeed(i*10+100)
    wheels.append(wheelnew)

print(wheels)

for wheel in wheels:
    wheel.run()
