import time
import logging

class Display:
    def __init__(self, wait):
        self.wait_time = wait

    def button_one(self):
        logging.debug("Started button 1")
        self.wait()
        logging.debug("Released button 1")

    def button_two(self):
        logging.debug("Started button 2")
        self.wait()
        logging.debug("Released button 2")

    def button_three(self):
        logging.debug("Started button 3")
        self.wait()
        logging.debug("Released button 3")

    def wait(self):
        time.sleep(self.wait_time)