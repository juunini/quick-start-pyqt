from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from style import *

titleDiv = QWidget()
titleLayout = QHBoxLayout()
titleStat = QLabel()
title = QLabel()
Title(titleDiv, titleLayout, titleStat, title, "테스트", "테스트입니다.")

mainDiv = QWidget()
mainLayout = QVBoxLayout()
Div(mainDiv, mainLayout)
