import utime
from machine import Pin, PWM
from MOTOR import Motor
from colour_detector import detect_colour
from graph import collect, deposit, return_home
from config import button, led, servo_pin

tasks = 4
test_color = ['blue', 'red']
start = utime.time()

motor=Motor()
servo = PWM(servo_pin)
#Set PWM frequency
servo.freq (50)
#Servo at a degree
servo.duty_u16(3800)


def main():
    motor.forward()
    utime.sleep(1)
    while utime.time()-start<270:
        for i in range(tasks):
            end = utime.time()
            print(end-start)
            if end-start>270:
                break
            color = collect(i)
            deposit(color)
    
    return_home()
    led.value(0)

    

try:
    while True:
        if button.value()==1:
            main()
# except Exception as e:
#     print(e)
#     led.value(0)
#     motor.off()
except:
    led.value(0)
    motor.off()
