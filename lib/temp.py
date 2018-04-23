#
# A class to keep track of Temp
#

# Usage
# temp = Temp(DSDataPin)
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

    def startTempThread(self):
	# starts Temp thread
	self.temp_thread = _thread.start_new_thread(self.getReading,())

    def getTemp(self):
	# return temp which is already fixed to 2 decimal palace e.g. 20.12
	#self.temp = float("{0:.1f}v".format(self.temp))
	#self.temp = round(self.temp, 1)
	return self.temp

    def getReading(self):
        # get temp
        # start converstion
        self.pwTemp.start_conversion()

        # wait a bit until we have a reading
	while self.pwTemp.read_temp_async() != None:
        	time.sleep(0.1)

	# to get here self.pwTemp.read_temp_async() must have returned something
	self.temp = self.pwTemp.read_temp_async()

