# _*_ coding:utf-8 _*_
# __Author__： zizle


from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint, QPointF
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton

class CenterDrawer1(QLabel):
    def __init__(self, *args, **kwargs):
        super(CenterDrawer1, self).__init__(*args, **kwargs)
        self.animation = QPropertyAnimation(self, b'windowOpacity')
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.setDuration(2000)
        self.setText('阿斯顿发敬爱欧迪芬')
        self.resize(200, 300)
        self.setStyleSheet('background:rgb(200,200,200)')
        b = QPushButton(self, text='btn', clicked=self.animation.start)


class CenterDrawer(QWidget):
    def __init__(self, *args, stretch=1 / 3, widget=None, **kwargs):
        super(CenterDrawer, self).__init__(*args, **kwargs)
        self.setWindowFlags(self.windowFlags(
        ) | Qt.FramelessWindowHint | Qt.Popup | Qt.NoDropShadowWindowHint)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 进入动画
        self.animIn = QPropertyAnimation(
            self, duration=3000)
        self.animIn.setPropertyName(b'windowOpacity')
        # 离开动画
        self.animOut = QPropertyAnimation(
            self, duration=3000, finished=self.onAnimOutEnd,
            )
        self.animOut.setPropertyName(b'windowOpacity')
        self.animOut.setDuration(500)

        # 半透明背景
        self.alphaWidget = QWidget(
            self, objectName='CDrawer_alphaWidget',
            styleSheet='#CDrawer_alphaWidget{background:rgba(55,55,55,100);}')
        self.alphaWidget.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setWidget(widget)          # 子控件

    def resizeEvent(self, event):
        self.alphaWidget.resize(self.size())
        super(CenterDrawer, self).resizeEvent(event)

    def mousePressEvent(self, event):
        pos = event.pos()
        if pos.x() >= 0 and pos.y() >= 0 and self.childAt(pos) is None and self.widget:
            if not self.widget.geometry().contains(pos):
                self.animationOut()
                return
        super(CenterDrawer, self).mousePressEvent(event)

    def show(self):
        super(CenterDrawer, self).show()
        parent = self.parent().window() if self.parent() else self.window()
        if not parent or not self.widget:
            return
        # 设置Drawer大小和主窗口一致
        self.setGeometry(parent.geometry())
        geometry = self.geometry()
        self.animationIn(geometry)

    def animationIn(self, geometry):
        """进入动画
        :param geometry:
        """
        # self.widget.hide()
        self.animIn.setStartValue(0)
        self.animIn.setEndValue(1)
        self.animIn.start()
        # self.widget.show()

        #
        # if self.direction == self.LEFT:
        #     # 左侧抽屉
        #     self.widget.setGeometry(
        #         0, 0, int(geometry.width() * self.stretch), geometry.height())
        #     self.widget.hide()
        #     self.animIn.setStartValue(QPoint(-self.widget.width(), 0))
        #     self.animIn.setEndValue(QPoint(0, 0))
        #     self.animIn.start()
        #     self.widget.show()
        # elif self.direction == self.TOP:
        #     # 上方抽屉
        #     self.widget.setGeometry(
        #         0, 0, geometry.width(), int(geometry.height() * self.stretch))
        #     self.widget.hide()
        #     self.animIn.setStartValue(QPoint(0, -self.widget.height()))
        #     self.animIn.setEndValue(QPoint(0, 0))
        #     self.animIn.start()
        #     self.widget.show()
        # elif self.direction == self.RIGHT:
        #     # 右侧抽屉
        #     width = int(geometry.width() * self.stretch)
        #     self.widget.setGeometry(
        #         geometry.width() - width, 0, width, geometry.height())
        #     self.widget.hide()
        #     self.animIn.setStartValue(QPoint(self.width(), 0))
        #     self.animIn.setEndValue(
        #         QPoint(self.width() - self.widget.width(), 0))
        #     self.animIn.start()
        #     self.widget.show()
        # elif self.direction == self.BOTTOM:
        #     # 下方抽屉
        #     height = int(geometry.height() * self.stretch)
        #     self.widget.setGeometry(
        #         0, geometry.height() - height, geometry.width(), height)
        #     self.widget.hide()
        #     self.animIn.setStartValue(QPoint(0, self.height()))
        #     self.animIn.setEndValue(
        #         QPoint(0, self.height() - self.widget.height()))
        #     self.animIn.start()
        #     self.widget.show()

    def animationOut(self):
        """离开动画
        """
        self.animOut.setStartValue(1)
        self.animOut.setEndValue(0)
        self.animOut.start()
        # self.animIn.stop()  # 停止进入动画
        # geometry = self.widget.geometry()
        # if self.direction == self.LEFT:
        #     # 左侧抽屉
        #     self.animOut.setStartValue(geometry.topLeft())
        #     self.animOut.setEndValue(QPoint(-self.widget.width(), 0))
        #     self.animOut.start()
        # elif self.direction == self.TOP:
        #     # 上方抽屉
        #     self.animOut.setStartValue(QPoint(0, geometry.y()))
        #     self.animOut.setEndValue(QPoint(0, -self.widget.height()))
        #     self.animOut.start()
        # elif self.direction == self.RIGHT:
        #     # 右侧抽屉
        #     self.animOut.setStartValue(QPoint(geometry.x(), 0))
        #     self.animOut.setEndValue(QPoint(self.width(), 0))
        #     self.animOut.start()
        # elif self.direction == self.BOTTOM:
        #     # 下方抽屉
        #     self.animOut.setStartValue(QPoint(0, geometry.y()))
        #     self.animOut.setEndValue(QPoint(0, self.height()))
        #     self.animOut.start()

    def onAnimOutEnd(self):
        """离开动画结束
        """
        # 模拟点击外侧关闭
        QApplication.sendEvent(self, QMouseEvent(
            QMouseEvent.MouseButtonPress, QPointF(-1, -1), Qt.LeftButton, Qt.NoButton, Qt.NoModifier))

    def setWidget(self, widget):
        """设置子控件
        :param widget:
        """
        self.widget = widget
        if widget:
            widget.setParent(self)
            self.animIn.setTargetObject(widget)
            self.animOut.setTargetObject(widget)

    def setEasingCurve(self, easingCurve):
        """设置动画曲线
        :param easingCurve:
        """
        self.animIn.setEasingCurve(easingCurve)






if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    surface = CenterDrawer1()
    surface.show()
    sys.exit(app.exec_())



