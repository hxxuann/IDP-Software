import time
from LED import turn_led_off, turn_led_on
start = time.time()
global location 
location = (0,0)
turn_led_on()

def collect(point):
    #collect parcel from points ABCD
    pass

def deposit():
    #deposit parcel at depots
    pass

tasks = [0,1,2,3]

while time.time()-start<270:
    for i in tasks:
        end = time.time()
        if end-start>270:
            break
        collect(i)
        deposit()
        
turn_led_off()