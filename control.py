from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pynput.keyboard import Key, Controller, Listener
import time

pygame.init()
pygame.joystick.init()
keyboard = Controller()

joystick_count = pygame.joystick.get_count()
if pygame.joystick.get_count() == 0:
    print("No joystick connected. Please connect your G29.")
    quit()

for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()    
    name = joystick.get_name()
    if "G29" in name:
        print(f"G29 detected as joystick#{i}")
        break


event_mapping = {
    1538:{
        (0,1):Key.up,
        (1,0):Key.right,
        (0,-1):Key.down,
        (-1,0):Key.left,
    } 
}

try:
    while True:
        for event in pygame.event.get():
            if event.type in event_mapping:
                if event.value in event_mapping[event.type]:
                    keyboard.press(event_mapping[event.type][event.value])
                    keyboard.release(event_mapping[event.type][event.value])
                
        time.sleep(0.01)

except KeyboardInterrupt:
    print("Script terminated by user.")
finally:
    pygame.joystick.quit()
    pygame.quit()