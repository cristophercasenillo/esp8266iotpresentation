
# Prerequisites
1. Install Visual Studio Code
2. Install python - https://www.python.org/
3. Download latest version of the ESP8266 firmware from https://micropython.org/download/ESP8266_GENERIC/
4. Install the VS Code Extension PyMakr

# Flashing the ESP8266 with the firmware

1. Create virtual environment using

    `python -m venv .venv`

2. Install esptool in the virtual environment 

    `pip install esptool`

3. Using esptool.py you can erase the flash with the command: 

    `esptool --port <serial_port> erase_flash` 

4. And then deploy the new firmware using:

    `esptool --port <serial_port> --baud 115200 write_flash --flash_size=detect 0 <path_to_firmware_file>`

# Test light up LED

 ```python
 from machine import Pin
x = Pin(4,Pin.OUT)
x.on()
x.off()
```

# Connect to wifi
```python
import network

# setup as station
sta_if = network.WLAN(network.STA_IF)

# activate station
sta_if.active(True)

# scan wifi networks
sta_if.scan() # outputs list of tuples

# connect to wifi
sta_if.connect('<SSID>','<PASSWORD>')

# get connection details
sta_if.ifconfig()


```
References
https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware

Microdot https://github.com/miguelgrinberg/microdot and
https://microdot.readthedocs.io/en/latest/
