from tkinter.ttk import*
from tkinter import*

from datetime import datetime
from time import sleep

from pygame import mixer


#window
window=Tk()
window.title("Clock")
window.geometry('350x200')




def sound_alarm():
    mixer.music.load('music.mp3')
    mixer.music.play()


def alarm():
    while True:
        control = 1
        print (control)
        alarm_hour ="10"
        alarm_min ="42"
        alarm_sec ="00"
        alarm_period ="PM".upper()

        now = datetime.now()

        hour = now.strftime("%I") 
        minute = now.strftime("%M")
        seconds =now.strftime("%S")
        period = now.strftime("%p")


        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_min == minute:
                        if alarm_sec == seconds:
                            print("Time to take break")
                            sound_alarm()
        sleep(1)            


mixer.init()
alarm()







window.mainloop()