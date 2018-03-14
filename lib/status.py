#
# A class to keep track of status
#

# Usage
# status = Status()
# status.doWeNeedToAlert()
# status.sendStatus()
#

class Status:

    def __init__(self):
        self._doWeNeedToAlert = False

    def doWeNeedToAlert(self):
        # Do we need to alert?
        return self._doWeNeedToAlert

    def sendStatus(self):
        # send an update
        return True
