import time
import board
import digitalio
from queue import Queue
from adafruit_seesaw.seesaw import Seesaw
from adafruit_seesaw.digitalio import DigitalIO
from adafruit_seesaw.pwmout import PWMOut

from displays.display import Display

class ButtonHandler():
    def __init__(self, args, display: Display, queue: Queue, delay=0.01, addr=0x3A):
        super().__init__()
        
        self.args = args
        self.display = display
        self.queue = queue

        self.delay = delay
        self.i2c = board.I2C()

        # For the QT Py RP2040, QT Py ESP32-S2, other boards that have SCL1/SDA1 as the STEMMA QT port.
        # import busio
        # i2c = busio.I2C(board.SCL1, board.SDA1)
        self.arcade_qt = Seesaw(self.i2c, addr=addr)

        # Button pins in order (1, 2, 3, 4)
        button_pins = (18, 19, 20, 2)
        self.buttons = []
        for button_pin in button_pins:
            button = DigitalIO(self.arcade_qt, button_pin)
            button.direction = digitalio.Direction.INPUT
            button.pull = digitalio.Pull.UP
            self.buttons.append(button)

        # LED pins in order (1, 2, 3, 4)
        led_pins = (12, 13, 0, 1)
        self.leds = []
        for led_pin in led_pins:
            led = PWMOut(self.arcade_qt, led_pin)
            self.leds.append(led)

    def _pulse_on(self, led_num):
        for cycle in range(0, 65535, 2000):
                self.leds[led_num].duty_cycle = cycle
                time.sleep(self.delay)

    def _pulse_off(self, led_num):
        for cycle in range(65534, 0, -2000):
                self.leds[led_num].duty_cycle = cycle
                time.sleep(self.delay)

    def run(self):
        while True:
            if not self.buttons[0].value:
                self._pulse_on(0)

                if self.args.video:
                    self.queue.put(0)
                if self.args.model:
                    self.display.button_one()
                
                self._pulse_off(0)

            if not self.buttons[1].value:
                self._pulse_on(1)
                
                if self.args.video:
                    self.queue.put(1)
                if self.args.model:
                    self.display.button_two()
                
                self._pulse_off(1)
            
            if not self.buttons[2].value:
                self._pulse_on(2)
                
                if self.args.video:
                    self.queue.put(2)
                if self.args.model:
                    self.display.button_three()
                
                self._pulse_off(2)
