# _*_ coding:utf-8 _*_
# __Author__： zizle
from PyQt5 import QtWidgets
from chartsView.bag import lineChart, lineStackChart, customerAxis, barStackChart


class Surface(QtWidgets.QWidget):
    def __init__(self):
        super(Surface, self).__init__()
        layout = QtWidgets.QGridLayout()
        # 折线图
        line = lineChart.LineChart()
        # 折线堆叠鼠标交互
        line_stack = lineStackChart.LineStackChart()
        # 自定义轴
        customer_xaxis = customerAxis.CustomerAxis()
        # 自定义上x轴
        customer_top_xaxis = customerAxis.TopXAxis()
        # 自定义添加右侧Y轴
        customer_right_yaxis = customerAxis.YAxis()
        # 柱状图堆叠鼠标交互
        bar_stack = barStackChart.BarStackChart()
        layout.addWidget(line, 0, 0)
        layout.addWidget(line_stack, 1, 2)
        layout.addWidget(customer_xaxis, 0, 1)
        layout.addWidget(customer_top_xaxis, 1, 1)
        layout.addWidget(customer_right_yaxis, 0, 2)
        layout.addWidget(bar_stack, 1, 0)
        self.resize(1360, 768)
        self.setLayout(layout)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    surface = Surface()
    surface.show()
    sys.exit(app.exec_())
