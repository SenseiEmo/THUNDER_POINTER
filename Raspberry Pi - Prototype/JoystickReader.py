from signal import signal, SIGTERM, SIGHUP, pause
from smbus import SMBus
from time import sleep

bus= SMBus(1)

def safeExit(signum, frame):
    exit(1)

ads7830_commands = [0x84, 0xc4, 0x94, 0xd4, 0xa4, 0xe4, 0xb4, 0xf4]

def read_ads7830(input):
    bus.write_byte(0x4b, ads7830_commands[input])
    return bus.read_byte(0x4b)

try:
    signal(SIGTERM, safeExit)
    signal(SIGHUP, safeExit)

    while True:
        print(f"x: {read_ads7830(7)}, y: {read_ads7830(6)}")
        sleep(0.1)

    pause()


except KeyboardInterrupt:
    pass
