import time
import board
import busio
import adafruit_tcs34725

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)
def detect_colour():
    color = sensor.color_rgb_bytes
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