from adafruit_motorkit import MotorKit
import board
import time

from displays.display import Display

class WindNWater(Display):
    def __init__(self, wait):
        super().__init__(wait)

        self.wind_kit = MotorKit(i2c=board.I2C())
        self.wind_motors = [self.wind_kit.motor1, self.wind_kit.motor2, self.wind_kit.motor3, self.wind_kit.motor4]
        
        self.water_kit = MotorKit(i2c=board.I2C(), address=0x61)

    # Water Wheel
    def button_one(self):
        self.water_kit.motor1.throttle  = 0.1

        super().wait()

        self.water_kit.motor1.throttle = 0

    # Wind Turbines
    def button_two(self):
        for motor in self.wind_motors:
            motor.throttle = 0.2

        super().wait()

        # Stop the 4 motors
        for motor in self.wind_motors:
            motor.throttle = 0

    # Dam
    def button_three(self):
        self.water_kit.motor2.throttle = 0.4

        super().wait()

        self.water_kit.motor2.throttle = 0