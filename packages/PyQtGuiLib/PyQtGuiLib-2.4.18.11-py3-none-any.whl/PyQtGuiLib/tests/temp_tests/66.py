from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
import sys

class FollowThread(QThread):
    update_position = pyqtSignal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent

    def run(self):
        while True:
            x = self.main_window.x()
            y = self.main_window.y()
            self.update_position.emit(x, y)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel('Follow Me!',self)
        self.follow_thread = FollowThread(self)
        self.follow_thread.update_position.connect(self.update_label_position)
        self.follow_thread.start()
        self.label.show()
        self.show()

    def update_label_position(self, x, y):
        self.label.move(x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
