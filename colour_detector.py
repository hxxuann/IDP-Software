import utime
from MOTOR import Motor
from machine import PWM, I2C
from vl53l0x import VL53L0X
from tcs34725 import TCS34725, html_rgb
from config import colour_sda, colour_scl, tof_scl, tof_sda, servo_pin, line_left, line_right
# colour sensor
i2c_bus = I2C(1, sda=colour_sda, scl=colour_scl)
TCS34725_ADDRESS = 0x29
print("I2C scan:", [hex(addr) for addr in i2c_bus.scan()])
tcs = TCS34725(i2c_bus)
motor = Motor()
def scan_sensor(i2c_bus):
    devices = i2c_bus.scan()
    if TCS34725_ADDRESS in devices:
        print("TCS34725 sensor detected at address 0x{:02X}".format(TCS34725_ADDRESS))
        return True
    else:
        print("TCS34725 sensor not detected.")
        return False

# TOF sensor

i2c = I2C(0, sda=tof_sda, scl=tof_scl)
tof = VL53L0X(i2c)
budget = tof.measurement_timing_budget_us
print("Budget was:", budget)
tof.set_measurement_timing_budget(40000)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 18)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 12)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 14)
tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 8)

        

# Function to scan I2C devices
def scan_sensor(i2c_bus):
    devices = i2c_bus.scan()
    if TCS34725_ADDRESS in devices:
        print("TCS34725 sensor detected at address 0x{:02X}".format(TCS34725_ADDRESS))
        return True
    else:
        print("TCS34725 sensor not detected.")
        return False

# Function to test the sensor and get readings
# def test_sensor():
#     if scan_sensor(i2c_bus):

#         tcs = TCS34725(i2c_bus)
#         print('Raw data: {}'.format(tcs.read('raw')))
#         print('RGB data: {}'.format(tcs.read('rgb')))
#         print(tcs.read(raw=False))
#     else:
#         print("Unable to initialize sensor.")
# while True:
#     print(tcs.read('raw'))
#     sleep_ms(500)
#     
def detect_colour():
    color = html_rgb(tcs.read('raw'))
    print(color)
    red=color[0]
    green=color[1]
    blue=color[2]
    if red > 5 and green > 20 and blue<10:
        return "yellow"
    elif red > 15:
        return "red"
    elif blue > 20:
        return "blue"
    # elif green > 10 and blue>10:
    #     return "green"
    else:
        return "green"
        # return "invalid colour"    
servo = PWM(servo_pin)
#Set PWM frequency
servo.freq (50)
#Servo at a degree
servo.duty_u16(3800)

def pickup():
    servo.duty_u16(2000)
    utime.sleep(1)
    motor.forward_slow()
    utime.sleep(0.5)
    print(tof.ping()-36)
    while (tof.ping()-36) > 8:
        print(tof.ping()-36)
        if line_left.value() == 1:
            motor.forward_slow(0)
        elif line_right.value() == 1:
            motor.forward_slow(1)
        else:
            motor.forward_slow()
    motor.off()
    servo.duty_u16(2400)
    utime.sleep(1)
    colour = detect_colour()
    #Servo at a degree

    return colour

def dropoff():
    servo.duty_u16(2000)
    
def liftup():
    servo.duty_u16(3800)
    utime.sleep(1)
    
