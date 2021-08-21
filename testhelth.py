print("Healthy Programmer")
from pygame import mixer
mixer.init()
mixer.music.load("song2.wav")
mixer.music.set_volume(0.7)

def func1():
    while True:
        print("TIME TO DRINK WATER")
        print("Type Drank to stop alarm and Drink water")
        mixer.music.play()
        pani=input("")
        wata=8

        if pani=="Drank":
            f=open('water.mp3', "a")
            f.write(pani)
            f.close()
            mixer.music.pause()
        break
def func2():
    while True:
        print("TIME TO Do exercise")
        print("Type Exdone to stop alarm and Do something")
        mixer.music.play()
        exercise=input("")
        if exercise=="Exdone":
            f=open("Exdone","w")
            f.write(exercise)
            f.close()
            mixer.music.pause()
        break
def func3():
    while True:
        print("TIME TO Do Eye exercise")
        print("Type Eydone to stop alarm and Do something")
        mixer.music.play()
        eyeexercise=input("")
        if eyeexercise=="Eydone":
            f=open("Eyeexercise","w")
            f.write(eyeexercise)
            f.close()
            mixer.music.pause()
        break
while True:
    chance=3
    import time
    for i in range(chance):
        time.sleep(4)
        if func1()==i:
            func1()
            break
        exercc = 4
        import time
        time.sleep(10)
        for sham in range(exercc):
            time.sleep(10)
            if func2()==sham:
                func2()
                break
        eyess = 3
        import time
        time.sleep(13)
        for ram in range(eyess):
            time.sleep(4)
            if func3()==ram:
                func3()
                break
        break