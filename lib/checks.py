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

    VCC_THRESHOLD = const(13)
    INTERVAL = const(60)

    def __init__(self, led, vin, bilgeSwitch, battery, temp, stateMachine):
        # capture some objects
        self.led = led
        self.vin = vin
        self.bilgeSwitch = bilgeSwitch
        self.battery = battery
        self.temp = temp
        self.stateMachine = stateMachine

        self.lastLongCheck = pycom.nvs_get('lastLongCheckTime')
        if self.lastLongCheck == None:
            print('LastLongCheckTime is None')
            self.lastLongCheck = 1520287405
        print("Doing checks every {} secs".format(INTERVAL))
        print("Last long check: {} epoc Secs".format(self.lastLongCheck))

    def short(self):
        # do short checks like bilgeSwitch and temp
        print('Doing short checks ...')

        # start temp conversion
        # check bilge BilgeSwitch
        # get temp conversion

        # check bilgeSwitch is off!
        if self.bilgeSwitch.isOn():
            print('  BilgeSwitch.isOn ... no....')
            self.stateMachine.doWeNeedToAlert(True, "BilgeSwitch")

        # check temp is okay
        _temp = self.temp.isOkay()
        if _temp >= "HIGH_ALARM":
            print('  Temp is HIGH_ALARM')
            print("  Temp is {}".format(self.temp.getTemp()))
            self.stateMachine.doWeNeedToAlert(True, "tempTooHigh")
        if _temp <= "LOW_ALARM":
            print('  Temp is LOW_ALARM')
            print("  Temp is {}".format(self.temp.getTemp()))
            self.stateMachine.doWeNeedToAlert(True, "tempTooLow")

        # to be removed
        print("temp is: {}".format(self.temp.isOkay()))
        # else temp is OKAY!
        # DONE

    def long(self):
        # do long checks like POSn, batteryVolts and VCC volts
        print('Doing long checks ...')
        print("Setting 'lastLongCheckTime' NVRAM to: {} secs".format(utime.time()))
        pycom.nvs_set('lastLongCheckTime', utime.time())

        # do short checks
        self.short()

        # check lipoVolts
        self.checkLipoVolts()

        # check VCC volts
        self.checkVccVolts()

        # checkLocation
        self.checkLocation()


    def whichToDo(self):
        # work out which checks to do ...
        # reset problemFlag
        self.problemFlag = False
        print('Working out which checks to do ...')
        print('lastLongCheck is {}'.format(self.lastLongCheck))
        print('INTERVAL is {}'.format(INTERVAL))
        print('utime.time is {}'.format(utime.time()))

        # is it a daily check or a short check?
        if utime.time() > self.lastLongCheck + INTERVAL:
            if utime.time() > self.lastDayCheck + 86400:
                self.daily()
            else:
                self.long()
        # otherwise it must be a short check
        else:
            self.short()

    def checkVccVolts(self):
        # check VCC
        # if VVC >
        return True

    def checkLipoVolts(self):
        print("  Battery volts: {0:.2f}v".format(self.battery.volts()))
        if self.battery.alarm():
            print('  Battery Needs a charge')
        else:
            print('  Battery okay')
