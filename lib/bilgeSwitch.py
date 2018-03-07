#
# A class to keep track of a bilgeSwitch
#

# Usage
# bilgeSwitch = BilgeSwitch(bilgeSwitchPin)
# bilgeSwitch.isO()

class BilgeSwitch:

    def __init__(self, bilgeSwitchPin):
        self.bilgeSwitchPin = bilgeSwitchPin

    def isOn(self):
        print('is bilgeSwitch on ?')
        return True
