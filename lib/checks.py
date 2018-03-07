#
# A class to keep track of which checks to do
# takes an interval in Seconds

# usage
# checks = Check(SecondsInternval)
# checks.whichToDo()

# uses NVRAM to store lastLongCheck

import pycom
import utime

class Checks:

    def __init__(self, interval, led, vin, bilgeSwitch, battery, temp):
        self.interval = interval
        self.led = led
        self.vin = vin
        self.bilgeSwitch = bilgeSwitch
        self.battery = battery
        self.temp = temp
        self.problemFlag = False

        self.lastLongCheck = pycom.nvs_get('lastLongCheckTime')
        if self.lastLongCheck == None:
            print('LastLongCheckTime is None')
            self.lastLongCheck = 1520287405
        print("Doing checks every {} secs".format(self.interval))
        print("Last long check: {} epoc Secs".format(self.lastLongCheck))

    def short(self):
        # do short checks like bilgeSwitch and temp
        print('Doing short checks ...')
        # check bilgeSwitch is off!
        if self.bilgeSwitch.isOn():
            print('BilgeSwitch.isOn ... no....')
            problemFlag = True

        # check temp is okay
        _temp = self.temp.isOkay()
        if _temp == "HIGH_ALARM":
            print('Temp is HIGH_ALARM')
            print("temp is {}".format(self.temp.getTemp()))
            problemFlag = True
        if _temp == "LOW_ALARM":
            print('Temp is HIGH_ALARM')
            print("temp is {}".format(self.temp.getTemp()))
            problemFlag = True

        # to be removed
        print("temp is: {}".format(self.temp.isOkay()))
        # else temp is OKAY!
        # DONE

    def long(self):
        # do long checks like POSn, batteryVolts and VCC volts
        print('Doing long checks ...')
        print("Setting 'lastLongCheckTime' NVRAM to: {} secs".format(utime.time()))
        pycom.nvs_set('lastLongCheckTime', utime.time())

        print("Battery volts: {0:.2f}v".format(self.battery.volts()))
        if self.battery.alarm():
            print('Battery Needs a charge')
        else:
            print('Battery okay')

    def whichToDo(self):
        # work out which checks to do ...
        # reset problemFlag
        self.problemFlag = False
        print('Working out which checks to do ...')
        print('lastLongCheck is {}'.format(self.lastLongCheck))
        print('self.interval is {}'.format(self.interval))
        print('utime.time is {}'.format(utime.time()))

        if utime.time() > self.lastLongCheck + self.interval:
            self.long()
        else:
            self.short()
