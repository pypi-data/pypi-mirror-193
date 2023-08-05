import random

import PySide2

from PyQtGuiLib.header import (
    PYQT_VERSIONS,
    QApplication,
    sys,
    QWidget,
    qt,
    QPushButton,
    Qt,
    QPalette,
    QColor,
    QPaintEvent,
    QPainter,
    QBrush,
    QSize,
    QMainWindow,
    QLineEdit,
    desktopCenter,
    QPixmap,
    QFrame,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy,
    QMouseEvent,
    Signal
)
from PyQt5.QtCore import QObject

class Btn(QPushButton):
    c_click = Signal(QPushButton)
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.__set_sty()
        # self.setFixedSize(50, 30)
        self.setAttribute(Qt.WA_Hover,True)

    def __set_sty(self):
        self.setStyleSheet("""
            QPushButton{
            border: none;
            border-radius:3px;
            color: rgba(255, 255, 255, 255);
            font-size:16px;
            background-color: rgb(255, 0, 127);}
            QPushButton:hover{
            background-color: rgb(0, 0, 0);}
            """)

    def leaveEvent(self, event) -> None:
        self.setStyleSheet("""
            QPushButton{
            border: none;
            border-radius:3px;
            color: rgba(255, 255, 255, 255);
            font-size:16px;
            background-color: rgb(255, 0, 127);}
            QPushButton:hover{
            background-color: rgb(0, 0, 0);}
            """)

    def mousePressEvent(self, e: QMouseEvent) -> None:
        self.c_click.emit(self)
        self.deleteLater()
        super(Btn, self).mousePressEvent(e)


class TestHover(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.setMouseTracking(True)

        self.spa = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.btns = []
        btn = Btn("我我我我我我我我我我我我我我", self)
        btn.c_click.connect(self.test)
        self.btns.append(btn)
        for i in range(10):
            btn = Btn(self.random_string(), self)
            btn.c_click.connect(self.test)
            self.btns.append(btn)
        for t in self.btns:
            self.layout.addWidget(t)
        self.layout.addItem(self.spa)

    def random_string(self, text="我", max_length=3):
        length = random.randint(1, max_length)
        return text * length

    def test(self,obj:QPushButton):
        index = self.btns.index(obj)
        if index+1 < len(self.btns):
            next_obj = self.btns[index+1]
            next_obj.setStyleSheet(next_obj.styleSheet())
            next_obj.setStyleSheet('''
    QPushButton{
                border: none;
                border-radius:3px;
                color: rgba(255, 255, 255, 255);
                font-size:16px;
                background-color: rgb(0, 0, 0);
    }
    QPushButton:hover{

            background-color: rgb(255, 0, 127);
    }
            ''')

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = TestHover()
    win.show()

    if PYQT_VERSIONS in ["PyQt6","PySide6"]:
        sys.exit(app.exec())
    else:
        sys.exit(app.exec_())