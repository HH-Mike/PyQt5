import sys
import Buddy
from PyQt5.QtWidgets import QApplication,QMainWindow
#Alt+A B C 热键
if __name__ == '__main__':
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui=Buddy.Ui_MainWindow()
    #向主窗口添加控件
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

