## Test code for read date/time from gps and update RTC
#import machine
import math
import network
#import os
import time
import utime
from machine import RTC
from machine import SD
from machine import Timer
from L76GNSS import L76GNSS
from pytrack import Pytrack
import struct
from battery import Battery
from checks import Checks
from button import Button
from vin import Vin
from bilgeSwitch import BilgeSwitch
from led import Led
from temp import Temp
from stateMachine import StateMachine
import gc

# enable GC
gc.enable()

print('Going to kipp 4 secs in 1 sec')
time.sleep(1)
py.setup_sleep(4)
print('Kip...')
py.go_to_sleep(gps=True)


# setup as a station


#battery.volts()
#print("Battery volts: {0:.2f}v".format(battery.volts()))
#if battery.alarm():
#    print('Battery Needs a charge')
#else:
#    print('Battery okay')

# roughly works ...
vin = Vin('P16', 'P10')
led = Led('P11')
battery = Battery(py)

# still need work
stateMachine = StateMachine()
bilgeSwitch = BilgeSwitch('P13')
temp = Temp('P9')
button = Button('P14')

check = Checks(led, vin, bilgeSwitch, battery, temp, stateMachine)
check.whichToDo()

# https://forum.pycom.io/topic/1626/pytrack-gps-api/12

# to sleep with GPS VBACKUP on
# should go down to 17ua
# https://forum.pycom.io/topic/2525/power-consumption/16
#
# py.go_to_sleep(True)


# tell us why we woke
# display the reset reason code and the sleep remaining in seconds
# possible values of wakeup reason are:
# WAKE_REASON_ACCELEROMETER = 1
# WAKE_REASON_PUSH_BUTTON = 2
# WAKE_REASON_TIMER = 4
# WAKE_REASON_INT_PIN = 8

print("Wakeup reason: " + str(py.get_wake_reason()))
if py.get_wake_reason():
    print("Approximate sleep remaining: " + str(py.get_sleep_remaining()) + " sec")

# enable wakeup source from INT pin
py.setup_int_pin_wake_up(False)

# enable activity and also inactivity interrupts, using the default callback handler
py.setup_int_wake_up(True, True)

#Start GPS
#py = Pytrack()
l76 = L76GNSS(py, timeout=600)
#start rtc
rtc = machine.RTC()
start = utime.ticks_ms()
print('Aquiring GPS signal ', end='')
#try to get gps date to config rtc

while (True):
   gps_datetime = l76.get_datetime()
   coord2 = l76.get_datetime()
   print("$G_RMC>> {} - Free Mem: {}".format(coord2, gc.mem_free()))
   #print('.', end='')
   #case valid readings
   if gps_datetime[3]:
       print(' done')
       end = utime.ticks_ms()
       took = end - start
       print("First GNS fix took: {} mSec".format(took))

       day = int(gps_datetime[4][0] + gps_datetime[4][1] )
       month = int(gps_datetime[4][2] + gps_datetime[4][3] )
       year = int('20' + gps_datetime[4][4] + gps_datetime[4][5] )
       hour = int(gps_datetime[2][0] + gps_datetime[2][1] )
       minute = int(gps_datetime[2][2] + gps_datetime[2][3] )
       second = int(gps_datetime[2][4] + gps_datetime[2][5] )
       print("Current location: {}  {} ; Date: {}/{}/{} ; Time: {}:{}:{}".format(gps_datetime[0],gps_datetime[1], day, month, year, hour, minute, second))
       rtc.init( (year, month, day, hour, minute, second, 0, 0))
       break

print('RTC Set from GPS to UTC:', rtc.now())

chrono = Timer.Chrono()
chrono.start()

print("RTC time : {}".format(rtc.now()))
   #coord = l76.coordinates()
   # lat_d, lon_d
   #print("$GPGLL>> {} - Free Mem: {}".format(coord, gc.mem_free()))
coord1 = l76.coordinates1()
# lat_d, lon_d, gps_time, gps_altitude, valid, num_satellites, hdop
print("$GPGGA>> {} - Free Mem: {}".format(coord1, gc.mem_free()))
   #coord2 = l76.get_datetime()
   # lat_d, lon_d, gps_time, valid, gps_date
   #print("$G_RMC>> {} - Free Mem: {}".format(coord2, gc.mem_free()))

# go to sleep for 60 secs maximum if no button interrupt happens
#pycom.rgbled(0x00FF00)
#time.sleep(2)


# switch off heartbeat LED
#pycom.heartbeat(False)
print('Going to kipp 2 secs in 1 sec')
time.sleep(1)
py.setup_sleep(2)
py.go_to_sleep(gps=True)
