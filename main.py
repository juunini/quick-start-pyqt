import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Main(QMainWindow):
	def __init__(self):
		super().__init__()

		window = QWidget()
		import layout
		window.setLayout(layout.main)

		self.setCentralWidget(window)

		#크기 설정
		self.setGeometry(300,100,800,0)
		#제목 설정
		self.setWindowTitle("SQLi-diot");
		self.show()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	do = Main()
	sys.exit(app.exec_())
