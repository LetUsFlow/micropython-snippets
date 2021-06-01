set -x

mpy-cross -march=xtensawin bme280.py
mpy-cross -march=xtensawin dht22.py
mpy-cross -march=xtensawin mhz14a.py

ampy -p /dev/ttyUSB0 put bme280.mpy
ampy -p /dev/ttyUSB0 put dht22.mpy
ampy -p /dev/ttyUSB0 put mhz14a.mpy

rm *.mpy
