import threading
from queue import Queue
import sys

from hardware.buttons import ButtonHandler
from Ui.video_handler import VideoHandler
from displays.display import Display 


def main():
    display = Display(5)
    
    q = Queue()
    buttons = ButtonHandler(display, q)
    video = VideoHandler(["timer.mp4", "timer2.mp4", "WindWater/windmill_idle.mp4"], q)
    
    threading.Thread(target=buttons.run, args=()).start()
    threading.Thread(target=video.run, args=()).start()    

if __name__ == "__main__":
    main()