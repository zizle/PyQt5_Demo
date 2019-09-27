# _*_ coding:utf-8 _*_
# Author: zizle
"""
对于样式的改变：
常规样式主要看主窗口Surface类的初始化内的setStyleSheet
"""
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from processBar.bag import special


class Surface(QtWidgets.QWidget):
    def __init__(self):
        super(Surface, self).__init__()
        # 定时器模拟进度
        self.timer = QTimer()
        layout = QtWidgets.QHBoxLayout()
        normal_layout = QtWidgets.QVBoxLayout()
        special_layout = QtWidgets.QVBoxLayout()
        normal_group = QtWidgets.QGroupBox('常规样式')
        special_group = QtWidgets.QGroupBox('特殊样式')
        """常规样式"""
        # 分组
        group1 = QtWidgets.QGroupBox("常规进度条")
        group2 = QtWidgets.QGroupBox("百分比居中")
        group3 = QtWidgets.QGroupBox("设置颜色")
        group4 = QtWidgets.QGroupBox("边框样式")
        group5 = QtWidgets.QGroupBox("格子进度条")
        group6 = QtWidgets.QGroupBox("填充方式")
        group7 = QtWidgets.QGroupBox("繁忙状态")
        group8 = QtWidgets.QGroupBox("圆圈繁忙进度")
        group9 = QtWidgets.QGroupBox("圆圈百分比")
        group10 = QtWidgets.QGroupBox("Metro加载中")
        group11 = QtWidgets.QGroupBox("水波浪")
        # 组1控件布局
        layout1 = QtWidgets.QVBoxLayout()
        process1 = QtWidgets.QProgressBar()
        process1.timer = None  # 定时器模拟进度
        button1 = QtWidgets.QPushButton('Start')
        button1.clicked.connect(lambda: self.start_stop(button1, process1))
        layout1.addWidget(process1)
        layout1.addWidget(button1)
        group1.setLayout(layout1)
        # 组2控件布局
        layout2 = QtWidgets.QVBoxLayout()
        process2 = QtWidgets.QProgressBar()
        process2.setObjectName('process2')
        process2.timer = None
        button2 = QtWidgets.QPushButton('Start')
        button2.clicked.connect(lambda: self.start_stop(button2, process2))
        layout2.addWidget(process2)
        layout2.addWidget(button2)
        group2.setLayout(layout2)
        # 组3控件布局
        layout3 = QtWidgets.QVBoxLayout()
        process3 = QtWidgets.QProgressBar()
        process3.setObjectName('process3')
        process3.timer = None
        button3 = QtWidgets.QPushButton('Start')
        button3.clicked.connect(lambda: self.start_stop(button3, process3))
        layout3.addWidget(process3)
        layout3.addWidget(button3)
        group3.setLayout(layout3)
        # 组4控件布局
        layout4 = QtWidgets.QVBoxLayout()
        process4 = QtWidgets.QProgressBar()
        process4.timer = None
        process4.setObjectName('process4')
        button4 = QtWidgets.QPushButton('Start')
        button4.clicked.connect(lambda: self.start_stop(button4, process4))
        layout4.addWidget(process4)
        layout4.addWidget(button4)
        group4.setLayout(layout4)
        # 组5控件布局
        layout5 = QtWidgets.QVBoxLayout()
        process5 = QtWidgets.QProgressBar()
        process5.setObjectName('process5')
        process5.timer = None
        button5 = QtWidgets.QPushButton('Start')
        button5.clicked.connect(lambda: self.start_stop(button5, process5))
        layout5.addWidget(process5)
        layout5.addWidget(button5)
        group5.setLayout(layout5)
        # 组6控件布局
        layout6 = QtWidgets.QVBoxLayout()
        process6 = QtWidgets.QProgressBar()
        process6.setObjectName('process6')
        process6.timer = None
        process6.setTextVisible(False)  # 进度文本不可见
        button6 = QtWidgets.QPushButton('Start')
        button6.clicked.connect(lambda: self.start_stop(button6, process6))
        layout6.addWidget(process6)
        layout6.addWidget(button6)
        group6.setLayout(layout6)
        # 组7控件布局
        layout7 = QtWidgets.QVBoxLayout()
        process7 = QtWidgets.QProgressBar()
        process7.setObjectName('process7')
        process7.timer = None
        process7.setTextVisible(False)  # 进度文本不可见
        process7.setMinimum(0)
        process7.setMaximum(0)
        layout7.addWidget(process7)
        group7.setLayout(layout7)
        """特殊样式"""
        # 组8控件布局,颜色设置查看styleSheet{#process8}
        layout8 = QtWidgets.QHBoxLayout()
        process8_1 = special.CircleProgressBar()
        process8_1.setObjectName('process8')
        process8_2 = special.CircleProgressBar(clockwise=False)
        layout8.addWidget(process8_1)
        layout8.addWidget(process8_2)
        group8.setLayout(layout8)
        # 组9控件布局
        layout9 = QtWidgets.QHBoxLayout()
        # 顺时针
        layout9_1 = QtWidgets.QVBoxLayout()
        process9_1 = special.PercentProgressBar()
        process9_1.setObjectName('process91')
        process9_1.timer = None
        button9_1 = QtWidgets.QPushButton('Start')
        button9_1.clicked.connect(lambda: self.start_stop(button9_1, process9_1))
        layout9_1.addWidget(process9_1)
        layout9_1.addWidget(button9_1)
        # 逆时针初始化传入参数clockwise=False
        # (不显示百分号初始参数：showPercent=False)
        layout9_2 = QtWidgets.QVBoxLayout()
        process9_2 = special.PercentProgressBar(clockwise=False)
        process9_2.setObjectName('process92')
        process9_2.timer = None
        button9_2 = QtWidgets.QPushButton('Start')
        button9_2.clicked.connect(lambda: self.start_stop(button9_2, process9_2))
        layout9_2.addWidget(process9_2)
        layout9_2.addWidget(button9_2)
        # 外围阴影小圈 showFreeArea=True
        # (外围没有小圈，进度条小圆头：showSmallCircle=True)
        layout9_3 = QtWidgets.QVBoxLayout()
        process9_3 = special.PercentProgressBar(showFreeArea=True, showSmallCircle=True)
        process9_3.setObjectName('process93')
        process9_3.timer = None
        button9_3 = QtWidgets.QPushButton('Start')
        button9_3.clicked.connect(lambda: self.start_stop(button9_3, process9_3))
        layout9_3.addWidget(process9_3)
        layout9_3.addWidget(button9_3)
        # 设置颜色，查看styleSheet{#process94}
        layout9_4 = QtWidgets.QVBoxLayout()
        process9_4 = special.PercentProgressBar(showFreeArea=True)
        process9_4.setObjectName('process94')
        process9_4.timer = None
        button9_4 = QtWidgets.QPushButton('Start')
        button9_4.clicked.connect(lambda: self.start_stop(button9_4, process9_4))
        layout9_4.addWidget(process9_4)
        layout9_4.addWidget(button9_4)

        layout9.addLayout(layout9_1)
        layout9.addLayout(layout9_2)
        layout9.addLayout(layout9_3)
        layout9.addLayout(layout9_4)
        group9.setLayout(layout9)

        # 常规布局添加组
        normal_layout.addWidget(group1)
        normal_layout.addWidget(group2)
        normal_layout.addWidget(group3)
        normal_layout.addWidget(group4)
        normal_layout.addWidget(group5)
        normal_layout.addWidget(group6)
        normal_layout.addWidget(group7)
        # 特殊布局添加组
        special_layout.addWidget(group8)
        special_layout.addWidget(group9)
        special_layout.addWidget(group10)
        special_layout.addWidget(group11)
        # 样式
        button1.setMaximumWidth(100)
        button2.setMaximumWidth(100)
        button3.setMaximumWidth(100)
        button4.setMaximumWidth(100)
        button5.setMaximumWidth(100)
        button6.setMaximumWidth(100)
        button9_1.setMaximumWidth(100)
        button9_2.setMaximumWidth(100)
        button9_3.setMaximumWidth(100)
        button9_4.setMaximumWidth(100)
        normal_group.setFixedWidth(500)
        special_group.setFixedWidth(500)
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
        #process8 {
            qproperty-color: #575757; /*颜色*/
        }
        #process94 {
            qproperty-textColor: rgb(255, 0, 0);
            qproperty-borderColor: rgb(0, 255, 0);
            qproperty-backgroundColor: rgb(0, 0, 255);
        }
        """)
        normal_group.setLayout(normal_layout)
        special_group.setLayout(special_layout)
        layout.addWidget(normal_group)
        layout.addWidget(special_group)
        self.setLayout(layout)

    def start_stop(self, button, process_bar):
        if process_bar.timer is None:
            process_bar.timer = QTimer()
            process_bar.timer.timeout.connect(lambda: self.time_out(process_bar))
        if button.text() == "Start":
            if process_bar.timer.isActive():
                return
            process_bar.timer.start(200)
            button.setText('Stop')
        else:
            process_bar.timer.stop()
            button.setText("Start")
        # 如果进度满则重新开始
        try:
            current = process_bar.value()
        except Exception:
            current = process_bar.value
        if current >= 100:
            process_bar.setValue(0)

    def time_out(self, process_bar):
        try:
            current = process_bar.value()
        except Exception:
            current = process_bar.value
        if current >= 100:
            process_bar.timer.stop()
            return
        process_bar.setValue(current + 1)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    surface = Surface()
    surface.show()
    sys.exit(app.exec_())
