from buildhat import Motor

from displays.display import Display

class Coal(Display):
    def __init__(self, wait):
        super().__init__(wait)

        self.motor_a = Motor("A")
        self.motor_b = Motor("B")

        self.motor_b.set_default_speed(25)
        self.motor_a.set_default_speed(5)

    def button_one(self):
        self.motor_b.start()

        self.wait()

        self.motor_b.stop()

    def button_two(self):
        self.motor_a.start()

        self.wait()

        self.motor_a.stop()
