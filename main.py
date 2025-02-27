import time
import threading
from machine import Pin
from LED import turn_led_off, turn_led_on
from colour_detector import detect_colour

start = time.time()
location = (0,0)
turn_led_on()

button=Pin(12,Pin.IN)
while True:
    if button.value()==1:
        #main()
        

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