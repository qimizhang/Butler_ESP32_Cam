# Example for Pycom device, gpio mode
# Connections:
# Pin # | HX711
# ------|-----------
# P9    | data_pin
# P10   | clock_pin
#

from hx711 import HX711
import hx711
from machine import Pin

pin_OUT = Pin(12, Pin.IN, pull=Pin.PULL_DOWN)
pin_SCK = Pin(13, Pin.OUT)

hx711 = HX711(pin_SCK, pin_OUT)

hx711.tare()
value = hx711.read()
value = hx711.get_value()
print(value)
a = value
while 1:
    value = hx711.read()
    value = hx711.get_value()
    print(value)
    if value == a:
        continue
    else:
        break
print("finish")