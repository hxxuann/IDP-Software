from machine import Pin
from utime import sleep
from config import led

def turn_led_on(on=True):
    led.value(0)
    delay_time = 5
    print(f"Waiting for {delay_time} seconds before turning on the LED...")
    sleep(delay_time)
    led.value(1)
        

def turn_led_off():
    # time_start=time.time()
    # while True:
    #     if time.time()-time_start>8:
    #         led.value(0) 
    #         print("LED is OFF now!")
    #         break
    sleep(8)
    turn_led_on(False)
    led.value(0) 
    print("LED is OFF now!")
