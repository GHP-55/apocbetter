import time
import os
import serial

def serialcmdw():
    os.system('clear')
    serialcmd = input("serial command: ")
    ser.write(serialcmd.encode())
    serialcmdw()

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
time.sleep(1)
serialcmdw()
