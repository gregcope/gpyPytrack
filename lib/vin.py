#
# A class to keep track of Voltage In
#

# Usage
# vin = Vin(VoltageDividerPin, regEngablePin)
# vin.volts()
# vin.regulatorOn()
# vin.regulatorOff()
# vin.regulatorState()

from machine import Pin, ADC

class Vin:

    CHARGE_THRESHOLD = const(13)
    LOW_THRESHOLD = 11.7
    ADC_VREF = 1200
    VOLTAGE_DIVIDER_MULTIPLER = 12

    def __init__(self, VoltageDividerPin, regEngablePin):
        # setup regEmablePin to ENABLE regulator
        self.pin = Pin(regEngablePin, mode=Pin.OUT)
        # setup VoltageDividerPin to be able to read VoltageDivider
        adc = machine.ADC()
        adc.vref(ADC_VREF)
        self.adcPin = adc.channel(pin=VoltageDividerPin, attn=ADC.ATTN_11DB)

    def volts(self):
        # read ADC on VoltageDividerPin and work out voltage
        print('checking vin volts')
        vinVolts = 0
        # ADC read VoltageDividerPin
        adcVal = self.adcPin.value()
        # return the ADC vaue times the VOLTAGE_DIVIDER_MULTIPLER
        # to get the actual volts on the VoltageDivider
        return adcVal * VOLTAGE_DIVIDER_MULTIPLER
        #return _vinVolts

    def regulatorOn(self):
        print('Regulator On')
         # set regEngablePin ON
        self.pin.hold(False)
        self.pin.value(1)
        self.pin.hold(True)

    def regulatorOff(self):
        print('Regulator Off')
        # set regEngablePin OFF
        self.pin.hold(False)
        self.pin.value(0)
        self.pin.hold(True)

    def regulatorState(self):
        return self.pin.value()
