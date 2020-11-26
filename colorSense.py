import RPi.GPIO as GPIO
import time
import tkinter as tk
import tkinter.font as tkFont

red = None
blue = None
green = None

root = None
dfont = None
frame = None

fullscreen = False

aux_vcc = 16
s2 = 5
s3 = 6
signal = 26
NUM_CYCLES = 10

root = tk.Tk()
root.title("Sensor Value")
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(aux_vcc, GPIO.OUT)
    GPIO.output(aux_vcc, GPIO.HIGH)
    GPIO.setup(s2, GPIO.OUT)
    GPIO.setup(s3, GPIO.OUT)
    print("\n")

def toggle_fullscreen():
    global root
    global fullscreen

    fullscreen = not fullscreen
    root.attributtes('-fullscreen', fullscreen)
    resize()

def end_fullscreen(event=None):
    global root
    global fullscreen
    fullscreen = False
    root.attributes('-fullscreen', False)
    resize()

def resize():
    global dfont
    global frame
    new_size = -max(12, int((frame.winfo_height() / 10)))
    dfont.configure(size=new_size)

def loop():
    global red
    global blue
    global green
    temp = 1
    while(1):
        GPIO.output(s2, GPIO.LOW)
        GPIO.output(s3, GPIO.LOW)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        red = NUM_CYCLES / duration
        #print("red value: ", red)

        GPIO.output(s2, GPIO.LOW)
        GPIO.output(s3, GPIO.HIGH)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        blue = NUM_CYCLES / duration
        #print("blue value: ", blue)

        GPIO.output(s2, GPIO.HIGH)
        GPIO.output(s3, GPIO.HIGH)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        green = NUM_CYCLES / duration
        #print("green value: ", green)
        time.sleep(2)
        
        red = tk.DoubleVar()
        green = tk.DoubleVar()
        blue = tk.DoubleVar()

def endprogram():
    GPIO.cleanup()

if __name__=='__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        endprogram()
