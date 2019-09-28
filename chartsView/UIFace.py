# _*_ coding:utf-8 _*_
# __Author__： zizle
from PyQt5 import QtWidgets
from chartsView.bag import charts


class Surface(QtWidgets.QWidget):
    def __init__(self):
        super(Surface, self).__init__()
        layout = QtWidgets.QVBoxLayout()
        # 折线图
        line = charts.LineChart()
        # 折线堆叠
        line_stack = charts.LineStackChart()

        layout.addWidget(line)
        layout.addWidget(line_stack)
        self.setLayout(layout)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    surface = Surface()
    surface.show()
    sys.exit(app.exec_())
