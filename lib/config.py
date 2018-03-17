#
# A class to keep track of config
#

# Usage
# config = Config()
# config.getCoordinates()
# config.setCoordinates()
#
#

class Config:

    def __init__(self):
        # get the actual values from storage

    def getTemp(self):
        return self.temp

    def setTemp(self, temp):
        self.temp = temp
        self.save()

    def getBilgeSwitchState(self):

    def setBilgeSwitchState(self, state):
        self.bilgeSwitchState = stat
        self.save()

    def getSaveTime(self):
        return self.saveTime

    def getCoordinates(self):
        # Do we need to alert?
        return self.lat, self.lon

    def setCoordinates(self, lat, lon):
        # save the lat/lon
        self.lat = lat
        self.lon = lon
        self.save()

    def save(self):
        # do the actual saving

    def setVCCIsOn(self, VCCIsOn):
        self.VCCIsOn = state

    def getVCCIsOn(self):
        return self.VCCIsOn
