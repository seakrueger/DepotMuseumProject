import os
import time
import logging
from vlc import MediaPlayer, Media

class Player():
    def __init__(self):
        self.player = MediaPlayer()
        self.player.toggle_fullscreen()

        self.playing = False
        self.path = os.path.dirname(__file__) + "/assets/" + os.environ.get('USER')

    def play(self, media):
        video = Media(os.path.join(self.path, media))
        self.player.set_media(video)
        self.player.play()

        self._wait_for_finish()
        logging.debug("finished")

    def _wait_for_finish(self):
        while self.player.get_state() not in {5, 6, 7}:
            time.sleep(0.1)
