import CHIP_IO.GPIO as GPIO
import CHIP_IO.OverlayManager as OM
import CHIP_IO.PWM as PWM
import time

# Initialize hardware pwm thorugh the OM
OM.enable_debug()
OM.load("PWM0")

# Test it loaded properly
if(OM.get_pwm_loaded()):
    print("PWM OM Successfully loaded...")

# Setup the pins
GPIO.setup("XIO-P0", GPIO.OUT)
GPIO.setup("XIO-P1", GPIO.OUT)
PWM.start("PWM0", 100, 100, 0)

# Run the test
try:
    GPIO.output("XIO-P0", GPIO.HIGH)
    GPIO.output("XIO-P1", GPIO.LOW)

    print("Testing duty cycle...")

    # Test duty cycle
#    for x in range(0,100):
#        SPWM.set_duty_cycle("PWM0", x)
#        print(x)
#        time.sleep(.1)

    # Test frequency
    PWM.set_duty_cycle("PWM0", 100)
    print("Testing frequency at 100% duty")
    for f in range(100,5000,100):
        PWM.set_frequency("PWM0", f)
        print(f)
        time.sleep(.1)

    # Hold at high
    print("Holding high")
    PWM.set_duty_cycle("PWM0", 100)
    PWM.set_frequency("PWM0", 5000)

    time.sleep(3)

except:
    print("An error hath occurred.")

# Cleanup afterwards
PWM.stop("PWM0")
PWM.cleanup()
OM.unload("PWM0")
GPIO.cleanup()
