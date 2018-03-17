#
# A class to keep track of Temp
#

# Usage
# temp = Temp(DSDataPin, DSPowerPin)
# temp.tooLow()
# temp.tooHigh()
# temp.isOkay() returns, Okay, tooLow, tooHigh

class Temp:

    # Temp Consts
    HIGH_ALARM = const(80)
    LOW_ALARM = const(1)

    def __init__(self, DSDataPin):
        # Pin with the DS18B20 on
        self.DSDataPin = DSDataPin
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
        # return temp string to 1 decimal place
        self.temp = self.readTemp()
        # TODO FORMAT to 1 de place
        return self.temp

    def readTemp(self):
        # TODO replace with real temp reading code...
        return 25
