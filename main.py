import pygame  # load pygame keywords
import sys     # let  python use your file system
import os      # help python identify your OS
import random
import serial
import struct

'''
Global Variables
'''

clicks = 0
STATE = 0 # [ 0: Menu, 1: Level 1 ... 10: Score / Credits]

'''
Objects
'''

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def restart():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]

def action():
    main = False

def redup():
    if C[0] < 250:
        C[0] = C[0] + 10
    elif C[0] == 250:
        C[0] = 254

def greenup():
    if C[1] < 250:
        C[1] = C[1] + 10
    elif C[1] == 250:
        C[1] = 254

def blueup():
    if C[2] < 250:
        C[2] = C[2] + 10
    elif C[2] == 250:
        C[2] = 254

def reddown():
    if C[0] >= 10:
        C[0] = C[0] - 10
    if (C[0] % 10) != 0:
        C[0] = C[0] - 4

def greendown():
    if C[1] >= 10:
        C[1] = C[1] - 10
    if (C[1] % 10) != 0:
        C[1] = C[1] - 4

def bluedown():
    if C[2] >= 10:
        C[2] = C[2] - 10
    if (C[2] % 10) != 0:
        C[2] = C[1] - 4

def cclear():
    C[0] = 0
    C[1] = 0
    C[2] = 0

'''
Setup
'''

main = True

BLUE  = (25,25,200)
BLACK = (23,23,23 )
WHITE = (254,254,254)
RED = (200, 25, 25)
GREEN = (25, 200, 25)

C = [ 0, 0, 0]
COLOR = ( C[0], C[1], C[2] )

K = {
    273 : redup , # Up / 2
    274 : reddown , # Down / 3
    276 : greendown , # Left / 4
    275 : greenup , # Right / 5
    97 : restart , # A / 6
    49 : blueup , # 1 / 7
    50 : bluedown , # 2 / 6
    51 : action , # 3 / 6
    52 : action , # 4 / 6
    53 : cclear , # 5 / 6
    54 : action , # 6 / 6
    55 : action , # 7 / 6
    56 : action , # 8 / 6
    57 : action , # 9 / 6
}

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

szero = '0'
ser.write(szero.encode())

# Game Dimentions
gamex = 1080
gamey = 1920

# Pygame Setup
fps   = 40  # frame rate
ani   = 1   # animation cycles
clock = pygame.time.Clock()
pygame.init()

# Backgroud
world = pygame.display.set_mode([gamex,gamey],pygame.FULLSCREEN)

# Disable Mouse
pygame.mouse.set_visible(False)

'''
Main Loop
'''
while main:

    # Event Handler

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in K.keys():
                K[event.key]()
                print(COLOR)
                print( str(event.key) + ' was pressed')
            else:
                print( str(event.key) + ' is not in dictionary')

    COLOR = ( C[0], C[1], C[2] )
    world.fill(COLOR)

    # Tick Handler
    pygame.display.flip()
    clock.tick(fps)
