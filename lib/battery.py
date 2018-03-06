#
# A class to keep track of the lipo battery
#

# Usage
# bat = battery(Pytrack)
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
