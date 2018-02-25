## Test code for read date/time from gps and update RTC
import machine
import math
import network
import os
import time
import utime
from machine import RTC
from machine import SD
from machine import Timer
from L76GNSS import L76GNSS
from pytrack import Pytrack
import struct
# setup as a station

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


time.sleep(2)
gc.enable()

#Start GPS
py = Pytrack()
l76 = L76GNSS(py, timeout=600)
#start rtc
rtc = machine.RTC()
print('Aquiring GPS signal....')
#try to get gps date to config rtc
while (True):
   gps_datetime = l76.get_datetime()
   #case valid readings
   if gps_datetime[3]:
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
while (True):

   print("RTC time : {}".format(rtc.now()))
   coord = l76.coordinates()
   # lat_d, lon_d
   #f.write("{} - {}\n".format(coord, rtc.now()))
   print("$GPGLL>> {} - Free Mem: {}".format(coord, gc.mem_free()))
   coord1 = l76.coordinates1()
   # lat_d, lon_d, gps_time, gps_altitude, valid, num_satellites, hdop
   print("$GPGGA>> {} - Free Mem: {}".format(coord1, gc.mem_free()))
   coord2 = l76.get_datetime()
   # lat_d, lon_d, gps_time, valid, gps_date
   print("$G_RMC>> {} - Free Mem: {}".format(coord2, gc.mem_free()))
