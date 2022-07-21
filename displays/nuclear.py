from adafruit_servokit import ServoKit

from hardware.led import LED
from displays.display import Display

class Nuclear(Display):
    def __init__(self, wait):
        super().__init__(wait)

        self.servo_kit = ServoKit(channels=16)
        self.reactor = LED(26)

    def button_one(self):
        self.reactor.flash(10)
        self.reactor.on()

        self.wait()

        self.reactor.off()

    def button_two(self):
        self.servo_kit.continuous_servo[0].throttle = 0.5

        self.wait()

        self.servo_kit.continuous_servo[0].throttle = 0

    def button_three(self):
        self.servo_kit.continuous_servo[1].throttle = -0.1

        self.wait()

        self.servo_kit.continuous_servo[1].throttle = 0