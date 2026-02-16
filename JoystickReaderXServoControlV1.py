#Imports all neccesery modules for the code -->
from signal import signal, SIGTERM, SIGHUP, pause
from smbus import SMBus
from time import sleep
from gpiozero import AngularServo

bus = SMBus(1)

servoX = AngularServo(18, min_pulse_width=0.0005, max_pulse_width=0.0025)
#servoY = AngularServo(--, min_pulse_width=0.0006, max_pulse_width=0.0023)

#This sets the servos' location to zero at the begining
#It does so but for only a second
#It doesn't work
try:
    servoX.angle = 0
    sleep(1)
except:
    while (True):
        print("Failed to zero!")
        sleep()

def safeExit(signum, frame):
    exit(1)

ads7830_commands = [0x84, 0xc4, 0x94, 0xd4, 0xa4, 0xe4, 0xb4, 0xf4]

#Reads the ads7830 output -->
def read_ads7830(input):
    bus.write_byte(0x4b, ads7830_commands[input])
    return bus.read_byte(0x4b)


#Prints the Joystick values and controlls the servos -->
try:
    signal(SIGTERM, safeExit)
    signal(SIGHUP, safeExit)

    while True:
        print(f"x: {read_ads7830(7)}, y: {read_ads7830(6)}")
        servoX.angle = servoX.min()
        servoX.angle = ((read_ads7830(7))/512) * 180
        #servoY.angle = read_ads7830(6)
        sleep(0.1)

    pause()

except KeyboardInterrupt:
    pass

finally:
    servoX.angle = 0
