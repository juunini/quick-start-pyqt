import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Main(QMainWindow):
        def __init__(self):
                super().__init__()

                window = QWidget()
                main = QVBoxLayout()
                window.setLayout(main)
                self.setCentralWidget(window)
                
                window.setStyleSheet("QWidget{background: #000;color: #747a81}")
                main.setContentsMargins(50, 50, 50, 50)
                main.setSpacing(20)

                #layout area------------------------------------

                import layout
                main.addWidget(layout.titleDiv)
                main.addWidget(layout.mainDiv)

                #layout area end------------------------------------

                #active area-----------------------------------

                

                #active area end---------------------------------
                #크기 설정
                self.setGeometry(300,100,800,0)
                #제목 설정
                self.setWindowTitle("title");
                self.show()

if __name__ == "__main__":
        app = QApplication(sys.argv)
        do = Main()
        sys.exit(app.exec_())
