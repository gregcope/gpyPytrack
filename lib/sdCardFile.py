#
# A class to manage an sdcard log file
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
        self._fileName = fileName
        # mount
        self._sd = SD()
        os.mount(self._sd, '/sd')
        # rotate if required
        self.rotateIfNeeded(self)
        # open file
        self._f = open(self._fileName, 'w')

    def write(self, ThingToWrite):
        print(ThingToWrite)
        self._f.write("{}: {}\n".format(rtc.now(), ThingToWrite))
        os.sync()

    def rotateIfNeeded(self):
        # Check file size
        # and rotate if above ROTATIONSIZE
        stat = os.stat(self._fileName)
        print("{} is {} bytes".format(self._fileName, stat[6))
        if stat[6] > ROTATIONSIZE:
            # make a new name
            _newName = self._fileName + '.old'
            # remove it if exists
            try:
                os.remove(_newName)
            # rename
            os.rename(self._fileName, _newName)        
