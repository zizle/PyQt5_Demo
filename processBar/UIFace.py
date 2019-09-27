# _*_ coding:utf-8 _*_
# Author: zizle
"""
对于样式的改变：
主要看主窗口Surface类的初始化内的setStyleSheet
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer


class CustomerProcessBar(QtWidgets.QProgressBar):
    def __init__(self):
        super(CustomerProcessBar, self).__init__()
        self.setValue(0)
        self.setMaximum(100)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_out)

    def timer_out(self):
        if self.value() >= 100:
            self.timer.stop()
            return
        self.setValue(self.value() + 1)

    def timer_start(self):
        if self.timer.isActive():
            return
        self.timer.start(200)

    def timer_stop(self):
        if self.timer.isActive():
            self.timer.stop()


class Surface(QtWidgets.QWidget):
    def __init__(self):
        super(Surface, self).__init__()
        layout = QtWidgets.QVBoxLayout()
        # 分组
        group1 = QtWidgets.QGroupBox("常规进度条")
        group2 = QtWidgets.QGroupBox("百分比居中")
        group3 = QtWidgets.QGroupBox("设置颜色")
        group4 = QtWidgets.QGroupBox("边框样式")
        group5 = QtWidgets.QGroupBox("格子进度条")
        group6 = QtWidgets.QGroupBox("填充方式")
        group7 = QtWidgets.QGroupBox("繁忙状态")
        # 组1控件布局
        layout1 = QtWidgets.QVBoxLayout()
        process1 = CustomerProcessBar()
        button1 = QtWidgets.QPushButton('Start')
        button1.clicked.connect(lambda: self.start_stop(button1, process1))
        layout1.addWidget(process1)
        layout1.addWidget(button1)
        group1.setLayout(layout1)
        # 组2控件布局
        layout2 = QtWidgets.QVBoxLayout()
        process2 = CustomerProcessBar()
        process2.setObjectName('process2')
        button2 = QtWidgets.QPushButton('Start')
        button2.clicked.connect(lambda: self.start_stop(button2, process2))
        layout2.addWidget(process2)
        layout2.addWidget(button2)
        group2.setLayout(layout2)
        # 组3控件布局
        layout3 = QtWidgets.QVBoxLayout()
        process3 = CustomerProcessBar()
        process3.setObjectName('process3')
        button3 = QtWidgets.QPushButton('Start')
        button3.clicked.connect(lambda: self.start_stop(button3, process3))
        layout3.addWidget(process3)
        layout3.addWidget(button3)
        group3.setLayout(layout3)
        # 组4控件布局
        layout4 = QtWidgets.QVBoxLayout()
        process4 = CustomerProcessBar()
        process4.setObjectName('process4')
        button4 = QtWidgets.QPushButton('Start')
        button4.clicked.connect(lambda: self.start_stop(button4, process4))
        layout4.addWidget(process4)
        layout4.addWidget(button4)
        group4.setLayout(layout4)
        # 组5控件布局
        layout5 = QtWidgets.QVBoxLayout()
        process5 = CustomerProcessBar()
        process5.setObjectName('process5')
        button5 = QtWidgets.QPushButton('Start')
        button5.clicked.connect(lambda: self.start_stop(button5, process5))
        layout5.addWidget(process5)
        layout5.addWidget(button5)
        group5.setLayout(layout5)
        # 组6控件布局
        layout6 = QtWidgets.QVBoxLayout()
        process6 = CustomerProcessBar()
        process6.setObjectName('process6')
        process6.setTextVisible(False)  # 进度文本不可见
        button6 = QtWidgets.QPushButton('Start')
        button6.clicked.connect(lambda: self.start_stop(button6, process6))
        layout6.addWidget(process6)
        layout6.addWidget(button6)
        group6.setLayout(layout6)
        # 组7控件布局
        layout7 = QtWidgets.QVBoxLayout()
        process7 = CustomerProcessBar()
        process7.setObjectName('process7')
        process7.setTextVisible(False)  # 进度文本不可见
        process7.setMinimum(0)
        process7.setMaximum(0)
        layout7.addWidget(process7)
        group7.setLayout(layout7)
        # 布局添加组
        layout.addWidget(group1)
        layout.addWidget(group2)
        layout.addWidget(group3)
        layout.addWidget(group4)
        layout.addWidget(group5)
        layout.addWidget(group6)
        layout.addWidget(group7)
        # 样式
        button1.setMaximumWidth(100)
        button2.setMaximumWidth(100)
        button3.setMaximumWidth(100)
        button4.setMaximumWidth(100)
        button5.setMaximumWidth(100)
        button6.setMaximumWidth(100)

        self.setFixedWidth(600)
        self.setWindowTitle('PyQt5之进度条样式设置')
        self.setStyleSheet("""
        #process2, #process3 {
            text-align: center;
        }
        #process3::chunk {
            background-color: #FF3E96
        }
        #process4 {
            border: 1px solid #71C671;
            border-radius: 5px;
            max-height: 10px;
            min-height: 10px;
            text-align: right;
        }
        #process5 {
            border: 1px solid #00CD66;  /*边框以及边框颜色,不指定即为无边框*/
            text-align: right;
            max-height: 15px;
            min-height: 15px;
        }
        #process5::chunk {
            background-color: #00CD66;
            width: 5px; /*区块宽度*/
            margin:1px; /*区块外边距*/
        }
        #process6 {
            border:none;
            background-color: #CCCCCC;
            max-height: 12px;
            min-height: 12px;
            border-radius: 6px;
        }
        #process6::chunk {
            background-color: #575757;
            border-radius: 6px;
        }
        """)
        self.setLayout(layout)

    def start_stop(self, button, process_bar):
        if button.text() == "Start":
            process_bar.timer_start()
            button.setText('Stop')
        else:
            process_bar.timer_stop()
            button.setText("Start")
        # 如果进度满则重新开始
        if process_bar.value() >= 100:
            process_bar.setValue(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    surface = Surface()
    surface.show()
    sys.exit(app.exec_())
