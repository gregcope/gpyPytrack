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
        return self._temp

    def setTemp(self, temp):
        self._temp = temp
        self._save()

    def getBilgeSwitchState(self):

    def setBilgeSwitchState(self, state):
        self._bilgeSwitchState = stat
        self._save()

    def getSaveTime(self):
        return self._saveTime

    def getCoordinates(self):
        # Do we need to alert?
        return self._lat, self._lon

    def setCoordinates(self, lat, lon):
        # save the lat/lon
        self._lat = lat
        self._lon = lon
        self._save()

    def _save(self):
        # do the actual saving
