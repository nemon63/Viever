from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSlider, QLabel, QStyle, QFileDialog
from PyQt5.QtCore import QTimer, Qt, pyqtSignal
import vlc

class VideoPlayer(QWidget):
    time_changed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()

        self.videoframe = QWidget(self)
        self.videoframe.setStyleSheet("background-color: black;")
        self.mediaplayer.set_hwnd(self.videoframe.winId())

        self.positionSlider = QSlider(Qt.Horizontal, self)
        self.positionSlider.setToolTip("Position")
        self.positionSlider.setMaximum(1000)
        self.positionSlider.sliderMoved.connect(self.set_position)

        self.timeLabel = QLabel("00:00:00", self)

        self.openButton = QPushButton(self.style().standardIcon(QStyle.SP_DialogOpenButton), "", self)
        self.playButton = QPushButton(self.style().standardIcon(QStyle.SP_MediaPlay), "", self)
        self.pauseButton = QPushButton(self.style().standardIcon(QStyle.SP_MediaPause), "", self)
        self.stopButton = QPushButton(self.style().standardIcon(QStyle.SP_MediaStop), "", self)

        self.openButton.clicked.connect(self.openFile)
        self.playButton.clicked.connect(self.playVideo)
        self.pauseButton.clicked.connect(self.pauseVideo)
        self.stopButton.clicked.connect(self.stopVideo)

        controlLayout = QHBoxLayout()
        controlLayout.addWidget(self.openButton)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.pauseButton)
        controlLayout.addWidget(self.stopButton)
        controlLayout.addWidget(self.positionSlider)
        controlLayout.addWidget(self.timeLabel)

        self.controlWidget = QWidget(self)
        self.controlWidget.setLayout(controlLayout)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.videoframe)
        self.layout.addWidget(self.controlWidget)
        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 0)

        self.setLayout(self.layout)

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_ui)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi *.mkv)")
        if fileName != '':
            self.media = self.instance.media_new(fileName)
            self.mediaplayer.set_media(self.media)
            self.media.parse()
            self.setWindowTitle(self.media.get_meta(0))
            self.playVideo()

    def playVideo(self):
        if self.mediaplayer.get_media():
            self.mediaplayer.play()
            self.timer.start()

    def pauseVideo(self):
        self.mediaplayer.pause()
        self.time_changed.emit()

    def stopVideo(self):
        self.mediaplayer.stop()
        self.time_changed.emit()

    def set_position(self, position):
        self.mediaplayer.set_position(position / 1000.0)
        self.time_changed.emit()

    def update_ui(self):
        media_pos = self.mediaplayer.get_position() * 1000
        self.positionSlider.setValue(media_pos)

        time = self.mediaplayer.get_time() / 1000
        mins, secs = divmod(time, 60)
        hours, mins = divmod(mins, 60)
        self.timeLabel.setText(f"{int(hours):02}:{int(mins):02}:{int(secs):02}")

        self.time_changed.emit()

        if not self.mediaplayer.is_playing():
            self.timer.stop()
            if self.mediaplayer.get_position() >= 0.99:
                self.positionSlider.setValue(0)
