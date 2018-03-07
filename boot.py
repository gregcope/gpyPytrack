from machine import UART
import machine
import os
from network import WLAN
from network import Bluetooth
from network import LTE
from pytrack import Pytrack
import network
import utime
import pycom

start = utime.ticks_us()
uart = UART(0, baudrate=115200)
os.dupterm(uart)

# switch stuff off ...
# WLAN off
wlan = WLAN()
#wlan.init(mode=WLAN.STA)
wlan.deinit()
# Bluetooth off
#bt = Bluetooth()
#bt.deinit()
# LTE off
#lte = LTE()
#lte.disconnect()
#lte.deinit()
# switch off FTP and telnet servers
server = network.Server()
server.deinit()
# done switching stuff off

# Initialise some other objects
py = Pytrack()

machine.main('main.py')

end = utime.ticks_us()
took = end - start
print("boot.py ... done in: {} uSec".format(took))
utime.sleep(2)
