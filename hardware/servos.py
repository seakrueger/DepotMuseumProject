import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.continuous_servo[0].throttle = -0.05
kit.continuous_servo[1].throttle = 0.1
time.sleep(30)
kit.continuous_servo[0].throttle = 0
kit.continuous_servo[1].throttle = 0
