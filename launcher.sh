#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/apocbetter
echo 'I CDed'
DISPLAY=:0 python3 main.py
echo 'I PYTHONED'
exit

# Do not touch, if you fuck this up I will find you
