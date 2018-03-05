#
# A class to keep track of which checks to do
#

# Usage
# bat = battery()
# bat.volts()
# bat.alarm

class Battery:

    def __init__(self, py):
        self.chargedVolts = 4
        self.low = 3
        self.py = py

    def volts(self):
        #print('Doing battery check')
        return self.py.read_battery_voltage()

    def alarm(self):
        if self.volts() <= self.low:
            return True
        else:
            return False
