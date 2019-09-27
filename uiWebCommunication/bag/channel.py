# _*_ coding:utf-8 _*_
# Author: zizle

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class JSChannel(QObject):
    receiveMessageFromJS = pyqtSignal(str)
    sendMessageToJS = pyqtSignal(str)

    @pyqtSlot(str)  # 装饰器用于把函数暴露给JS调用
    def JSSendMessage(self, message):
        """JS发送信号的信号槽函数"""
        # 将信号信息发出到界面处理
        self.receiveMessageFromJS.emit(message)







