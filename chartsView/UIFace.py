# _*_ coding:utf-8 _*_
# __Author__： zizle
from PyQt5 import QtWidgets
from bag import charts


class Surface(QtWidgets.QWidget):
    def __init__(self):
        super(Surface, self).__init__()
        layout = QtWidgets.QVBoxLayout()
        line = charts.LineChart()
        layout.addWidget(line)
        self.setLayout(layout)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    surface = Surface()
    surface.show()
    sys.exit(app.exec_())
