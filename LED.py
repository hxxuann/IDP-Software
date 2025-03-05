from machine import Pin
from utime import sleep
LED_PIN = 25  # according to documentation, not sure
led = Pin(LED_PIN, Pin.OUT)
def turn_led_on(on=True):
    delay_time = 5
    print(f"Waiting for {delay_time} seconds before turning on the LED...")
    time.sleep(delay_time)
    while on:
        
        led.value(1)
        sleep(1)
        led.value(0)
        sleep(1)
        

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
