from vlc import MediaPlayer, Media
import os
import time

class Player():
    def __init__(self):
        self.player = MediaPlayer()
        self.player.toggle_fullscreen()

        self.playing = False
        self.path = os.path.dirname(__file__) + "/assets/"

    def play(self, media):
        video = Media(os.path.join(self.path, media))
        self.player.set_media(video)
        self.player.play()

        self.playing = True
        if self._is_finished():     
            print("finished media")

    def _is_finished(self):
        while self.playing:
            state = self.player.get_state()
            if state == 6 or state == 7:
                self.playing = False
                return True

            time.sleep(0.1)    