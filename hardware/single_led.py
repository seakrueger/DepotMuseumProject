import board
import time
import RPi.GPIO as GPIO

# Simple LED Handler
class LED():
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

        self.pin = pin

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def flash(self, delay, num_flashes):
        n = 0
        while n < num_flashes: 
            self.on()
            time.sleep(delay)
            self.off()
            time.sleep(delay)

            n += 1

        self.off()
