#!/usr/bin/python

from sys import	exit
import subprocess
import time
import json

print('PulseAudio inputs watcher started.')

counter	= 0
sinks = {}
currentId = 0

while True:
	
	print('==> Main loop')
	
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
			if (len(vol) < 4):
				item["VOL_M"] = int(vol[1].replace('%','').replace(' ',''))
				item["VOL_L"] = 0
				item["VOL_R"] = 0
			else:
				item["VOL_M"] = 0
				item["VOL_L"]	= int(vol[1].replace('%','').replace(' ',''))
				item["VOL_R"]	= int(vol[3].replace('%','').replace(' ',''))
				

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
			
	# resulting output
	for	key in	sinks:
		item = sinks[key]
		jsonText = json.dumps(item)
		print(jsonText)
		
	print(f'CurrentId: {currentId}')
	

	time.sleep(1)


exit()