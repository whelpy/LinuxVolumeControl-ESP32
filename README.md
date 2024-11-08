LinuxVolumeControl-ESP32

This is client-server suite for controlling individial applications volume in linux.

Server part is python script running in linux, periodically scanning for processes with sound.

Client part is ESP8266 module, with LCD displace from nokia phone, and and encoder.
It displays title and volume value of one application, turning encoder left and right changes the volume. Pressing on encoder iterates over applications.
Updated volume values appear on server, and get applied to pulse audio control.

Display backlight turns on for N seconds when new application appears, or active application changes the title, or when you turn or press the encoder.
