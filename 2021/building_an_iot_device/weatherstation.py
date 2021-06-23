# @Author: Matthew Hale <mlhale>
# @Date:   2021-06-23T13:48:11-05:00
# @Email:  mlhale@unomaha.edu
# @Filename: weatherstation.py
# @Last modified by:   mlhale
# @Last modified time: 2021-06-23T14:40:12-05:00
# @Author: Matthew Hale <mlhale>
# @Date:   2021-06-23T13:26:34-05:00
# @Email:  mlhale@unomaha.edu
# @Filename: password-cracker.py
# @Last modified by:   mlhale
# @Last modified time: 2021-06-23T14:40:12-05:00
# @Copyright: Copyright (C) 2021 Matthew L. Hale

# Modified barometer example, humiture, and temperature examples from https://github.com/sunfounder/SunFounder_SensorKit_for_RPi2/blob/master/Python/31_barometer.py to work with IFTTTlib by Matt Hale
#
import Adafruit_BMP.BMP085 as BMP085
import time
from iftttlib import IFTTTLib

ifttt = IFTTTLib()

#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

DHTPIN = 17

GPIO.setmode(GPIO.BCM)

MAX_UNCHANGE_COUNT = 100

STATE_INIT_PULL_DOWN = 1
STATE_INIT_PULL_UP = 2
STATE_DATA_FIRST_PULL_DOWN = 3
STATE_DATA_PULL_UP = 4
STATE_DATA_PULL_DOWN = 5

def read_dht11_dat():
    # Humidity sensor method
	GPIO.setup(DHTPIN, GPIO.OUT)
	GPIO.output(DHTPIN, GPIO.HIGH)
	time.sleep(0.05)
	GPIO.output(DHTPIN, GPIO.LOW)
	time.sleep(0.02)
	GPIO.setup(DHTPIN, GPIO.IN, GPIO.PUD_UP)

	unchanged_count = 0
	last = -1
	data = []
	while True:
		current = GPIO.input(DHTPIN)
		data.append(current)
		if last != current:
			unchanged_count = 0
			last = current
		else:
			unchanged_count += 1
			if unchanged_count > MAX_UNCHANGE_COUNT:
				break

	state = STATE_INIT_PULL_DOWN

	lengths = []
	current_length = 0

	for current in data:
		current_length += 1

		if state == STATE_INIT_PULL_DOWN:
			if current == GPIO.LOW:
				state = STATE_INIT_PULL_UP
			else:
				continue
		if state == STATE_INIT_PULL_UP:
			if current == GPIO.HIGH:
				state = STATE_DATA_FIRST_PULL_DOWN
			else:
				continue
		if state == STATE_DATA_FIRST_PULL_DOWN:
			if current == GPIO.LOW:
				state = STATE_DATA_PULL_UP
			else:
				continue
		if state == STATE_DATA_PULL_UP:
			if current == GPIO.HIGH:
				current_length = 0
				state = STATE_DATA_PULL_DOWN
			else:
				continue
		if state == STATE_DATA_PULL_DOWN:
			if current == GPIO.LOW:
				lengths.append(current_length)
				state = STATE_DATA_PULL_UP
			else:
				continue
	if len(lengths) != 40:
		#print ("Data not good, skip")
		return False

	shortest_pull_up = min(lengths)
	longest_pull_up = max(lengths)
	halfway = (longest_pull_up + shortest_pull_up) / 2
	bits = []
	the_bytes = []
	byte = 0

	for length in lengths:
		bit = 0
		if length > halfway:
			bit = 1
		bits.append(bit)
	#print ("bits: %s, length: %d" % (bits, len(bits)))
	for i in range(0, len(bits)):
		byte = byte << 1
		if (bits[i]):
			byte = byte | 1
		else:
			byte = byte | 0
		if ((i + 1) % 8 == 0):
			the_bytes.append(byte)
			byte = 0
	#print (the_bytes)
	checksum = (the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3]) & 0xFF
	if the_bytes[4] != checksum:
		#print ("Data not good, skip")
		return False

	return the_bytes[0], the_bytes[2]





def setup():
	print ('\n Barometer begins...')
    ifttt.setKey("your_key")
    

def loop():
	while True:
        
        humidity_data = read_dht11_dat()
        humidity = "N/A"
		if humidity_data:
			humidity, temperature = humidity_data
			# print ("humidity: %s %%,  Temperature: %s C`" % (humidity, temperature))
            
		time.sleep(1)
        
		sensor = BMP085.BMP085()
		temp = sensor.read_temperature()	# Read temperature to veriable temp
		pressure = sensor.read_pressure()	# Read pressure to veriable pressure

		print ('')
		print ('      Temperature = {0:0.2f} C'.format(temp))	# Print temperature
        print ('      Humidity: %s %%' % (humidity))            # Print humidity
		print ('      Pressure = {0:0.2f} Pa'.format(pressure))	# Print pressure
        ifttt.invokeWebhookTrigger("ng-weather",temp,pressure,"N/A",) # send pressure and temp to IFTTT
		time.sleep(1)			
		print ('')

def destroy():
	GPIO.cleanup()

        
if __name__ == '__main__':		# Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
