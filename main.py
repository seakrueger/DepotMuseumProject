import threading
from queue import Queue
import sys
from PyQt5.QtWidgets import QApplication

from default_window import DefualtWindow
from hardware.buttons import ButtonHandler
from displays.display import Display 
import status


def start_ui(queue):
    app = QApplication(sys.argv)
    window = DefualtWindow(queue)
    window.show()
    sys.exit(app.exec())

def main():
    q = Queue()
    display = Display(5)

    buttons = ButtonHandler(display, q)
    
    threading.Thread(target=buttons.run, args=()).start()
    threading.Thread(target=status.log_input, args=(q, )).start()
    #start_ui(q)
    

if __name__ == "__main__":
    main()