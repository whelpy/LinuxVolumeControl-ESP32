#!/usr/bin/python

from sys import	exit
import subprocess
import time
import json
import serial

print('PulseAudio inputs watcher started.')

sinks = {}
currentId = 0

def getVolumeValues():	
	global currentId
	counter	= 0
	for key in sinks:
		item = sinks[key]
		item["EXP"] = 1

	process	= subprocess.Popen('pactl list sink-inputs', shell=True, stdout=subprocess.PIPE)
	lines =	process.stdout.read().decode('utf-8').split('\n')
	for	line in	lines:
		if	(line.startswith('Sink Input ')):
			lineParts	= line.split(' ')
			number = int(lineParts[2].replace('#',''))			
			
			if (number in sinks):
				item = sinks[number]
				item["EXP"] = 0
			else:
			# add new list item
				counter =	counter	+ 1
				item = {}
				item["ID"] = number
				sinks[number] = item
				item["EXP"] = 0
				if (currentId == 0):
					currentId = number
				
		if	(line.startswith('\tVolume: ')):
			vol =	line.replace('\tVolume: ', '').split('/')
			item["VOL"] = int(vol[1].replace('%','').replace(' ',''))

		if	(line.startswith('\t\tmedia.name = ')):
			title	= line.replace('\t\tmedia.name = ',	'').replace('\"', '')
			item["TITLE"] = title

		if	(line.startswith('\t\tapplication.name = ')):
			app =	line.replace('\t\tapplication.name = ',	'').replace('\"', '')
			item["APP"] = app

	# clear expired
	expiredIds = []
	for	key in	sinks:
		item = sinks[key]
		if (item["EXP"] == 1):
			expiredIds.append(key)
			
	for expId in expiredIds:		
		sinks.pop(expId)
		if (currentId == expId):
			currentId = 0
	

def getCurrentValue():
	if (currentId in sinks):
		item = sinks[currentId]
		jsonText = json.dumps(item)
		print(jsonText)
		ser.write(str.encode(jsonText))
		ser.write(b'\n')
	else:
		print(b'{"ID": 0 }')
		ser.write(b'{"ID": 0 }')
		ser.write(b'\n')
	
	
ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)  # open serial port

while True:
	print(ser.name)         # check which port was really used
	s = ser.readline()
	print(s)
	
	print('==> Main loop')
	getVolumeValues()
			
	# resulting output
	#for	key in	sinks:
	#	if (currentId == 0):
	#		currentId = key
	#	item = sinks[key]
	#	jsonText = json.dumps(item)
	#print(currentId)
		
	getCurrentValue()
	

	time.sleep(1)


exit()