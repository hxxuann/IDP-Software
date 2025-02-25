import time
import board
import busio
import adafruit_tcs34725

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)

while True:
    # temp = sensor.color_temperature
    # lux = sensor.lux
    print('Color: ({0}, {1}, {2})'.format(*sensor.color_rgb_bytes))
    # print('Temperature: {0}K'.format(sensor.color_temperature))
    # print('Lux: {0}'.format(sensor.lux))
    time.sleep(1)