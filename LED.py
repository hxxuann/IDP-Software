from machine import Pin
import time

LED_PIN = 25  # according to documentation, not sure

led = Pin(LED_PIN, Pin.OUT)

delay_time = 5

print(f"Waiting for {delay_time} seconds before turning on the LED...")

time.sleep(delay_time)

led.value(1) 
print("LED is ON now!")

# Insert ode when robot goes back to home

# time.sleep(5)  # Stays on for a while
# led.value(0) 
# print("LED is OFF now!")
