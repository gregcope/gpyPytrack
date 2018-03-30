#
# A class to keep track of an LED
#

# Usage
# led = Led(ledPin)
# led.on()
# led.off()
# etc ...
from machine import Pin

class Led:

    def __init__(self, ledPin):
        self.pin = Pin(ledPin, mode=Pin.OUT)

    def On(self):
        print('Led On')
        # switch pin on
        self.pin.value(1)

    def regulatorOff(self):
        print('Regulator Off')
        # switch pin off
        self.pin.value(0)
