from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSplitter
from PyQt5.QtCore import Qt
from ui_components.text_editors import TextEditors
from ui_components.media_widgets import MediaWidgets

class RightPane(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.splitter = QSplitter(Qt.Vertical)
        self.layout.addWidget(self.splitter)

        self.media_widgets = MediaWidgets(self.main_window)
        self.splitter.addWidget(self.media_widgets)

        self.text_editors = TextEditors(self.main_window)
        self.splitter.addWidget(self.text_editors)
