import RPi.GPIO as GPIO
import time
import tkinter as tk
import tkinter.font as tkFont

#Declare Global Variables
root = None
dfont = None
frame = None
msg = None
value = None
aux_vcc = 16
s2 = 5
s3 = 6
signal = 26
NUM_CYCLES = 10

#Fulscreen or windowed
fullscreen = False

#toggle fullscreen
def toggle_fullscreen(event=None):
    global root
    global fullscreen
    fullscreen = not fullscreen
    root.attributes('-fullscreen', fullscreen)
    resize()

#go into windowed mode
def end_fullscreen(event=None):
    global root
    global fullscreen
    fullscreen = False
    root.attributes('-fullscreen', False)
    resize()

#resize font based on screen size
def resize(event=None):
    global dfont
    global frame
    new_size = -max(12, int((frame.winfo_height() / 10)))
    dfont.configure(size=new_size)

def setup():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(aux_vcc, GPIO.OUT)
    GPIO.output(aux_vcc, GPIO.HIGH)
    GPIO.setup(s2, GPIO.OUT)
    GPIO.setup(s3, GPIO.OUT)
    print("\n")

def endprogram():
    GPIO.cleanup()

def loop():
    temp = 1
    global root
    global value
    global msg
    try:
        GPIO.output(s2, GPIO.HIGH)
        GPIO.output(s3, GPIO.LOW)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        val = NUM_CYCLES / duration
        value.set(val)
        print("value: ", val)
        if val > 6500:
            print("Cigarette Bud Detected")
            msge="Cigarette bud\nDetectedd"
            msg.set(msge)
        else:
            print("Place the Cigarette")
            msge="Place the\nCigarette"
            msg.set(msge)
    except KeyboardInterrupt:
        endprogram()

    root.after(500, loop)
#create the window
root = tk.Tk()
root.title("Cigarette Bud Crusher: BioCrux")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

value = tk.DoubleVar()
msg = tk.StringVar()

dfont = tkFont.Font(size=-24)

label_color = tk.Label(frame, text="Value", font=dfont)
label_value = tk.Label(frame, textvariable=value, font=dfont)
label_space = tk.Label(frame, text=" ", font=dfont)
label_msg = tk.Label(frame, textvariable=msg, font=dfont)

label_color.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
label_value.grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)
label_space.grid(row=0, column=2, padx=5, pady=5)
label_space.grid(row=1, column=0, padx=5, pady=5)
label_msg.grid(row=1, column=1, padx=5, pady=5)
label_space.grid(row=1, column=2, padx=5, pady=5)
label_space.grid(row=2, column=1, padx=5, pady=5)

for i in range(0,3):
    frame.rowconfigure(i, weight=1)
for i in range(0,3):
    frame.columnconfigure(i, weight=1)

root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', end_fullscreen)

root.bind('<Configure>', resize)

setup()

root.after(500, loop)

toggle_fullscreen()
root.mainloop()
