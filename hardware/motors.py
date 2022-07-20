from adafruit_motorkit import MotorKit
import board
import time

# A program for testing motors

kit = MotorKit(i2c=board.I2C(), address=0x60)

m = kit.motor1

m.throttle = 0.5
time.sleep(2)
m.throttle = 0
