import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.continuous_servo[0].throttle = -0.3
kit.continuous_servo[1].throttle = 0.5
time.sleep(5)
kit.continuous_servo[0].throttle = 0
kit.continuous_servo[1].throttle = 0
