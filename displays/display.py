import time

class Display:
    def __init__(self, wait):
        self.wait_time = wait

    def button_one(self):
        print("Started button 1")
        self.wait()
        print("Released button 1")

    def button_two(self):
        print("Started button 2")
        self.wait()
        print("Released button 2")

    def button_three(self):
        print("Started button 3")
        self.wait()
        print("Released button 3")

    def wait(self):
        time.sleep(self.wait_time)