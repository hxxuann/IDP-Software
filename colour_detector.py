import time
from MOTOR import Motor
from machine import Pin, PWM, I2C, ADC
from vl53l0x import VL53L0X
from tcs34725 import TCS34725, html_rgb

# colour sensor
i2c_bus = I2C(1, sda=Pin(18), scl=Pin(19))
TCS34725_ADDRESS = 0x29
print("I2C scan:", [hex(addr) for addr in i2c_bus.scan()])
tcs = TCS34725(i2c_bus)
motor = Motor()

# colour sensor
i2c_bus = I2C(0, sda=Pin(8), scl=Pin(9),freq=50000)
print("I2C scan:", [hex(addr) for addr in i2c_bus.scan()])
tcs = TCS34725(i2c_bus)

# TOF sensor
sda = Pin(18)
scl = Pin(19)
id = 1
i2c = I2C(id=id, sda=sda, scl=scl)
# Create a VL53L0X object
tof = VL53L0X(i2c)
budget = tof.measurement_timing_budget_us
print("Budget was:", budget)
tof.set_measurement_timing_budget(40000)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 18)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 12)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 14)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 8)

def detect_colour():
    color = html_rgb(tcs.read('raw'))
    print(color)
    red=color[0]
    green=color[1]
    blue=color[2]
    if red > 128 and green > 128:
        return "yellow"
    elif red > 128:
        return "red"
    elif blue > 128:
        return "blue"
    elif green > 128:
        return "green"
    else:
        return "invalid colour"
        
print(detect_colour())

    

def pickup():
    while (tof.ping()-36) > 10:
        motor.forward_slow()
    
    # actuator stuff
    
    return