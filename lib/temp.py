#
# A class to keep track of Temp
#

# Usage
# temp = Temp(DSDataPin, DSPowerPin)
# temp.tooLow()
# temp.tooHigh()
# temp.isOkay() returns, Okay, tooLow, tooHigh

class Temp:

    HIGH_ALARM = const(80)
    LOW_ALARM = const(1)

    def __init__(self, DSDataPin):
        self.DSDataPin = DSDataPin
        self._temp = -180

    def isOkay(self):
        # is temp between high/low
        # return okay, tooLow, toohigh

        # set self.temp
        self.getTemp()

        if self._temp >= HIGH_ALARM:
           return "HIGH"
        if self._temp <= LOW_ALARM:
           return "LOW"
        else:
           return "OKAY"

    def getTemp(self):
        # return temp string to 1 decimal place
        self._temp = self.readTemp()
        # TODO FORMAT to 1 de place
        return self._temp

    def readTemp(self):
        # replace with real temp reading code...
        return 25
