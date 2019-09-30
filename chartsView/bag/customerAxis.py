# _*_ coding:utf-8 _*_
# Author: zizle
""" 自定性X/Y轴 """
import random
from PyQt5 import QtWidgets, QtChart
from PyQt5.QtCore import Qt

def random_data_table():
    """ 随机生成画图数据 """
    # 线条数据个数
    series_count = 3
    # 最大值
    max_value = 10
    # 数据个数
    value_count = 7
    random.seed()
    data_table = []
    for i in range(series_count):
        data_list = []
        y_value = 0.0
        for j in range(value_count):
            y_value += random.uniform(0, max_value) / float(value_count)
            value = j + random.random() * max_value / float(value_count), y_value
            label = "Slice " + str(i) + ":" + str(j)  # 第几条线第几个数据
            data_list.append((value, label))
        data_table.append(data_list)
    return data_table


class XAxis(QtChart.QChartView):
    """ 自定义x轴"""
    def __init__(self):
        super(XAxis, self).__init__()
        # 创建图表
        chart = QtChart.QChart()
        chart.setTitle('自定义X轴')
        data_table = random_data_table()  # 获取随机生成的数据作图
        for i, data_list in enumerate(data_table):
            series = QtChart.QLineSeries()
            for value, name in data_list:
                series.append(*value)
            series.setName("Series " + str(i))
            chart.addSeries(series)
        chart.createDefaultAxes()
        # 自定义x轴
        series = chart.series()

        axis = QtChart.QCategoryAxis(
            chart, labelsPosition=QtChart.QCategoryAxis.AxisLabelsPositionOnValue
        )
        min_x = chart.axisX().min()
        max_x = chart.axisX().max()
        tick_count = chart.axisX().tickCount()
        if tick_count < 2:
            axis.append("LABEL0", min_x)
        else:
            step_x = (max_x - min_x) / (tick_count - 1)
            for i in range(tick_count):
                axis.append("LABEL%s" % i, min_x + i * step_x)
        chart.setAxisX(axis, series[0])
        # 图表加入容器
        self.setChart(chart)


class TopXAxis(QtChart.QChartView):
    def __init__(self):
        super(TopXAxis, self).__init__()
        # 创建图表
        chart = QtChart.QChart()
        chart.setTitle('自定义Top-X轴')
        data_table = random_data_table()  # 获取随机生成的数据作图
        for i, data_list in enumerate(data_table):
            series = QtChart.QLineSeries()
            for value, name in data_list:
                series.append(*value)
            series.setName("Series " + str(i))
            chart.addSeries(series)
        chart.createDefaultAxes()
        # 自定义top-x轴
        series = chart.series()
        x_category = ['%d月' % i for i in range(1, 9)]
        axis_x = QtChart.QCategoryAxis(
            chart, labelsPosition=QtChart.QCategoryAxis.AxisLabelsPositionOnValue
        )
        axis_x.setGridLineVisible(False)  # 隐藏网格线条
        axis_x.setTickCount(len(x_category))  # 设置刻度个数
        # 强制修改原x轴的刻度个数与自定义上x轴刻度个数一直
        chart.axisX().setTickCount(len(x_category))

        min_x = chart.axisX().min()
        max_x = chart.axisX().max()
        tick_count = chart.axisX().tickCount()
        print(tick_count)
        if tick_count < 2:
            axis_x.append("LABEL0", min_x)
        else:
            step_x = (max_x - min_x) / (tick_count - 1)
            for i in range(tick_count):
                axis_x.append(x_category[i], min_x + step_x * i)
            chart.addAxis(axis_x, Qt.AlignTop)
        series[0].attachAxis(axis_x)
        # 图表在容器中显示
        self.setChart(chart)


class YAxis(QtChart.QChartView):
    def __init__(self):
        super(YAxis, self).__init__()
        # 创建图表
        chart = QtChart.QChart()
        chart.setTitle('自定义添加右侧Y轴')
        data_table = random_data_table()  # 获取随机生成的数据作图
        for i, data_list in enumerate(data_table):
            series = QtChart.QLineSeries()
            for value, name in data_list:
                series.append(*value)
            series.setName("Series " + str(i))
            chart.addSeries(series)
        chart.createDefaultAxes()
        # 自定义y轴
        series = chart.series()
        y_category = ['周%d' % i for i in range(1, 8)]
        axisy = QtChart.QCategoryAxis(
            chart, labelsPosition=QtChart.QCategoryAxis.AxisLabelsPositionOnValue
        )
        axisy.setGridLineVisible(False)
        axisy.setTickCount(len(y_category))
        min_y = chart.axisY().min()
        max_y = chart.axisY().max()
        tick_count = axisy.tickCount()
        if tick_count < 2:
            axisy.append(y_category[0])
        else:
            step_y = (max_y - min_y) / (tick_count -1)
            for i in range(tick_count):
                axisy.append(y_category[i], min_y + step_y * i)
        chart.addAxis(axisy, Qt.AlignRight)  # 在右侧添加轴
        series[0].attachAxis(axisy)
        self.setChart(chart)





if __name__ == '__main__':
    random_data_table()



class CustomerAxis(QtWidgets.QWidget):
    """ 自定义轴 """
    def __init__(self):
        super(CustomerAxis, self).__init__()
        layout = QtWidgets.QGridLayout()
        # 自定义x轴
        x_chart = XAxis()
        layout.addWidget(x_chart, 0, 0)
        self.setLayout(layout)
