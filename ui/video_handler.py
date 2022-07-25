import time
import os
from queue import Queue

from ui.video_player import Player

class VideoHandler:
	def __init__(self, queue: Queue):
		self.videos = ["pres1.wmv", "pres2.wmv", "pres3.wmv"]
		self.queue = queue

		self.vlc = Player()
		
	def run(self):
		while True:
			data = self.queue.get()
			self.vlc.play(self.videos[data])
