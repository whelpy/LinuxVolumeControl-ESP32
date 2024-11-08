LinuxVolumeControl-ESP32

This is client-server suite for controlling individial applications volume in linux.

Server part is python script running in linux, periodically scanning for processes with sound.

Client part is ESP8266 module, with LCD display from nokia phone, and an encoder.
It displays title and volume values of one application, turning encoder left and right changes the volume. Pressing on encoder iterates over applications.
Updated volume values are being processed with server python script, and then applied to pulse audio control.

Display backlight turns on for N seconds when new application appears, or active application changes the title, or when you turn or press the encoder.

Example of inital setup (work in progress).
![IMG_20241108_161059](https://github.com/user-attachments/assets/6c422dad-32bc-4db6-94ec-2231a6160f3f)
