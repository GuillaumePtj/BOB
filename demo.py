
############################################################################################################################################################################
# le but de ce code est d'executer des boucles for (aller retours) qui font tourner tout les moteurs en meme temps et effectuent tous une certaine rotation
# le code est basé sur la persistance rétinienne, chaque trame est envoyée pour chaque moteur, leur commandant de tourner de 1 degré chacun leur tour, 135 fois
#cette version demo procede a la séquence suivante : tout les moteurs font 135° aller-retours, pause de 2 secondes, tout les moteurs font 180° et plus pour le stepper
############################################################################################################################################################################


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

nmot = 1
angle = 1
dir = 0
vitesse = 1


while 1:
    # premiere position 
    for i in (135):
        
        angle = angle + 1
        nmot = 1    #+1 degré pour le moteur 1

        eb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()

        nmot = 2    #+1 degré pour le moteur 2

        deb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()
        
        nmot = 3    #+1 degré pour le moteur 3

        deb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()
        
        nmot = 4    #+1 degré pour le moteur 4

        deb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()

    # deuxieme position 
    for i in (135):
        
        dir = 1
        angle = angle - 1
        nmot = 1    #+1 degré pour le moteur 1

        eb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()

        nmot = 2    #+1 degré pour le moteur 2

        deb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()
        
        nmot = 3    #+1 degré pour le moteur 3

        deb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()
        
        nmot = 4    #+1 degré pour le moteur 4

        deb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()

    time.sleep(2)

    # troisieme position 
    for i in (180):
        
        angle = angle + 1
        nmot = 1    #+1 degré pour le moteur 1

        eb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()

        nmot = 2    #+1 degré pour le moteur 2

        deb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()
        
        nmot = 3    #+1 degré pour le moteur 3

        deb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()
        
        nmot = 4    #+1 degré pour le moteur 4

        deb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle + 1)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()

    # quatrieme position 
    for i in (180):
        
        dir = 1
        angle = angle - 1
        nmot = 1    #+1 degré pour le moteur 1

        eb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()

        nmot = 2    #+1 degré pour le moteur 2

        deb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()
        
        nmot = 3    #+1 degré pour le moteur 3

        deb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()
        
        nmot = 4    #+1 degré pour le moteur 4

        deb_trame =  np.uint16(65535)
        num_moteur = np.uint8(nmot)
        angle = np.uint16(angle + 1)
        sens = np.uint8(dir)
        vitesse = np.uint8(2)
        fin_trame =  np.uint16(65535)
        buffer = [(deb_trame>>8)&0xFF, (deb_trame&0xFF), num_moteur, (angle>>8)&0xFF, (angle&0xFF), sens, vitesse, (fin_trame>>8)&0xFF, (fin_trame&0xFF)]
        message = bytearray (buffer)
        print(message)

        ser.write(message)
        ser.flush()

    time.sleep(2)

ser.close()

