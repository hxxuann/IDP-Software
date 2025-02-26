import time
import threading
from LED import turn_led_off, turn_led_on
from colour_detector import detect_colour

start = time.time()
location = (0,0)
turn_led_on()

def collect(point):
    #collect parcel from points ABCD
    pass

def deposit():
    #deposit parcel at depots
    pass

tasks = [0,1,2,3]

blink_thread = threading.Thread(target=blink_led, daemon=True)
blink_thread.start()

while time.time()-start<270:
    for i in tasks:
        end = time.time()
        if end-start>270:
            break
        collect(i)
        color = detect_colour()
        deposit(color)
        
turn_led_off()