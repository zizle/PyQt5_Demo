# _*_ coding:utf-8 _*_
# Author: zizle

import random
from PyQt5 import QtChart
from PyQt5.QtCore import Qt


class BarStackChart(QtChart.QChartView):
    def __init__(self):
        super(BarStackChart, self).__init__()
        self.chart = QtChart.QChart()
        self.chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)  # 动态渲染
        self.x_category = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        series_names = ['视频广告', '直接访问', '搜索引擎']
        series = QtChart.QBarSeries()
        for name in series_names:
            bar = QtChart.QBarSet(name)
            for _ in range(len(self.x_category)):
                bar.append(random.randint(1, 101))
            series.append(bar)
            # 鼠标悬停信号
            bar.hovered.connect(self.bar_hovered)
        self.chart.addSeries(series)
        self.chart.createDefaultAxes()
        # 设置x轴
        axis_x = QtChart.QBarCategoryAxis()
        axis_x.append(self.x_category)
        self.chart.setAxisX(axis_x, series)
        # 设置图例
        legend = self.chart.legend()
        legend.setCursor(Qt.PointingHandCursor)  # 鼠标悬停图例为手形
        for marker in legend.markers():
            # 点击事件
            marker.clicked.connect(self.legend_clicked)
            # 悬停事件
            marker.hovered.connect(self.legend_hovered)
        self.setChart(self.chart)

    def bar_hovered(self, status, index):
        # status 是否在柱子上
        # index 第几组柱形图
        bar = self.sender()
        pen = bar.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        bar.setPen(pen)

    def legend_clicked(self):
        marker = self.sender()
        if not marker:
            return
        bar = marker.barset()
        if not bar:
            return
        # bar的透明度
        brush = bar.brush()
        color = brush.color()
        alpha = 0.0 if color.alphaF() == 1.0 else 1.0
        color.setAlphaF(alpha)
        brush.setColor(color)
        bar.setBrush(brush)
        # markerLabel的透明度
        brush = marker.labelBrush()
        color = brush.color()
        alpha = 0.4 if color.alphaF() == 1.0 else 1.0
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setLabelBrush(brush)
        # 设置marker透明度(重新获取brush不然已被上面覆盖)
        brush = marker.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setBrush(brush)

    def legend_hovered(self, status):
        marker = self.sender()
        if not marker:
            return
        bar = marker.barset()
        if not bar:
            return
        pen = bar.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        bar.setPen(pen)

