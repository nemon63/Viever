from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from video_player import VideoPlayer

class MediaWidgets(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.video_player = VideoPlayer(self.main_window)
        self.video_player.setMinimumSize(800, 600)
        self.layout.addWidget(self.video_player)

        self.image_label = QLabel("image")
        self.image_label.setFrameShape(QLabel.Panel)
        self.image_label.setFrameShadow(QLabel.Plain)
        self.image_label.setLineWidth(1)
        self.image_label.setMidLineWidth(1)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumSize(800, 600)
        self.image_label.setScaledContents(True)
        self.layout.addWidget(self.image_label)
