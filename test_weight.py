# Example for Pycom device, gpio mode


from hx711_gpio import *
# import hx711
from machine import Pin
import utime

pin_OUT = Pin(2, Pin.IN, pull=Pin.PULL_DOWN)
pin_SCK = Pin(13, Pin.OUT)

hx711 = HX711(pin_SCK, pin_OUT)

hx711.tare(times=10)
value = hx711.read_average(times=10)
value = hx711.get_value()
print(value)
a = value
# 应该作为main函数还未完善

while 1:
    hx711.tare(times=10)
    value1 = hx711.read_average(times=10)
    value1 = hx711.get_value()
    
    print(value1)
    utime.sleep_ms(500)
    if value1 == a:
        continue
    else:
        #TODO: 重量变化调用摄像头，相应的函数在label_upload中
        break
print("finish")
