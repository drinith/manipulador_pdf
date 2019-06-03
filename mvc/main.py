from sys import exit,argv
from PyQt5.QtWidgets import QApplication
from viewPDF import View
if __name__ == '__main__':
    
    app = QApplication(argv)
    ex = View()
    exit(app.exec_())