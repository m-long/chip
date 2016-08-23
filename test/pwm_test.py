import CHIP_IO.GPIO as GPIO
import CHIP_IO.SOFTPWM as SPWM
import time

# Setup the pins
GPIO.setup("XIO-P0", GPIO.OUT)
GPIO.setup("XIO-P1", GPIO.OUT)
SPWM.start("XIO-P7", 100, 100, 0)

# Run the test
try:
    GPIO.output("XIO-P0", GPIO.HIGH)
    GPIO.output("XIO-P1", GPIO.LOW)

    print("Testing duty cycle...")

    # Test duty cycle
#    for x in range(0,100):
#        SPWM.set_duty_cycle("XIO-P7", x)
#        print(x)
#        time.sleep(.1)

    # Test frequency
    SPWM.set_duty_cycle("XIO-P7", 50)
    print("Testing frequency at 50% duty")
    for f in range(100,5000,100):
        SPWM.set_frequency("XIO-P7", f)
        print(f)
        time.sleep(.1)

    # Hold at high 50%
    print("Holding high at 50% duty")
    SPWM.set_duty_cycle("XIO-P7", 50)
    SPWM.set_frequency("XIO-P7", 5000)

    time.sleep(3)

    # Hold at high 100%
    print("Holding high at 100% duty")
    SPWM.set_duty_cycle("XIO-P7", 100)
    SPWM.set_frequency("XIO-P7", 5000)

    time.sleep(3)

    # Try higher frequency
    print("Holding high at 10000Hz")
    SPWM.set_frequency("XIO-P7", 10000)

    time.sleep(3)

except:
    print("An error hath occurred.")

# Cleanup afterwards
SPWM.stop("XIO-P7")
SPWM.cleanup()
GPIO.cleanup()
