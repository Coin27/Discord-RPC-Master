#------------------------------------
from pypresence import Presence 
from time import sleep
import os
import sys,time
import psutil
#------------------------------------
l_image = "IMAGE NAME HERE"

s_image = "IMAGE NAME HERE"

l_image2 = "IMAGE NAME HERE"

s_image2 = "IMAGE NAME HERE"

l_text = "TEXT HERE"

s_text = "TEXT HERE"

l_text2 = "TEXT HERE"

s_text2 = "TEXT HERE"

time1 = "status change time here"
#------------------------------------
btns = [
    {
        "label": "BUTTON TEXT HERE",
        "url": "URL HERE"
    },
    {
        "label": "BUTTON TEXT HERE",
        "url": "URL HERE"
    }
]
#------------------------------------
os.system('color 1f')
RPC = Presence("800295255916150816")
#------------------------------------
print("█▀▀ █░░ █ █▀█ ▀█▀ █▀▀ ▄▀█ █▀▄▀█  █▀█ █▀█ █▀▀")
print("█▀░ █▄▄ █ █▀▀ ░█░ ██▄ █▀█ █░▀░█  █▀▄ █▀▀ █▄▄")
sleep(1)
#------------------------------------
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.001)
print_slow("--------------------------------------------------------------------------------")
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.06)
print_slow("\nСделано Coin collect27#1234 | Программа активирована без ошибок.")
#------------------------------------
RPC.connect()
while True:
    sleep(time1)
    RPC.update(
    state=l_text,
    details=s_text,
    buttons=btns,
    large_image=l_image,
    small_image=s_image,
    large_text="Сделано Coin collect27#1234",
    small_text="Flip Team on top")
    sleep(time1) 
    RPC.update(
    state=l_text2,
    details=s_text2,
    buttons=btns,
    large_image=l_image2,
    small_image=s_image2,
    large_text="Сделано Coin collect27#1234",
    small_text="Flip Team on top")
