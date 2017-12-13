from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import layout

def Widget(QWidget):
	QWidget.setStyleSheet("""
		QWidget{background: #22282e; color: #747a81;}
	""")

def Input(QLineEdit):
	QLineEdit.setStyleSheet("""
		QLineEdit{
			height: 30px;
			padding: 0 20px;
			font-size: 14px;
			font-family: Sansita;
			color: #747a81;
			border-top: 2px solid #101315;
			border-left: 2px solid #101315;
			border-right: 2px solid #242a2f;
			border-bottom: 2px solid #2b3136;
			background: #15181b;
		}
	""")

def TextArea(QTextEdit):
	QTextEdit.setStyleSheet("""
		QTextEdit{
			height: 90px;
			padding: 0 20px;
			font-size: 14px;
			font-family: Sansita;
			color: #747a81;
			border-top: 2px solid #101315;
			border-left: 2px solid #101315;
			border-right: 2px solid #242a2f;
			border-bottom: 2px solid #2b3136;
			background: #15181b;
		}
	""")

def Select(QComboBox):
	QComboBox.setStyleSheet("""
		QComboBox{
			height: 30px;
			padding: 0 20px;
			font-size: 14px;
			color: #747a81;
			border-top: 2px solid #101315;
			border-left: 2px solid #101315;
			border-right: 2px solid #242a2f;
			border-bottom: 2px solid #2b3136;
			background: #15181b;
			font-family: Sansita;
		}
		QComboBox::drop-down{
			border: none;
		}
		QComboBox::down-arrow{
			width: 0;
			height: 0;
			margin-top: 4px;
			margin-right: 10px;
			border: 5px solid #15181b;
			border-top: 5px solid #747a81;
		}
		QComboBox QAbstractItemView{
			border: 2px solid #101315;
		}
	""")
