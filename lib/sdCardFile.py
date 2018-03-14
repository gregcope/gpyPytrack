#
# A class to manage an sdcard log file
#

# Usage
# sdCardFile = SdCardFile('logfile')
# sdCardFile.write("a string")
# sdCardFile.read()
# etc ...

class sdCardFile:

    def __init__(self, FileName):
        self._fileName = FileName

    def write(self, ThingToWrite):
        print(ThingToWrite)
        # set self.ledPin ON

    def read(self):
        print('Reading')
        # set self.ledPin OFF
