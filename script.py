import os
from time import time, sleep
while True:
    sleep(10 - time() % 10)
    os.system("paste <(cat /sys/class/thermal/thermal_zone*/type) <(cat /sys/class/thermal/thermal_zone*/temp) | column -s $'\t' -t | sed 's/\(.\)..$/.\1°C/'")