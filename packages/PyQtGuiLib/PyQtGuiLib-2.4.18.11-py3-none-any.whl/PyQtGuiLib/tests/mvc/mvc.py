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
    QLinearGradient,
    QLabel,
    QFont,
    textSize,
    QFontMetricsF,
    Qt,
    QMouseEvent,
    QTableWidget,
    QTableWidgetItem,

    QStyledItemDelegate,
    QStyleOptionViewItem,
    QModelIndex,
    QAbstractItemModel,
    QStyle,
    QPalette,

    QSpinBox,
    QAbstractItemView
)

# QSplashScreen
'''
    测试用例的标准模板,该代码用于复制
'''
from PyQtGuiLib.core.resolver import dumpStructure

class ItemDelegate(QStyledItemDelegate):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def createEditor(self, parent, option:QStyleOptionViewItem, index:QModelIndex):
        # print(parent)
        btn = QSpinBox(parent)
        return btn

    # def setEditorData(self, editor:QSpinBox, index:QModelIndex):
    #     n = int(index.model().data(index))
    #     print("-->",n)
    #     editor.setValue(n+10)

    def setModelData(self, editor:QSpinBox, model:QAbstractItemModel, index):

        v = editor.value()
        print(v)
        model.setData(index,v)


#     def updateEditorGeometry(self, editor:QSpinBox, option:QStyleOptionViewItem, index):
#         editor.setStyleSheet('''
# background-color: rgb(25, 25, 25);
#         ''')
#         editor.setGeometry(option.rect)

    def paint(self, painter:QPainter, option:QStyleOptionViewItem, index:QModelIndex):
        print(painter)
        # print(option.state,QStyle.State_Selected)
        painter.fillRect(option.rect,option.palette.highlight())

        # painter.drawText(10,10,"hello")
        super(ItemDelegate, self).paint(painter,option,index)

class Test(QTableWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.resize(600,600)
        self.setColumnCount(5)
        self.setRowCount(5)
        self.setMouseTracking(True)
        self.setStyleSheet('''
QTableView::item:hover{
background-color: rgb(7, 64, 128);
}
        ''')
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.setSelectionMode(QAbstractItemView.SingleSelection)
        item = QTableWidgetItem("10")
        itemdel = ItemDelegate()
        self.setItemDelegate(itemdel)

        self.setItem(0,0,item)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = Test()
    win.show()

    if PYQT_VERSIONS in ["PyQt6","PySide6"]:
        sys.exit(app.exec())
    else:
        sys.exit(app.exec_())