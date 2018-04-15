#
# A class to keep track of Voltage In
#

# Usage
# vin = Vin(voltageDividerPin, regEngablePin)
# vin.volts()
# vin.regulatorOn()
# vin.regulatorState()
# etc ...

class Vin:

    CHARGE_THRESHOLD = const(13)
    LOW_THRESHOLD = 11.7

    def __init__(self, voltageDividerPin, regEngablePin):

        # setup the regulator pin
        # as output to toggle the regulator
        self.regEngablePin = Pin('regEngablePin', mode=Pin.OUT)

        # setup the voltageDividerPin
        # as input to read the ADC
        self.voltageDividerPin = Pin('voltageDividerPin', mode=Pin.IN)

    def volts(self):
        # read ADC on VoltageDividerPin and work out voltage
        print('checking vin volts')

        vinVolts = 0
        # do stuff to VoltageDividerPin
        return vinVolts

    def regulatorOn(self):
        print('Regulator On
        # set regEngablePin ON
        # Need to self.regEngablePin.hold(True) to keep it on
        # over power downs
        self.regEngablePin.value(1)
        self.regEngablePin.hold(True)

    def regulatorOff(self):
        print('Regulator Off')
        # set regEngablePin OFF
        # Need to self.regEngablePin.hold(False) to allow it to keep it on
        # over power downs
        self.regEngablePin.hold(False)
        self.regEngablePin.value(0)

    def regulatorState(self):
        print('Regulator is: X')
        # return state of pin
        # true == on, false == 0ff
        return self.regEngablePin()
