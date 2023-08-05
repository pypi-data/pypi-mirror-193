from PyQt5.QtCore import (QEasingCurve, QPoint, QPropertyAnimation, Qt,
                          QTimer)
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QGraphicsDropShadowEffect,
                             QGraphicsOpacityEffect)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget


class Tip(QWidget):
    def __init__(self, trip: int, content: str, icon: str, parent=None):
        super().__init__(parent)
        self.trip = trip
        self._translate = QtCore.QCoreApplication.translate
        self.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 48))
        self.frame.setStyleSheet("QFrame{\n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 "    border:none;\n"
                                 "    border-radius:12px;\n"
                                 "    font: 16px \"MiSans\";\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(14, -1, 16, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(f":[表情]ttom/img/svg/tip{icon}.svg"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setText(self._translate("Form", content))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.adjustSize()
        self.setFixedSize(self.width(), 66)
        self.opacityEffect = QGraphicsOpacityEffect(self)
        self.opacityAni = QPropertyAnimation(self.opacityEffect, b"opacity")
        self.slideAni = QPropertyAnimation(self, b'pos')
        self.setAttribute(Qt.WA_StyledBackground)
        self.closeTimer = QTimer(self)
        self.closeTimer.setInterval(2000)
        self.frame.setGraphicsEffect(
            QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QColor('#D2CECD')))
        self.opacityEffect.setOpacity(1)
        self.closeTimer.timeout.connect(self.__fade_out)

    def __fade_out(self):
        self.opacityAni.setDuration(1000)
        self.opacityAni.setStartValue(1)
        self.opacityAni.setEndValue(0)
        self.opacityAni.finished.connect(self.deleteLater)
        self.opacityAni.start()

    def getSuitablePos(self):
        for i in range(10):
            dy = i * (self.height() + 20)
            pos = QPoint((self.window().width() - self.width()) / 2, self.trip + dy)
            widget = self.window().childAt(pos + QPoint(2, 2))
            if isinstance(widget, (Tip)):
                pos += QPoint(0, self.height() + 20)
            else:
                break
        return pos

    def showEvent(self, e):
        pos = self.getSuitablePos()
        self.slideAni.setDuration(200)
        self.slideAni.setEasingCurve(QEasingCurve.OutQuad)
        self.slideAni.setStartValue(QPoint((self.window().width() - self.width()) / 2, self.height() - 60))
        self.slideAni.setEndValue(pos)
        self.slideAni.start()
        super().showEvent(e)
        self.closeTimer.start()



