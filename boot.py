from machine import UART
import machine
import os
from network import WLAN, Bluetooth

uart = UART(0, baudrate=115200)
os.dupterm(uart)

# switch stuff off ...
# WLAN off
wlan = WLAN()
#wlan.init(mode=WLAN.STA)
wlan.deinit()
# Bluetooth off
bt = Bluetooth()
bt.deinit()
# LTE off
lte = LTE()
lte.disconnect()
lte.deinit()
# switch off FTP and telnet servers
server = network.Server()
server.deinit()
# done switching stuff off

# Initialise some other objects
py = Pytrack()

machine.main('main.py')
