import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import RPi.GPIO as GPIO
import time
import requests

aux_vcc = 16
s2 = 5
s3 = 6
signal = 26
NUM_CYCLES = 10
#text = None
#text1 = None

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(aux_vcc, GPIO.OUT)
    GPIO.output(aux_vcc, GPIO.HIGH)
    GPIO.setup(s2, GPIO.OUT)
    GPIO.setup(s3, GPIO.OUT)
    print("\n")

def stopSensor():
    GPIO.cleanup()

def window(text, text1):
    #global text
    #global text1
    app = QApplication(sys.argv)
    widget = QWidget()
    textLabel = QLabel(widget)
    textLabel1 = QLabel(widget)
    textLabel.setText(text)
    textLabel.move(215, 140)
    textLabel1.setText(text1)
    textLabel1.move(125, 152)
    widget.setGeometry(0,0,480,320)
    widget.setWindowTitle("Welcome")
    widget.show()
    sys.exit(app.exec_())

#setup()

while True:
    if __name__ == '__main__':
        window("Welcome", "Please exhaust the cigarette bud and place it here")
        setup()
        GPIO.output(s2, GPIO.HIGH)
        GPIO.output(s3, GPIO.LOW)
        time.sleep(0.3)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            duration = time.time() - start
        val = NUM_CYCLES / duration
        print("value: ", val)
        window(val, val)
