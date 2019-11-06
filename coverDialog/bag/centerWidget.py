# _*_ coding:utf-8 _*_
# __Author__： zizle


from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtWidgets import QWidget, QPushButton


class CenterDrawer(QWidget):
    def __init__(self, *args, **kwargs):
        super(CenterDrawer, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.animation = QPropertyAnimation(self, b'windowOpacity')
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setDuration(1000)
        # self.setText('阿斯顿发敬爱欧迪芬')
        self.resize(200, 300)
        self.setStyleSheet('background:rgb(247,247,247)')




