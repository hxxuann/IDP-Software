import time
from machine import Pin, PWM, I2C, ADC
from vl53l0x import VL53L0X
from tcs34725 import TCS34725

# colour sensor
i2c_bus = I2C(0, sda=Pin(8), scl=Pin(9),freq=50000)
print("I2C scan:", [hex(addr) for addr in i2c_bus.scan()])
tcs = TCS34725(i2c_bus)

# TOF sensor
sda = Pin(8)
scl = Pin(9)
id = 0
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
    color = tcs.color_rgb_bytes
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
        
    # print('Color: ({0}, {1}, {2})'.format(*sensor.color_rgb_bytes))

