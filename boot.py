import network
from machine import Pin
import time

led = Pin(4,Pin.OUT)

# setup as station
sta_if = network.WLAN(network.STA_IF)

# activate station
sta_if.active(True)

# connect to wifi
sta_if.connect('<ssid>','<password>')

# wait until wifi is connected
while not sta_if.isconnected():
    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(0.3)
    
led.on()

print(sta_if.ifconfig())