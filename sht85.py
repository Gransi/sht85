#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Peter Gransdorfer"
__copyright__ = "Copyright 2020"

__license__ = "GPL"
__maintainer__ = "Peter Gransdorfer"
__email__ = "peter.gransdorfer[AT]cattronix[com]"

import smbus

DEVICE = 0x44 # Default device I2C address


bus = smbus.SMBus(1) # Rev 2 Pi, Pi 2 & Pi 3 uses bus 1
                     # Rev 1 Pi uses bus 0

def readSHT85All(addr=DEVICE):

    # Measurement Commands for Single Shot Data Acquisition Mode
    bus.write_byte_data(addr, 0x24, 00)

    readout = bus.read_i2c_block_data(addr, 0x24, 6)
    # print (" ".join('{:02x}'.format(x) for x in readout))

    # Calc temperature °C
    temperaturebytes = int.from_bytes(readout[0:2], byteorder='big')
    temperature = -45 + 175 * (temperaturebytes / 65535)

    # Calc humidity
    humiditybytes = int.from_bytes(readout[3:5], byteorder='big')
    humidity = 100 * (humiditybytes / 65535)

    return temperature, humidity


def main():

  (temp, humidity) = readSHT85All()
  print ("Temp     :", temp)
  print ("Humidity :", humidity)


if __name__=="__main__":
   main()