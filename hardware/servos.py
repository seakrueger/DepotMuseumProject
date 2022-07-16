import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.continuous_servo[0].throttle = 0.5
time.sleep(2)
kit.continuous_servo[0].throttle = 0