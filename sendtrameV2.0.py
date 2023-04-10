import RPi.GPIO as GPIO 
import time
import serial
import sys
import array
import string
import numpy as np
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(33,GPIO.IN)
GPIO.setup(35,GPIO.OUT, initial=GPIO.LOW)

ser = serial.Serial("/dev/ttyAMA0", baudrate = 9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

def init ():
    GPIO.add_event_detect(33, GPIO.FALLING, callback=my_callback, bouncetime=300)
 
def my_callback(self):
    try:
        GPIO.output(35,GPIO.HIGH)
        time.sleep(1) 
        GPIO.output(35,GPIO.LOW)
        time.sleep(1)
        print("eh stop hein")
    except Exception as e:
            raise

if __name__ == "__main__":
    init()

while 1:
    Px = int(input("position en X : "))
    Py = int(input("position en Y : "))
    Pz = int(input("position en Z : "))
    Ox = int(input("orientation en X : "))
    Oy = int(input("orientation en Y : "))
    Oz = int(input("orientation en Z : "))

    deb_trame = np.uint16(65535)
    Position_x = np.uint16(Px)
    Position_y = np.uint16(Py)
    Position_z = np.uint16(Pz)
    Orientation_x = np.uint16(Ox)
    Orientation_y = np.uint16(Oy)
    Orientation_z = np.uint16(Oz)
    fin_trame =  np.uint16(65535)

    buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), (Position_x>>8)&0xFF, (Position_x&0xFF), (Position_y>>8)&0xFF, (Position_y&0xFF), (Position_z>>8)&0xFF, (Position_z&0xFF), (Orientation_x>>8)&0xFF, (Orientation_x&0xFF), (Orientation_y>>8)&0xFF, (Orientation_y&0xFF), (Orientation_z>>8)&0xFF, (Orientation_z&0xFF),(fin_trame>>8)&0xFF, (fin_trame&0xFF)]
    message = bytearray (buffer)
    print(message)

    ser.write(message)

    ser.flush()

ser.close()
