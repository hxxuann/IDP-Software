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
servo.duty_u16(1900)

def main():
    #wait for button to start
    while button.read() == 0: 
        pass
    motor.forward()
    utime.sleep(0.5)
    while utime.time()-start<270:
        for i in range(tasks):
            end = utime.time()
            if end-start>270:
                break
            collect(i)
            # color = detect_colour()
            deposit(test_color[i%2])
    
    return_home()
    led.value(0)

if __name__ == "__main__":
    main()