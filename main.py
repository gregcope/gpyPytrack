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


# setup as a station

battery = Battery(py)
#battery.volts()
print("Battery volts: {0:.2f}v".format(battery.volts()))
if battery.alarm():
    print('Battery Needs a charge')
else:
    print('Battery okay')

check = Checks(60)
check.whichToDo()


import gc
# https://forum.pycom.io/topic/1626/pytrack-gps-api/12

# PIN P9 / G16 for DS18X20 Data
# PIN P10 / G17 DS18X20 Power?
# PIN P11 / G22 for Power Switch VCC -> 5V on/off
# PIN P12 / G28 for external LED
# PIN P14 / G4 for button
# PIN P18 / G39 for 7-37V VCC voltage divider
# PIN P19 / G6 for bilgeSwitch sensor

# to sleep with GPS VBACKUP on
# should go down to 17ua
# https://forum.pycom.io/topic/2525/power-consumption/16
#
# py.go_to_sleep(True)


# enable GC
gc.enable()

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
#sd = SD()
#os.mount(sd, '/sd')
#f = open('/sd/gps-record.txt', 'w')
#while (True):

print("RTC time : {}".format(rtc.now()))
   #coord = l76.coordinates()
   # lat_d, lon_d
   #f.write("{} - {}\n".format(coord, rtc.now()))
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

lipoVolts = py.read_battery_voltage()
print("lipo battery Volts: {}".format(lipoVolts))

# switch off heartbeat LED
#pycom.heartbeat(False)
print('Going to kipp 2 secs in 1 sec')
time.sleep(1)
py.setup_sleep(2)
py.go_to_sleep(gps=True)
