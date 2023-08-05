# import sys
# from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow
# from PyQtGuiLib.header import Qt,qt
#
# class Tol(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.resize(600, 600)
#
#         self.setMouseTracking(True)
#         self.setWindowFlags(qt.FramelessWindowHint)
#         self.setAttribute(qt.WA_TranslucentBackground,True)
#
#         self.setStyleSheet('''
#         background-color:rgb(0, 170, 0);
#         ''')
#
#     def mouseMoveEvent(self, e) -> None:
#         print(e.pos())
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = Tol()
#     win.show()
#
#     sys.exit(app.exec_())

s = [1,1,2,3]
old_n = len(s)
s.extend([2,4,56,1])
for i in range(old_n,len(s)):
    print(i)