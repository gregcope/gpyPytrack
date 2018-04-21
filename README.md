gpyPytrack
=========

Intro
==========
Based on a Pycom gpy (Bluetooth, WLAN, LTE) ESP32 MicroPython board and its associated Pytrack module that has a L76 GNSS module (and LIPO battery charger).  This project needs a Daughter board.

Aim
==========
* Be very, very low power (17uA when asleep with GNSS VBACKUP powered)
* Chargeable from 12-24V
* Rechargeable LIPO battery for easy parts sourcing
* Has a button to enable user wake up
* GNSS For location
* LTE for Coms
* BilgeSwitch and Temp (DS18B20) Alarms
* LED for Status (in switch)

Checks
=============
* Frequent
  * BilgeSwitch state
  * Temp above / below threshold
  * If in Alarm, send coms
* Less Frequent (less likely to change frequently)
  * Position
  * Battery volts
  * VCC volts
  * If in Alarm, send coms
* Daily
  * All of the above and sends status

Parts
==========
* [Pycom Gpy](https://pycom.io/hardware/gpy-specs)
* [Pycom pytrack](https://pycom.io/hardware/pytrack-specs/)
* [Mini Step Down Regulator Voltag Power Supply Module 4.5v~55v to 5v](https://www.ebay.co.uk/sch/i.html?_osacat=0&_odkw=Mini+Step+Down+Regulator+Voltag+Power+Supply+Module+4.5v~55v+to+5v&_from=R40&_trksid=p2334524.m570.l1313.TR0.TRC0.H0.XMini+Step+Down+Regulator+Voltag+Power+Supply+Module+4.5v~55v+to+5v+600ma.TRS0&_nkw=Mini+Step+Down+Regulator+Voltag+Power+Supply+Module+4.5v~55v+to+5v+600ma&_sacat=0)
* [DS18B20 Waterproof Digital Probe Temperature Sensor with Silicone Cable (higher temp) Thermometer](https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR0.TRC0.H0.Xvermont+l+tent.TRS0&_nkw=DS18B20+Waterproof+Digital+Probe+Temperature+Sensor+Silicone+Cable+Thermometer&_sacat=0)
* [12V 12mm LED Power Push Button Switch Momentary Waterproof Metal 4 Pin](https://www.ebay.co.uk/sch/i.html?_osacat=0&_odkw=waterproof+LED+switch+12mm&_from=R40&_trksid=p2334524.m570.l1313.TR0.TRC0.H0.Xwaterproof+LED+switch+12mm+momentary.TRS0&_nkw=waterproof+LED+switch+12mm+momentary&_sacat=0)
* 1200mah LIPO Battery
* Bilge Switch (any normally closed, simple switch would do)

Daughter board
==============
The Daughter board fits between the Gpy/Fipy and Pytrack module via headers (see pictures when I add them).  It is designed to hold certain parts and expose some pins via headers or JST connectors.   Its footprint is similar to the Pytrack to keep space requirements down.

![pycomDaughterBoard.brd.png](/pycomDaughterBoard.brd.png)

The Daughter board mounts;
* VCC voltagedivider connected to an ADC pin to measure VCC
* Switchable Regulator with ENABLE pin connected to a pin
* JST(s) to breakout the relevant connections for the 11-36v VCC+GND, LED, Switch, DS18B20 Temp module, BilgeSwitch, 5V+GND for the Pytrack USB port
* __Note we will be putting 2x4pin JSTs on the Pytrack External IO to use those as well (simplifies this board and makes it smaller)__  

See the eagle files for the details.

Referances
=============
* https://blog.yavilevich.com/2017/03/efficient-dc-12v-to-5v-conversion-for-low-power-electronics-evaluation-of-six-modules/
