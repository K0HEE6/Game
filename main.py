#Здесь у нас будет управление по типу WASD --> управление вертолетом, P --> Сохранение

from pynput import keyboard
from map import Map
import time
import os
from helicopter import Helicopter as Helico


TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10


field = Map(MAP_W, MAP_H)
field.generate_forest(3,10)
field.generate_rivers(10)
field.generate_rivers(10)

helico = Helico(MAP_W, MAP_H)



def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()



tick = 1

while True:
    os.system ("cls") #clear для MAC OS
    print("TICK", tick)
    field.print_map(helico)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()