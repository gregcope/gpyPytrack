#
# A class to keep track of which checks to do
# takes an interval in Seconds

# usage
# checks = Check(60)
# checks.whichToDo()

# uses NVRAM to store lastLongCheck

class Checks:

    def __init__(self, interval):
        self.lastLongCheck = 0
        self.interval = interval
        self.lastLongCheck = pycom.nvs_get(lastLongCheckTime)

    def short(self):
        print('Doing short checks')

    def long(self):
        print('Doing long checks')
        self.lastLongCheck = pycom.nvs_set(lastLongCheck)

    def whichToDo(self):
        print('Working out which checks to do')
        if timeNow > self.lastLongCheck + interval:
            self.long()
        else:
            self.short()
