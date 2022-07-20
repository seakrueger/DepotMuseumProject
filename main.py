import threading
import argparse
from queue import Queue

from hardware.buttons import ButtonHandler
from Ui.video_handler import VideoHandler
from displays.display import Display 

def main(args):
    display = Display(5)
    q = Queue()

    buttons = ButtonHandler(args, display, q)
    threading.Thread(target=buttons.run, args=()).start()

    if args.video:
        video = VideoHandler(["timer.mov", "timer2.mov", "WindWater/windmill_idle.mp4"], q)
        threading.Thread(target=video.run, args=()).start()    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", default=True, action=argparse.BooleanOptionalAction)
    parser.add_argument("--model", default=True, action=argparse.BooleanOptionalAction)

    args = parser.parse_args()
    
    main(args)
