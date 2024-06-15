from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton

class TextEditors(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLineEdit

class TextEditors(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.text_edit_descript = QTextEdit()
        self.text_edit_descript.textChanged.connect(self.main_window.save_description)
        self.layout.addWidget(self.text_edit_descript)

        self.horizontal_layout_2 = QHBoxLayout()
        self.text_edit_comment = QTextEdit()
        self.text_edit_code = QTextEdit()
        self.horizontal_layout_2.addWidget(self.text_edit_comment)
        self.horizontal_layout_2.addWidget(self.text_edit_code)
        self.layout.addLayout(self.horizontal_layout_2)

        self.text_edit_comment.installEventFilter(self)
        self.text_edit_code.installEventFilter(self)

        self.horizontal_layout_3 = QHBoxLayout()
        self.pbt_save = QPushButton("Сохранить")
        self.pbt_save.clicked.connect(self.main_window.save_changes)
        self.horizontal_layout_3.addWidget(self.pbt_save)
        self.pbt_load = QPushButton("Загрузить")
        self.pbt_load.clicked.connect(self.main_window.load_changes)
        self.horizontal_layout_3.addWidget(self.pbt_load)
        self.layout.addLayout(self.horizontal_layout_3)

        self.text_edit_tags = QLineEdit()
        self.text_edit_tags.setPlaceholderText("Теги (разделяйте пробелами)")
        self.layout.addWidget(self.text_edit_tags)

        self.text_edit_descript = QTextEdit()
        self.text_edit_descript.textChanged.connect(self.main_window.save_description)
        self.layout.addWidget(self.text_edit_descript)

        self.horizontal_layout_2 = QHBoxLayout()
        self.text_edit_comment = QTextEdit()
        self.text_edit_code = QTextEdit()
        self.horizontal_layout_2.addWidget(self.text_edit_comment)
        self.horizontal_layout_2.addWidget(self.text_edit_code)
        self.layout.addLayout(self.horizontal_layout_2)

        self.text_edit_comment.installEventFilter(self.main_window)
        self.text_edit_code.installEventFilter(self.main_window)

        self.horizontal_layout_3 = QHBoxLayout()
        self.pbt_save = QPushButton("Сохранить")
        self.pbt_save.clicked.connect(self.main_window.save_changes)
        self.horizontal_layout_3.addWidget(self.pbt_save)
        self.pbt_load = QPushButton("Загрузить")
        self.pbt_load.clicked.connect(self.main_window.load_changes)
        self.horizontal_layout_3.addWidget(self.pbt_load)
        self.layout.addLayout(self.horizontal_layout_3)
