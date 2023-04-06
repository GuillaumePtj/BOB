import RPi.GPIO as GPIO
import time
import serial
import sys
import array
import string
import numpy as np
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(13,GPIO.IN)

ser = serial.Serial("/dev/ttyAMA0", 
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1)


while 1:
    
    nmot = int(input("moteur n°: "))
    angle = int(input("angle: "))
    if angle == 0 :
        break
    dir = int(input("dir : "))
    vitesse = int(input("vitesse: "))

    deb_trame =  np.uint16(65535)
    num_moteur = np.uint8(nmot)
    angle = np.uint16(angle)
    sens = np.uint8(dir)
    vitesse = np.uint8(vitesse)
    fin_trame =  np.uint16(65535)

    buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
    message = bytearray (buffer)
    print(message)

    ser.write(message)

    ser.flush()
ser.close()