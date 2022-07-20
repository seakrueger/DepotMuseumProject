import time
import os
from queue import Queue

from ui.video_player import Player

class VideoHandler:
	def __init__(self, video_paths: list, queue: Queue):
		self.videos = video_paths
		self.queue = queue

		self.vlc = Player()
		
	def run(self):
		while True:
			data = self.queue.get()
			self.vlc.play(self.videos[data])