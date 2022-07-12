from adafruit_motorkit import MotorKit
import board
import time

# A program for testing motors

kit = MotorKit(i2c=board.I2C(), address=96)

kit.motor1.throttle = 0.5
time.sleep(2)
kit.motor1.throttle = 0