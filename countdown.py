from tkinter import *
import time

t = None

def count(y):
    global t
    #s = 60
    while t:
        mins, sec = divmod(int(t), 60)
        timer = '{:02d}:{:02d}'.format(mins, sec)
        print(timer, end="\r")
        time.sleep(1)
        #print(t)
        t = int(t)
        t -= 1
    print("Fire in the whole")

t = input("Enter the time in Secinds: ")
count(int(t))
