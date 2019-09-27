# _*_ coding:utf-8 _*_
# Author: zizle

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer


class CustomerProcessBar(QtWidgets.QProgressBar):
    def __init__(self):
        super(CustomerProcessBar, self).__init__()
        self.setValue(0)
        if self.minimum() != self.maximum():
            self.timer = QTimer()
            self.timer.timeout.connect(self.time_out)
            self.timer.start(1000)

    def time_out(self):
        if self.value() >= 100:
            self.timer.stop()
            self.timer.deleteLater()
            del self.timer
            return
        self.setValue(self.value() + 1)


class Surface(QtWidgets.QWidget):
    def __init__(self):
        super(Surface, self).__init__()
        layout = QtWidgets.QVBoxLayout()
        # 分组
        group1 = QtWidgets.QGroupBox("进度条1")
        group2 = QtWidgets.QGroupBox("进度条2")
        group3 = QtWidgets.QGroupBox("进度条3")
        group4 = QtWidgets.QGroupBox("进度条4")
        # 组控件

        layout1 = QtWidgets.QVBoxLayout()
        process1 = QtWidgets.QProgressBar()
        button1 = QtWidgets.QPushButton('Start')
        layout1.addWidget(process1)
        layout1.addWidget(button1)
        group1.setLayout(layout1)
        layout.addWidget(group1)
        layout.addWidget(group2)
        layout.addWidget(group3)
        layout.addWidget(group4)
        # 样式
        button1.setMaximumWidth(100)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    surface = Surface()
    surface.show()
    sys.exit(app.exec_())

