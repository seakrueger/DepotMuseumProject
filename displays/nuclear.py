from adafruit_servokit import ServoKit

from hardware.single_led import LED
from displays.display import Display

class Nuclear(Display):
    def __init__(self, wait):
        super().__init__(wait)

        self.servo_kit = ServoKit(channels=16)

    def button_one(self):
        self.servo_kit.continuous_servo[0].throttle = 0.5

        super().wait()

        self.servo_kit.continuous_servo[0].throttle = 0