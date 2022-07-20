import threading
from queue import Queue
import sys

from hardware.buttons import ButtonHandler
from Ui.video_handler import VideoHandler
<<<<<<< HEAD
from displays.display import Display 


def main():
    display = Display(5)
=======
from displays.nuclear import Nuclear 


def main():
    display = Nuclear(5)
>>>>>>> a639958 (nuclear main.py)
    
    q = Queue()
    buttons = ButtonHandler(display, q)
    video = VideoHandler(["timer.mov", "timer2.mov", "WindWater/windmill_idle.mp4"], q)
    
    threading.Thread(target=buttons.run, args=()).start()
    threading.Thread(target=video.run, args=()).start()    

if __name__ == "__main__":
    main()
