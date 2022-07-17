#------------------------------------
from pypresence import Presence 
import os
import sys,time
import psutil
#------------------------------------
l_image = "" #large image name

s_image = "" #small image name

l_image2 = "" #large image name 2

s_image2 = "" #small image name 2

l_text = "" #large text

s_text = "" #small text

l_text2 = "" #large text 1

s_text2 = "" #small text 2

cooldown = 1 # status change time here
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
print("█▀█ █▀█ █▀▀")
print("█▀▄ █▀▀ █▄▄")
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
    time.sleep(cooldown) 
    RPC.update(
        state=l_text,
        
        details=s_text,
        
        buttons=btns,
        
        large_image=l_image,
        
        small_image=s_image,
        
        large_text="Created by Коин27#4349")
    time.sleep(cooldown) 
    RPC.update(
        state=l_text2,
        
        details=s_text2,
        
        buttons=btns,
        
        large_image=l_image2,
        
        small_image=s_image2,
        
        large_text="Created by Коин27#4349")
