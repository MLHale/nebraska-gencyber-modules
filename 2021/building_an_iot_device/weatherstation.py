# @Author: Matthew Hale <mlhale>
# @Date:   2021-06-23T13:48:11-05:00
# @Email:  mlhale@unomaha.edu
# @Filename: weatherstation.py
# @Last modified by:   mlhale
# @Last modified time: 2021-06-23T14:18:57-05:00
# @Copyright: Copyright (C) 2019 Matthew L. Hale



#---------------------------------------------------------
#
#		This is a program based on the barometer module demo from 
#       https://github.com/sunfounder/SunFounder_SensorKit_for_RPi2
#
#---------------------------------------------------------
#!/usr/bin/env python3

import Adafruit_BMP.BMP085 as BMP085
import time

def setup():
	print ('\n Barometer begins...')

def loop():
	while True:
		sensor = BMP085.BMP085()
		temp = sensor.read_temperature()	# Read temperature to veriable temp
		pressure = sensor.read_pressure()	# Read pressure to veriable pressure

		print ('')
		print ('      Temperature = {0:0.2f} C'.format(temp))		# Print temperature
		print ('      Pressure = {0:0.2f} Pa'.format(pressure))	# Print pressure
		time.sleep(1)			
		print ('')

def destroy():
	pass

if __name__ == '__main__':		# Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
