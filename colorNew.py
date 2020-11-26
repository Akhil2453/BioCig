import RPi.GPIO as GPIO
import time
import tkinter as tk
import tkinter.font as tkFont
import requests

#Declare Global Variables
root = None
dfont = None
welcome = None
budDetect = None
thankYou = None
msg = None
value = None
number = None
aux_vcc = 16
s2 = 5
s3 = 6
signal = 26
NUM_CYCLES = 10

#Fulscreen or windowed
fullscreen = False

def number():
    global number
    global num
    try:
        num = number.get()
        number.set(num)
        print(num)
        #return num
        para = {'action': 'saveUserData', 'MOB': num, 'MCID': '002000244', 'BTNO': '10'}
        r = requests.post("http://clickcash.in/apisave/apiDataSavever2.php", data=para)
        print(r.text)
        time.sleep(15)
    except:
        pass

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
    global welcome
    new_size = -max(12, int((welcome.winfo_height() / 10)))
    dfont.configure(size=new_size)

def setup():
    #GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(aux_vcc, GPIO.OUT)
    GPIO.output(aux_vcc, GPIO.HIGH)
    GPIO.setup(s2, GPIO.OUT)
    GPIO.setup(s3, GPIO.OUT)
    print("\n")

def endprogram():
    GPIO.cleanup()

def newFrame():
    number = tk.IntVar()
    tk.Entry(budDetect, width=30, textvariable=number).pack()
    tk.Button(budDetect, text="Finish", command=number).pack()
    time.sleep(10)

def loop():
    temp = 1
    global root
    global value
    global msg
    global number
    global num
    #try:
    #GPIO.setmode(GPIO.BCM)
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
    if val > 5600:
       print("Cigarette Bud Detected")
       msge="Cigarette bud\nDetectedd"
       msg.set(msge)
       newFrame()
       #num = number(
       
       #for i in range(0,2000):
       #    temp = temp + 1
       #    print(temp)
        #param = {'action': 'saveUserData', 'MOB': num, 'MCID': '002000244', 'BTNO': '10'}
        #r = requests.post("http://clickcash.in/apisave/apiDataSavever2.php", data=param)
        #print(r.text)
    else:
        print("Place the Cigarette")
        msge="Place the\nCigarette"
        msg.set(msge)
#   except KeyboardInterrupt:
#      endprogram()
    root.after(500, loop)

root = tk.Tk()
root.title("Cigarette Bud Crusher: BioCrux")

welcome = tk.Frame(root)
budDetect = tk.Frame(root)
thankYou = tk.Frame(root)

welcome.pack(fill=tk.BOTH, expand=1)
budDetect.pack(fill=tk.BOTH, expand=1)
thankYou.pack(fill=tk.BOTH, expand=1)

value = tk.DoubleVar()
msg = tk.StringVar()
number = tk.IntVar()

dfont = tkFont.Font(size=-24)

label_space = tk.Label(welcome, text=" ", font=dfont)
label_value = tk.Label(welcome, text="Welcome to Biocrux Cigarette Zone.\n Please extinguish and drop your Cigarette bud here", font=dfont)
label_msg = tk.Label(welcome, textvariable=msg, font=dfont)

label_space.grid(row=0, column=1, padx=5, pady=5)
label_value.grid(row=1, column=1, padx=0, pady=0)
label_msg.grid(row=2, column=1, padx=0, pady=0)



for i in range(0,3):
    welcome.rowconfigure(i, weight=1)
    budDetect.rowconfigure(i, weight=1)
    thankYou.rowconfigure(i, weight=1)
for i in range(0,3):
    welcome.columnconfigure(i, weight=1)
    budDetect.columnconfigure(i, weight=1)
    thankYou.columnconfigure(i, weight=1)

root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', end_fullscreen)

root.bind('<Configure>', resize)

setup()

root.after(1000, loop)

toggle_fullscreen()

root.mainloop()