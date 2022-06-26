from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout, QWidget)

class VideoPlayer(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addWidget(self.errorLabel)

        self.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.error.connect(self.handleError)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

    def playFile(self, fileName):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
       
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.setWindowTitle("Player")
    player.resize(1280, 720)
    player.show()
    player.playFile("/home/pi/source/Ui/images/timer.mp4")
    sys.exit(app.exec_())