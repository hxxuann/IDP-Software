import utime
from machine import Pin, PWM
from MOTOR import Motor
from colour_detector import detect_colour
from graph import collect, deposit, return_home
from config import button, led, servo_pin

tasks = 4
test_color = ['blue', 'red']


motor=Motor()
servo = PWM(servo_pin)
#Set PWM frequency
servo.freq (50)
#Servo at a degree
servo.duty_u16(3800)


def main():
    # Move out of starting box
    motor.forward()
    utime.sleep(1)

    # Timer to move back to starting point when time remaining < 40s
    while utime.time()-start<260:
        for i in range(tasks):
            end = utime.time()
            print(end-start)
            if end-start>260:
                break
            color = collect(i)
            deposit(color)
    
    return_home()
    led.value(0)

    

try:
    while True:
        # Start main after button pressed
        if button.value()==1:
            start = utime.time()
            main()
# except Exception as e:
#     print(e)
#     led.value(0)
#     motor.off()
except:
    # Stop Robot
    led.value(0)
    motor.off()
