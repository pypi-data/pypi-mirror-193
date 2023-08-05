from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyComboBox(QComboBox):
    def paintEvent(self, event):
        painter = QStylePainter(self)
        option = QStyleOptionComboBox()
        option.initFrom(self)

        # 设置自定义背景颜色
        option.palette.setColor(QPalette.Window, QColor(48, 63, 159))

        # 绘制自定义背景
        painter.drawComplexControl(QStyle.CC_ComboBox, option)

        # 绘制下拉箭头
        arrowRect = self.style().subControlRect(QStyle.CC_ComboBox, option, QStyle.SC_ComboBoxArrow, self)
        painter.drawPixmap(arrowRect, QPixmap('arrow.png'))

        # 绘制文本
        textRect = self.style().subControlRect(QStyle.CC_ComboBox, option, QStyle.SC_ComboBoxEditField, self)
        painter.drawText(textRect, Qt.AlignLeft | Qt.AlignVCenter, self.currentText())

    def sizeHint(self):
        # 重写 sizeHint() 方法以便更好地适应自定义样式
        return QSize(120, 22)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    combo = MyComboBox()
    combo.addItems(['Item 1', 'Item 2', 'Item 3'])
    combo.show()

    sys.exit(app.exec_())
