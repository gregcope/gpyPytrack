#
# A class to keep track of which checks to do
#

class Checks:

    def __init__(self, interval):
        self.lastLongCheck = 0
        self.interval = interval

    def short(self):
        print('Doing short checks')

    def long(self):
        print('Doing long checks')
        self.lastLongCheck = now()

    def which(self):
        print('working out which to do')
        if timeNow > lastLongCheck + interval:
            self.long()
        else:
            self.short()
