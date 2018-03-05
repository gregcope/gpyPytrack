#
# A class to keep track of which checks to do
# takes an interval in Seconds

# usage
# checks = Check(60)
# checks.whichToDo()

# uses NVRAM to store lastLongCheck

import pycom
import utime

class Checks:

    def __init__(self, interval):
        self.interval = interval
        self.lastLongCheck = pycom.nvs_get('lastLongCheckTime')
        if self.lastLongCheck == None:
            print('LastLongCheckTime is None')
            self.lastLongCheck = 1520287405
        print("Doing checks every {} secs".format(self.interval))
        print("Last long check: {} epoc Secs".format(self.lastLongCheck))

    def short(self):
        print('Doing short checks ...')

    def long(self):
        print('Doing long checks ...')
        print("Setting 'lastLongCheckTime' NVRAM to: {} secs".format(utime.time()))
        pycom.nvs_set('lastLongCheckTime', utime.time())

    def whichToDo(self):
        print('Working out which checks to do')
        print('lastLongCheck is {}'.format(self.lastLongCheck))
        print('self.interval is {}'.format(self.interval))
        print('utime.time is {}'.format(utime.time()))

        if utime.time() > self.lastLongCheck + self.interval:
            self.long()
        else:
            self.short()
