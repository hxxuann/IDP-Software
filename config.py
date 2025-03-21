from machine import Pin

# List of pins
m1Dir = Pin(4, Pin.OUT)
pwm1 = Pin(5)
pwm2 = Pin(6)
m2Dir = Pin(7, Pin.OUT)
junction_left = Pin(10, Pin.IN)
line_right = Pin(11, Pin.IN)
junction_right = Pin(12, Pin.IN)
line_left = Pin(13, Pin.IN)
servo_pin = Pin(15)
tof_sda = Pin(16)
tof_scl = Pin(17)
colour_sda = Pin(18)
colour_scl = Pin(19)
button=Pin(21,Pin.IN)
led = Pin(20, Pin.OUT)