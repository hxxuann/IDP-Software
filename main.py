import utime
from machine import Pin
from MOTOR import Motor
from LED import turn_led_off, turn_led_on
from colour_detector import detect_colour
from graph import collect, deposit, return_home
from config import button

tasks = 4
test_color = ['blue', 'red']
start = utime.time()

motor=Motor()

turn_led_on()

def main():
    motor.forward()
    utime.sleep(0.5)
    while utime.time()-start<270:
        for i in range(tasks):
            end = utime.time()
            if end-start>270:
                break
            collect(i)
            # color = detect_colour()
            deposit(test_color[i%2])
    
    return_home()
    turn_led_off()

# button=Pin(12,Pin.IN)
while True:
    if button.value()==1:
        main()
        

