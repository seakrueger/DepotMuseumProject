import time
import os

from Ui.assets.video_player import VLC


def log_input(queue):
	vlc = VLC()
	
	while True:
		data = queue.get()
		print(data)
		
		if data == 1:
			vlc.play("timer.mp4")
		if data == 2:
			vlc.play("timer2.mp4")

		time.sleep(0.1)