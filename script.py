import os
from time import time, sleep
while True:
    sleep(10 - time() % 10)
    os.system("cat /sys/class/thermal/thermal_zone0/temp | column -s $'\t' -t | sed 's/\(.\)..$/.\1°C/'")
