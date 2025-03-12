from machine import Pin, PWM
from utime import sleep

class Motor:
    def __init__(self):
        self.m1Dir = Pin(4, Pin.OUT) # set pin left wheel 7
        self.m2Dir = Pin(7, Pin.OUT)
        self.pwm1 = PWM(Pin(5))
        self.pwm2 = PWM(Pin(6))
        self.pwm1.freq(1000)
        self.pwm2.freq(1000)
        self.pwm1.duty_u16(0)
        self.pwm2.duty_u16(0)
        
    def off(self):
        self.pwm1.duty_u16(0)
        self.pwm2.duty_u16(0)
        
    def forward(self, adjust=None):
        self.m1Dir.value(0) # forward = 0 reverse = 1 motor 1
        self.m2Dir.value(0)
        if adjust == None:
            self.pwm1.duty_u16(int(65535*100/100)) # speed range 0-100 motor 1
            self.pwm2.duty_u16(int(65535*100/100))
            sleep(0.1)
        elif adjust == 0:
            self.pwm1.duty_u16(int(65535*70/100)) # left sensor touch line, slow down left
            self.pwm2.duty_u16(int(65535*100/100))
            sleep(0.1)
        else:
            self.pwm1.duty_u16(int(65535*100/100)) # right sensor touch line, slow down right
            self.pwm2.duty_u16(int(65535*70/100))

    def forward_slow(self):
        self.m1Dir.value(0)
        self.m2Dir.value(0)
        self.pwm1.duty_u16(int(65535*40/100))
        self.pwm2.duty_u16(int(65535*40/100))        
            
    def reverse(self):
        self.m1Dir.value(1)
        self.m2Dir.value(1)
        self.pwm1.duty_u16(int(65535*80/100))
        self.pwm2.duty_u16(int(65535*80/100))

    def right(self):
        self.m1Dir.value(0)
        self.m2Dir.value(0)
        self.pwm1.duty_u16(int(65535*100/100))
        self.pwm2.duty_u16(int(65535*0/100))

    
    def left(self):
        self.m1Dir.value(0)
        self.m2Dir.value(0)
        self.pwm1.duty_u16(int(65535*0/100))
        self.pwm2.duty_u16(int(65535*100/100))

    
    def back(self):
        self.m1Dir.value(0)
        self.m2Dir.value(1)
        self.pwm1.duty_u16(int(65535*80/100))
        self.pwm2.duty_u16(int(65535*80/100))
