#
# A class to keep track of status
# A stateMachine
#

# Usage
# stateMachine = StateMachine()
# stateMachine.doWeNeedToAlert()
# stateMachine.sendStatus()
#

class StateMachine:

    def __init__(self):
        self.doWeNeedToAlert = False

    def doWeNeedToAlert(self):
        # Do we need to alert?
        return self.doWeNeedToAlert

    def sendStatus(self):
        # send an update
        return True
