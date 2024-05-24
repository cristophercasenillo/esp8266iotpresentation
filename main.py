import microdot
from machine import Pin

led = Pin(4,Pin.OUT)

app = microdot.Microdot()

@app.route('/')
async def index(request):
    return microdot.send_file('html/main.html')

@app.post('/button')
async def button(request):
    led.value(not led.value())

app.run(port=80)