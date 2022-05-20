# import datetime
# initial = datetime.datetime.today()
# print(initial.strftime("%%d/%m/%y | %I:%M %p"))
# tdelta=datetime.timedelta(minutes=30)
# # print(tdelta)
# print(initial+tdelta)
from datetime import datetime
from time import time
from pygame import mixer
def music(file,stopper):
    mixer.init()
    mixer.music.load(f"{file}.mp3")
    mixer.music.play(loops=-1)
    while True:
        x=str(input())
        if stopper==x:
            logs(file)
            mixer.music.stop()
            mixer.music.unload()
            break
def logs(msg):
    with open("log.txt","a") as f:
        f.write(f"{datetime.now().strftime('%d/%m/%y | %H:%M')}  :  {msg} \n")
water_init=time()
eyes_init=time()
exer_init=time()
while True:
    if time()-water_init>23*60:
        print("Please drink water and then type wdone to stop music")
        music("water","wdone")
        water_init=time()
    
    if time()-eyes_init>29*60:
        print("Get your eyes relaxed and then type edone to stop music")
        music("eyes","edone")
        eyes_init=time()
    
    if time()-exer_init>43*60:
        print("Stand up and stretch your body and then type exdone to stop music")
        music("exercise","exdone")
        exer_init=time()
    