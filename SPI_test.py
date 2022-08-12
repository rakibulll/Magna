from pyftdi.spi import SpiController, SpiIOError
from time import time, sleep

spi = SpiController(cs_count=2)
#URL scheme to follow: ftdi://[vendor][:[product][:serial|:bus:address|:index]]/interface
spi.configure('ftdi://ftdi:232h:1/1')
slave = spi.get_port(cs=0, freq=10E6, mode=2)

while True:

    write_buf = b'\xA0'
    read_buf = slave.exchange(write_buf, duplex=True)
