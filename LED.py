from machine import Pin
import time
LED_PIN = 25  # according to documentation, not sure
led = Pin(LED_PIN, Pin.OUT)
def turn_led_on():
    delay_time = 5
    print(f"Waiting for {delay_time} seconds before turning on the LED...")
    time.sleep(delay_time)
    led.value(1) 
    print("LED is ON now!")

def turn_led_off():
    # time_start=time.time()
    # while True:
    #     if time.time()-time_start>8:
    #         led.value(0) 
    #         print("LED is OFF now!")
    #         break
    time.sleep(8)
    led.value(0) 
    print("LED is OFF now!")
