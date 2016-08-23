import CHIP_IO.GPIO as GPIO
import CHIP_IO.SOFTPWM as SPWM
import time

# Pre-clean for test
# GPIO.cleanup()
# SPWM.stop("XIO-P7")
# SPWM.cleanup()

# Setup the pins
GPIO.setup("XIO-P0", GPIO.OUT)
GPIO.setup("XIO-P1", GPIO.OUT)
SPWM.start("XIO-P7", 100, 1000, 0)
# GPIO.setup("XIO-P7", GPIO.OUT)
# GPIO.output("XIO-P7", GPIO.HIGH)

GPIO.output("XIO-P0", GPIO.HIGH)
GPIO.output("XIO-P1", GPIO.LOW)

time.sleep(5)

SPWM.stop("XIO-P7")
GPIO.cleanup()
SPWM.cleanup()
