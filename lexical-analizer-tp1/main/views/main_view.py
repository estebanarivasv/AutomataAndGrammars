from PyQt5.QtWidgets import QLabel, QMainWindow
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Lexical analyzer")

        label = QLabel("Select an option for a lexical analyzer:\n1. Email\n2. URL\n3. IP address\n4. Secure "
                       "password\n5. Exit")

        # The `Qt` namespace has a lot of attributes to customise
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label.setAlignment(Qt.AlignCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(label)
