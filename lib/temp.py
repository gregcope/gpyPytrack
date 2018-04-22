#
# A class to keep track of Temp
#

# Usage
# temp = Temp(DSDataPin, DSPowerPin)
# temp.tooLow()
# temp.tooHigh()
# temp.isOkay() returns, Okay, tooLow, tooHigh

from machine import Pin
from onewire import DS18X20
from onewire import OneWire

class Temp:

    # Temp Consts
    HIGH_ALARM = const(80)
    LOW_ALARM = const(1)

    def __init__(self, DSDataPin):
        # Pin with the DS18B20 on
        ow = OneWire(pin(DSDataPin))
        self.pwTemp = DS18x20(ow)
        # temp variable
        self.temp = -180

    def isOkay(self):
        # is temp between high/low
        # return OkAY, LOW, HIGH

        # set self.temp
        self.getTemp()
        print("Temp is: {}".format(self.getTemp))

        # Are we too hot or too cold, or OKAY
        if self.temp >= HIGH_ALARM:
           return "HIGH"
        if self.temp <= LOW_ALARM:
           return "LOW"
        else:
           return "OKAY"

    def getTemp(self):
        # get temp
        # TODO Needs to be async or some sort of thread
        # def startTempThread(self):
        # self.temp_thread = _thread.start_new_thread(self.feedMicroGPS,())
        # do while ....
        self.pwTemp.start_conversion()
        # wait a bit
        self.temp = self.pwTemp.read_temp_async()

        # TODO FORMAT to 1 de place
        return self.temp
