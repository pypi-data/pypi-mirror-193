from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStyle
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt

class MyStyle(QStyle):
    def drawControl(self, control, option, painter, widget=None):
        if control == QStyle.CE_PushButton:
            painter.save()
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setBrush(QBrush(QColor(100, 100, 100, 100)))
            painter.setPen(QPen(QColor(0, 0, 0, 0)))
            painter.drawRoundedRect(option.rect.adjusted(5, 5, -5, -5), 5, 5)
            painter.restore()
        else:
            super().drawControl(control, option, painter, widget)

    def pixelMetric(self, metric, option=None, widget=None):
        if metric == QStyle.PM_ButtonMargin:
            return 10
        else:
            return super().pixelMetric(metric, option, widget)

    def styleHint(self, hint, option=None, widget=None, returnData=None):
        if hint == QStyle.SH_Button_FocusPolicy:
            return Qt.StrongFocus
        else:
            return widget.sizeHint()

    def subElementRect(self, element, option, widget=None):
        if element == QStyle.SE_PushButtonContents:
            return option.rect.adjusted(10, 10, -10, -10)
        else:
            return super().subElementRect(element, option, widget)

app = QApplication([])
app.setStyle(MyStyle())

window = QMainWindow()
button = QPushButton("Click Me", window)
button.show()

app.exec_()
