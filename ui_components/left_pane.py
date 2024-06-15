from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QTreeView
from PyQt5.QtCore import Qt

class LeftPane(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.initControls()
        self.initTreeView()

    def initControls(self):
        self.controls_layout = QHBoxLayout()

        self.btn_open = QPushButton("Выберите папку")
        self.btn_open.clicked.connect(self.main_window.open_folder)
        self.controls_layout.addWidget(self.btn_open)

        self.pbt_reviewed = QPushButton("Отметить как просмотренно")
        self.pbt_reviewed.clicked.connect(self.main_window.mark_as_reviewed)
        self.controls_layout.addWidget(self.pbt_reviewed)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Поиск...")
        self.search_bar.textChanged.connect(self.main_window.filter_tree_view)
        self.controls_layout.addWidget(self.search_bar)

        self.theme_selector = QComboBox()
        self.theme_selector.addItems(["Светлая тема", "Темная тема"])
        self.theme_selector.currentIndexChanged.connect(self.main_window.change_theme)
        self.controls_layout.addWidget(self.theme_selector)

        self.layout.addLayout(self.controls_layout)

    def initTreeView(self):
        self.tree_view = QTreeView()
        self.tree_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree_view.customContextMenuRequested.connect(self.main_window.open_menu)
        self.tree_view.doubleClicked.connect(self.main_window.on_tree_view_double_clicked)
        self.tree_view.clicked.connect(self.main_window.on_tree_view_clicked)
        self.tree_view.header().setSortIndicatorShown(True)
        self.tree_view.header().setSectionsClickable(True)
        self.tree_view.header().sectionClicked.connect(self.main_window.sort_tree_view)
        self.layout.addWidget(self.tree_view)
