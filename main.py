import utime
from machine import Pin
from LED import turn_led_off, turn_led_on
from colour_detector import detect_colour
from graph import collect, deposit, return_home

tasks = [0,1,2,3]

start = utime.time()
location = (0,0)
turn_led_on()

def main():
    while utime.time()-start<270:
        for i in tasks:
            end = utime.time()
            if end-start>270:
                break
            collect(i)
            color = detect_colour()
            deposit(color)
    
    return_home()
    turn_led_off()

button=Pin(12,Pin.IN)
while True:
    if button.value()==1:
        main()
        

