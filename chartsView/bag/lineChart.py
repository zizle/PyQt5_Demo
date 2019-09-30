# _*_ coding:utf-8 _*_
# Author: zizle

from PyQt5 import QtChart, QtWidgets
from PyQt5.QtGui import QPainter


class LineChart(QtChart.QChartView):
    def __init__(self):
        super(LineChart, self).__init__()
        chart = QtChart.QChart()
        # 线1
        series1 = QtChart.QLineSeries()
        series2 = QtChart.QLineSeries()
        series1.append(0, 5)
        series1.append(1, 3)
        series1.append(2, 2)
        series1.append(4, 4)
        # 线2
        series2.append(0, 2)
        series2.append(1, 3)
        series2.append(2, 5)
        series2.append(4, 3)
        # 加入线
        chart.addSeries(series1)
        chart.addSeries(series2)
        # 设置
        chart.setTitle('QChart做折线图')
        chart.createDefaultAxes()  # 设置默认坐标
        series1.setName('梨')  # 设置图例
        series2.setName('苹果')  # 设置图例
        self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        # 显示图表
        self.setChart(chart)