# _*_ coding:utf-8 _*_
# __Author__： zizle

import random
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtChart import QChartView, QChart, QBarSeries, QBarSet, QLineSeries


class UseBar(QtWidgets.QWidget):
    """
    折线图&柱状图使用方式
    图上的数据获取
    """
    def __init__(self, *args, **kwargs):
        super(UseBar, self).__init__(*args, **kwargs)
        layout = QtWidgets.QVBoxLayout()
        # 添加控件
        self.chart_view = QChartView()
        enlarge_btn = QtWidgets.QPushButton('放大', clicked=self.enlarge_chart)
        enlarge_btn.setStyleSheet("border:none;background-color:rgb(150,100,100); color:rgb(255,255,255);padding:5px;border-radius:5px")
        enlarge_btn.setCursor(Qt.PointingHandCursor)
        self.chart_view.setFixedSize(500, 200)
        layout.addWidget(self.chart_view, alignment=Qt.AlignTop)
        layout.addWidget(enlarge_btn, alignment=Qt.AlignTop)
        layout.addWidget(QtWidgets.QWidget())
        self.resize(1000, 600)
        self.setLayout(layout)
        self.draw_bar()  # 画图

    def draw_bar(self):
        """初始化的图形"""
        chart_set = QChart(title='例子', flags=Qt.Widget)
        chart_set.legend().hide()
        bar_series = QBarSeries()
        line_series = QLineSeries()
        bar_set = QBarSet('')
        x1_axis = [i for i in range(0, 21)]
        for idx, _ in enumerate(range(len(x1_axis))):
            y = float(random.randint(1, 1500))
            bar_set.append(y)
            line_series.append(x1_axis[idx], y)
        bar_series.append(bar_set)
        chart_set.addSeries(bar_series)
        chart_set.addSeries(line_series)
        chart_set.createDefaultAxes()
        self.chart_view.setChart(chart_set)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

    def enlarge_chart(self):
        """
        获取chart中的数据:
        1、获取图形列表：QChartView.chart().series() -> list of QSeries
        2、折线图点的数量：QLineSeries.count() -> int
        3、柱形图的柱子集合列表：QBarSeries.barSets() -> list of QBarSet
        4、柱形图每个集合中点的数量：QBarSet.count() -> int
        5、获取折线图的点：QLineSeries.at(index) -> QPointF
        6、折线图中QPointF转为坐标点：QPointF.x() -> float ; QPointF.y() -> float
        7、获取柱形图中的点：QBarSet.at(index) -> float
        """
        data = dict()
        data['title'] = '例子'
        line_list = list()
        bar_list = list()
        for series in self.chart_view.chart().series():  # 所有图形（每个折线都是一个series）
            series_data = dict()
            if isinstance(series, QBarSeries):
                for bar_set in series.barSets():  # 遍历柱子集合
                    x1_axis = list()
                    y1_axis = list()
                    for i in range(bar_set.count()):  # 获取每个集合中的点
                        x1_axis.append(i)
                        y1_axis.append(bar_set.at(i))
                        # print('柱子图数据', i, ":", bar_set.at(i))
                    series_data['x1_axis'] = x1_axis
                    series_data['y1_axis'] = y1_axis
                    bar_list.append(series_data)

            elif isinstance(series, QLineSeries):
                x1_axis = list()
                y1_axis = list()
                for i in range(series.count()):
                    # print('折线图点', i, (series.at(i).x(), series.at(i).y()))
                    x1_axis.append(series.at(i).x())
                    y1_axis.append(series.at(i).y())
                series_data['x1_axis'] = x1_axis
                series_data['y1_axis'] = y1_axis
                line_list.append(series_data)
            else:
                print('未知图形')
        data['line'] = line_list
        data['bar'] = bar_list
        self.large_view(data)

    def large_view(self, data):
        """放大后的视图"""
        # data: {
        #   'line': [{'x1_axis':[], 'y1_axis':[]},{},{},],
        #   'bar' : [{'x1_axis':[], 'y1_axis':[]},{},{},],
        # }
        new_chart_view = QChartView()
        chart_set = QChart(title=data['title'])
        new_chart_view.setChart(chart_set)
        new_chart_view.setRenderHint(QPainter.Antialiasing)
        chart_set.legend().hide()
        for chart_type in data:
            if chart_type == 'line':
                for chart_data in data[chart_type]:
                    line_series = QLineSeries()
                    for x_idx, x in enumerate(chart_data['x1_axis']):
                        line_series.append(float(x), float(chart_data['y1_axis'][x_idx]))
                    chart_set.addSeries(line_series)
            elif chart_type == 'bar':
                for chart_data in data[chart_type]:
                    bar_series = QBarSeries()
                    bar_set = QBarSet('')
                    for x_idx, x in enumerate(chart_data['x1_axis']):
                        bar_set.append(float(chart_data['y1_axis'][x_idx]))
                    bar_series.append(bar_set)
                    chart_set.addSeries(bar_series)
            else:
                pass
        chart_set.createDefaultAxes()
        # 新的显示窗
        new_widget = QtWidgets.QWidget(self)
        new_widget.resize(self.width(), self.height())
        layout = QtWidgets.QVBoxLayout(new_widget)
        layout.addWidget(new_chart_view)
        layout.addWidget(QtWidgets.QTableWidget())
        new_widget.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    barShow = UseBar()
    barShow.show()
    sys.exit(app.exec_())
