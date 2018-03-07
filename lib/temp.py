#
# A class to keep track of Temp
#

# Usage
# temp = Temp(DSDataPin, DSPowerPin)
# temp.tooLow()
# temp.tooHigh()
# temp.isOkay() returns, Okay, tooLow, tooHigh

class Temp:

    HIGH_ALARM = 80
    LOW_ALARM = 1

    def __init__(self, DSDataPin, DSPowerPin):
        self.DSDataPin = DSDataPin
        self.DSPowerPin = DSPowerPin
        self.temp = 50

    def isOkay(self):
        # is temp between high/low
        # return okay, tooLow, toohigh

        # set self.temp
        getTemp()
      
        if self._temp => HIGH_ALARM:
           return HIGH
        if self._temp <= LOW_ALARM:
           return LOW
        else:
           return OKAY

    def getTemp(self):
        # return temp string to 1 decimal place
        self.readTemp
        # TODO FORMAT to 1 de place
        return self.temp
