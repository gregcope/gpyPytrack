#
# A class to keep track of Voltage In
#

# Usage
# vin = Vin(VoltageDividerPin, regEngablePin)
# vin.volts()
# vin.regulatorOn()
# vin.regulatorState()
# etc ...

class Vin:

    CHARGE_THRESHOLD = const(13)
    LOW_THRESHOLD = 11.7

    def __init__(self, VoltageDividerPin, regEngablePin):
        self.regulatorState = False
        self.VoltageDividerPin = VoltageDividerPin
        self.regEngablePin = regEngablePin

    def volts(self):
        # read ADC on VoltageDividerPin and work out voltage
        print('checking vin volts')

        _vinVolts = 0
        # do stuff to VoltageDividerPin
        return _vinVolts

    def regulatorOn(self):
        print('Regulator On')
        # set regEngablePin ON

    def regulatorOff(self):
        print('Regulator Off')
        # set regEngablePin OFF

    def regulatorState(self):
        print('Regulator is: X')
        # reaf regEngablePin state
