#!/usr/bin/python

from sys import exit
import subprocess

class SinkItem:
    number = 0
    title = ''
    volumeMono = 0
    volumeL = 0
    volumeR = 0
    application = ''


print('PulseAudio inputs watcher started.')

counter = 0
sink = []

process = subprocess.Popen('pactl list sink-inputs', shell=True, stdout=subprocess.PIPE)
lines = process.stdout.read().decode('utf-8').split('\n')
for line in lines:
    #print(line)
    if (line.startswith('Sink Input ')):
        lineParts = line.split(' ')
        counter = counter + 1
        item = SinkItem()
        item.number = int(lineParts[2].replace('#',''))
        sink.append(item)

    if (line.startswith('\tVolume: ')):
        vol = line.replace('\tVolume', '').split('/')
        if (len(vol) < 4):
            item.volumeMono = int(vol[1].replace('%','').replace(' ',''))
        else:
            item.volumeL = int(vol[1].replace('%','').replace(' ',''))
            item.volumeR = int(vol[3].replace('%','').replace(' ',''))

    if (line.startswith('\t\tmedia.name = ')):
        title = line.replace('\t\tmedia.name = ', '').replace('\"', '')
        item.title = title

    if (line.startswith('\t\tapplication.name = ')):
        app = line.replace('\t\tapplication.name = ', '').replace('\"', '')
        item.application = app



for item in sink:
    print('=====')
    print(f'Sink number: {item.number}')
    print(f'Application: {item.application}')
    print(f'Title: {item.title}')
    print(f'Mono: {item.volumeMono}')
    print(f'Left: {item.volumeL}')
    print(f'Right: {item.volumeR}')




exit()