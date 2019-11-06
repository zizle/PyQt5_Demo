# _*_ coding:utf-8 _*_
# __Author__： zizle
"""
弹窗遮罩效果
"""
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QVBoxLayout, QLineEdit, QTabWidget,\
    QHBoxLayout, QGraphicsOpacityEffect, QLabel
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from coverDialog.bag import sideWidget, centerWidget


class DrawerWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(DrawerWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet('DrawerWidget{background:white;}')
        layout = QVBoxLayout(self)
        layout.addWidget(QLineEdit(self))
        layout.addWidget(QPushButton('button', self))


class Surface(QTabWidget):
    def __init__(self):
        super(Surface, self).__init__()
        self.resize(800, 600)
        # 增加两个tab的widget
        side_cover_widget = QWidget()
        center_cover_widget = QWidget()
        # 四周弹窗的布局
        side_layout = QGridLayout()
        left = QPushButton('左', clicked=self.left_open)
        top = QPushButton('上', clicked=self.top_open)
        right = QPushButton('右', clicked=self.right_open)
        bottom = QPushButton('下', clicked=self.bottom_open)
        side_layout.addWidget(left, 1, 0)
        side_layout.addWidget(top, 0, 1)
        side_layout.addWidget(right, 1, 2)
        side_layout.addWidget(bottom, 2, 1)
        side_cover_widget.setLayout(side_layout)
        # 中心弹窗的布局
        center_layout = QHBoxLayout()
        center = QPushButton('中心', clicked=self.center_open)
        center_layout.addWidget(center, alignment=Qt.AlignCenter)
        center_cover_widget.setLayout(center_layout)
        # 加入主窗口
        self.addTab(side_cover_widget, '四周弹出')
        self.addTab(center_cover_widget, '中心弹出')
        # 中心弹窗遮罩体
        opacity = QGraphicsOpacityEffect()
        opacity.setOpacity(0.4)
        self.cover = QWidget(self)
        self.cover.setGraphicsEffect(opacity)
        self.cover.setStyleSheet("background-color: rgb(150,150,150);")
        self.cover.setAutoFillBackground(True)
        self.cover.resize(self.width(), self.height())
        self.cover.hide()

    def center_open(self):
        self.cover.show()
        self.center_widget = centerWidget.CenterDrawer()
        # 关闭按钮
        layout = QHBoxLayout(self.center_widget, margin=0)
        layout.addWidget(
            QPushButton(self.center_widget, text='关闭', clicked=self.center_close),
            alignment=Qt.AlignTop | Qt.AlignRight
        )
        # 计算置于窗体中心
        self.center_widget.move(int((self.width() - self.center_widget.width()) / 2 + self.x()),
                                int((self.height() - self.center_widget.height()) / 2 + self.y()))
        self.center_widget.animation.start()
        self.center_widget.show()

    def center_close(self):
        self.cover.hide()
        # 设置关闭动画
        # 设置new widget变小的动画
        self.anim = QPropertyAnimation(self.center_widget, b"geometry")
        self.anim.setDuration(400)
        self.anim.setStartValue(QRect(
                self.center_widget.x(),
                self.center_widget.y(),
                self.center_widget.width(),
                self.center_widget.height()
            )
        )
        self.anim.setEndValue(QRect(self.x() + self.width(), self.y(), 0, 0))
        self.anim.start()
        self.center_widget.show()
        self.anim.finished.connect(self.center_widget.deleteLater)
        self.cover.close()

    def left_open(self):
        if not hasattr(self, 'left_widget'):
            self.left_widget = sideWidget.SideDrawer(self, direction=sideWidget.SideDrawer.LEFT)
            self.left_widget.setWidget(DrawerWidget())
        self.left_widget.show()

    def top_open(self):
        if not hasattr(self, 'top_widget'):
            self.top_widget = sideWidget.SideDrawer(self, direction=sideWidget.SideDrawer.TOP)
            self.top_widget.setWidget(DrawerWidget())
        self.top_widget.show()

    def right_open(self):
        if not hasattr(self, 'right_widget'):
            self.right_widget = sideWidget.SideDrawer(self, direction=sideWidget.SideDrawer.RIGHT)
            self.right_widget.setWidget(DrawerWidget())
        self.right_widget.show()

    def bottom_open(self):
        print('下边弹出')
        if not hasattr(self, 'bottom_widget'):
            self.bottom_widget = sideWidget.SideDrawer(self, direction=sideWidget.SideDrawer.BOTTOM)
            self.bottom_widget.setWidget(DrawerWidget())
        self.bottom_widget.show()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    surface = Surface()
    surface.show()
    sys.exit(app.exec_())
