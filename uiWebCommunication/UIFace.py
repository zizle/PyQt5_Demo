# _*_ coding:utf-8 _*_
# Author: zizle

import os
import sys
from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore, QtWebChannel
from lib import channel


class Surface(QtWidgets.QWidget):
    def __init__(self):
        super(Surface, self).__init__()
        # 布局
        layout = QtWidgets.QHBoxLayout()
        ui_group_layout = QtWidgets.QVBoxLayout()
        web_group_layout = QtWidgets.QVBoxLayout()
        # 组
        self.ui_group_box = QtWidgets.QGroupBox()
        self.web_group_box = QtWidgets.QGroupBox()
        # 组控件
        self.ui_receive_message = QtWidgets.QLabel('等待网页消息...')
        self.ui_edit_message = QtWidgets.QLineEdit()
        ui_send_button = QtWidgets.QPushButton('发送')
        web_show = QtWebEngineWidgets.QWebEngineView()
        # 组控件加入组布局
        ui_group_layout.addWidget(self.ui_receive_message, alignment=QtCore.Qt.AlignTop)
        ui_group_layout.addWidget(self.ui_edit_message)
        ui_group_layout.addWidget(ui_send_button)
        web_group_layout.addWidget(web_show)
        # 组布局加入组
        self.ui_group_box.setLayout(ui_group_layout)
        self.web_group_box.setLayout(web_group_layout)
        # 组加入总布局
        layout.addWidget(self.ui_group_box)
        layout.addWidget(self.web_group_box)
        # 设置标题
        self.ui_group_box.setTitle('PyQt5界面')
        self.web_group_box.setTitle('Web页面')
        self.setWindowTitle('界面与网页通讯')
        # 控件风格
        self.ui_group_box.setMinimumWidth(400)
        # 加载网页
        current_path = os.getcwd()
        web_show.page().load(QtCore.QUrl('file:///' + current_path + '/data/web.html'))
        self.setLayout(layout)
        # 设置通讯通道传输对象
        self.channel_obj = channel.JSChannel()
        # 网界信息通道
        web_channel = QtWebChannel.QWebChannel(web_show.page())
        # 网页设置通道
        web_show.page().setWebChannel(web_channel)
        # 注册信号传输对象方便在网页中获取
        web_channel.registerObject('messageChannel', self.channel_obj)
        # 通道实例收到信号连接槽函数
        self.channel_obj.receiveMessageFromJS.connect(self.message_from_web)
        # 按钮点击发送消息
        ui_send_button.clicked.connect(self.message_to_web)

    def message_from_web(self, message):
        old_message = self.ui_receive_message.text()
        new_message = old_message + "<br/>收到网页消息：<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + message
        self.ui_receive_message.setText(new_message)

    def message_to_web(self):
        message = self.ui_edit_message.text()
        print(message)
        self.channel_obj.sendMessageToJS.emit(message)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    surface = Surface()
    surface.show()
    sys.exit(app.exec_())
