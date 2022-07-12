import threading
from queue import Queue
import sys

from hardware.buttons import ButtonHandler
from displays.display import Display 
import status

def main():
    display = Display(5)
    
    q = Queue()
    buttons = ButtonHandler(display, q)
    
    threading.Thread(target=buttons.run, args=()).start()
    threading.Thread(target=status.log_input, args=(q, )).start()    

if __name__ == "__main__":
    main()