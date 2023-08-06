from RPi import GPIO

from .rpigpio import RPiGPIO
from .rpigpiofloat import RPiGPIOFloat


VERSION = '1.1.3'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
