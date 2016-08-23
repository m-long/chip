import CHIP_IO.GPIO as GPIO
import time

GPIO.setup("GPIO3", GPIO.OUT)
GPIO.setup("GPIO4", GPIO.IN)

GPIO.output("GPIO3", GPIO.HIGH)

if GPIO.input("GPIO4"):
	print("HIGH")
else:
	print("LOW")

time.sleep(2)

GPIO.cleanup()
