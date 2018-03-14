#
# A class to keep track of the lipo battery
#

# Usage
# bat = battery(Pytrack)
# bat.volts()
# bat.alarm

class Battery:

    BATTERY_LOW = const(3)
    BATTERY_CHARGED = const(4)
    
    def __init__(self, py):
        self.chargedVolts = 4
        self.py = py

    def volts(self):
        #print('Doing battery check')
        return self.py.read_battery_voltage()

    def voltsString(self):
        # return string to 2 decimal places
        return "{0:.2f}v".format(self.volts())

    def alarm(self):
        if self.volts() <= BATTERY_LOW:
            return True
        else:
            return False
