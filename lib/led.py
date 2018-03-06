#
# A class to keep track of an LED
#

# Usage
# led = Led(ledPin)
# led.on()
# led.off()
# etc ...

class Led:

    def __init__(self, ledPin):
        self.ledPin = ledPin

    def On(self):
        print('Led On')
        # set self.ledPin ON

    def regulatorOff(self):
        print('Regulator Off')
        # set self.ledPin OFF
