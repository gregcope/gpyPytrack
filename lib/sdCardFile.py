#
# A class to manage an sdcard file
#
#

from machine import SD
import OS

# Usage
# sdCardFile = SdCardFile('logfile')
# sdCardFile.write("a string")
# sdCardFile.read()
# etc ...

class sdCardFile:

    # 100K rotation size
    ROTATIONSIZE = const(100000)

    def __init__(self, fileName):
        self.fileName = fileName
        # mount
        self.sd = SD()
        os.mount(self.sd, '/sd')
        # rotate if required
        self.rotateIfNeeded(self)
        # open file
        self.f = open(self.fileName, 'w')

    def write(self, ThingToWrite):
        print("{}\n".format(ThingToWrite)
        self.f.write("{}".format(ThingToWrite))
        os.sync()
        
    def writeTimeWithStamp(self, ThingToWrite):
        print("{}: {}\n".format(rtc.now(), ThingToWrite))
        self.f.write("{}: {}\n".format(rtc.now(), ThingToWrite))
    os.sync()

    def rotateIfNeeded(self):
        # Check file size
        # and rotate if above ROTATIONSIZE
        stat = os.stat(self.fileName)
        print("{} is {} bytes".format(self.fileName, stat[6))
        if stat[6] > ROTATIONSIZE:
            # make a new name
            newName = self.fileName + '.old'
            # remove it if exists
            try:
                os.remove(newName)
            # rename
            os.rename(self._fileName, newName)
