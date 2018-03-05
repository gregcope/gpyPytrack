#
# A class to keep track of which checks to do
#

# Usage
# bat = battery()
# bat.volts()
# bat.alarm

class Battery:

    def __init__(self):
        self.chargedVolts = 4
        self.low = 3

    def volts(self):
        print('Doing battery check')
        return py.read_battery_voltage()

    def alarm(self):
        if volts() <= self.low:
            return True
        else:
            return False
