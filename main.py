import threading
from queue import Queue
import sys

from hardware.buttons import ButtonHandler
from Ui.video_handler import VideoHandler
from displays.wind_water import WindNWater 


def main():
    display = WindNWater(5)
    
    q = Queue()
    buttons = ButtonHandler(display, q)
    video = VideoHandler(["timer.mov", "timer2.mov", "WindWater/windmill_idle.mp4"], q)
    
    threading.Thread(target=buttons.run, args=()).start()
    threading.Thread(target=video.run, args=()).start()    

if __name__ == "__main__":
    main()