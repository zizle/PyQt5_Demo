# _*_ coding:utf-8 _*_
# __Author__： zizle
from PyQt5 import QtChart, QtWidgets
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QPointF, QPoint, QRectF, Qt


class ToolTipItem(QtWidgets.QWidget):
    def __init__(self, color, text, parent=None):
        super(ToolTipItem, self).__init__(parent)
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        label = QtWidgets.QLabel(self)
        label.setMinimumSize(12, 12)
        label.setMaximumSize(12, 12)
        label.setStyleSheet("border-radius:6px;background: rgba(%s,%s,%s,%s);" % (
            color.red(), color.green(), color.blue(), color.alpha()))
        layout.addWidget(label)
        self.textLabel = QtWidgets.QLabel(text, self, styleSheet="color:white;")
        layout.addWidget(self.textLabel)

    def setText(self, text):
        self.textLabel.setText(text)


class ToolTipWidget(QtWidgets.QWidget):
    Cache = {}

    def __init__(self, *args, **kwargs):
        super(ToolTipWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            "ToolTipWidget{background: rgba(50, 50, 50, 100);}")
        layout = QtWidgets.QVBoxLayout(self)
        self.titleLabel = QtWidgets.QLabel(self, styleSheet="color:white;")
        layout.addWidget(self.titleLabel)

    def updateUi(self, title, points):
        self.titleLabel.setText(title)
        for serie, point in points:
            if serie not in self.Cache:
                item = ToolTipItem(
                    serie.color(),
                    (serie.name() or "-") + ":" + str(point.y()), self)
                self.layout().addWidget(item)
                self.Cache[serie] = item
            else:
                self.Cache[serie].setText(
                    (serie.name() or "-") + ":" + str(point.y()))
            self.Cache[serie].setVisible(serie.isVisible())  # 隐藏那些不可用的项
        self.adjustSize()  # 调整大小


class GraphicsProxyWidget(QtWidgets.QGraphicsProxyWidget):
    def __init__(self, *args, **kwargs):
        super(GraphicsProxyWidget, self).__init__(*args, **kwargs)
        self.setZValue(999)
        self.tipWidget = ToolTipWidget()
        self.setWidget(self.tipWidget)
        self.hide()

    def width(self):
        return self.size().width()

    def height(self):
        return self.size().height()

    def show(self, title, points, pos):
        self.setGeometry(QRectF(pos, self.size()))
        self.tipWidget.updateUi(title, points)
        super(GraphicsProxyWidget, self).show()


class LineStackChart(QtChart.QChartView):
    def __init__(self):
        super(LineStackChart, self).__init__()
        self.chart = QtChart.QChart()
        # chart.setAcceptHoverEvents(True)  # 接受鼠标悬浮事件
        # chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        # 数据集
        data_table = [
            ["邮件营销", [120, 432, 101, 134, 90, 230, 210]],
            ["联盟广告", [220, 182, 491, 234, 290, 330, 310]],
            ["视频广告", [150, 232, 201, 154, 190, 330, 410]],
            ["直接访问", [320, 332, 301, 334, 390, 330, 320]],
            ["搜索引擎", [820, 532, 901, 934, 690, 480, 920]]
        ]
        for series_name, data_list in data_table:
            # 每个数据集创建一条线
            series = QtChart.QLineSeries()
            for index, value in enumerate(data_list):
                series.append(index, value)
            series.setName(series_name)  # 设置图例
            series.setPointsVisible(True)  # 设置点可见
            series.hovered.connect(self.series_hovered)  # 鼠标悬停信号连接
            self.chart.addSeries(series)  # 各线加入图表
        # 图表chart设置
        self.chart.setTitle("QChart鼠标交互")
        self.chart.createDefaultAxes()  # 使用默认轴
        # 设置X轴Y轴
        axis_X = self.chart.axisX()
        axis_Y = self.chart.axisY()
        axis_X.setTickCount(len(data_table[0][1]))  # x轴刻度数量
        axis_Y.setTickCount(len(data_table[0][1]))  # y轴刻度数量
        # axis_X.setGridLineVisible(False)  # 隐藏x轴竖向线条
        axis_Y.setRange(0, 1000)
        # 自定义X轴
        axis_label = QtChart.QCategoryAxis(
            self.chart, labelsPosition=QtChart.QCategoryAxis.AxisLabelsPositionOnValue
        )
        axis_label.setGridLineVisible(False)  # 设置竖向线条不可见
        min_x = axis_X.min()
        max_x = axis_X.max()
        step = (max_x - min_x) / (len(data_table[0][1]) - 1)  # x轴间距
        self.x_category = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        for i in range(len(self.x_category)):
            axis_label.append(self.x_category[i], min_x + i * step)
        self.chart.setAxisX(axis_label, self.chart.series()[-1])
        # 图例legend设置
        legend = self.chart.legend()
        legend.setMarkerShape(QtChart.QLegend.MarkerShapeFromSeries)  # 由线条设置图例
        # 绑定图例信号(鼠标动作)
        for marker in legend.markers():
            marker.clicked.connect(self.legend_clicked)  # 鼠标点击信号
            marker.hovered.connect(self.legend_hovered)  # 鼠标悬停信号
        # 图线抗锯齿
        self.setRenderHint(QPainter.Antialiasing)
        # 设置图表在容器上
        self.setChart(self.chart)
        # 线条对象
        self.line_item = QtWidgets.QGraphicsLineItem(self.chart)
        # 提示块
        self.tips_tool = GraphicsProxyWidget(self.chart)
        # 一些固定计算，减少mouseMoveEvent中的计算量
        # 获取x和y轴的最小最大值
        # axisX, axisY = self.chart.axisX(), self.chart.axisY()
        # self.min_x, self.max_x = axisX.min(), axisX.max()
        # self.min_y, self.max_y = axisY.min(), axisY.max()
        self.min_x, self.max_x = min_x, max_x
        self.min_y, self.max_y = axis_Y.min(), axis_Y.max()

    def legend_clicked(self):
        marker = self.sender()
        if not marker:
            return
        visible = not marker.series().isVisible()
        marker.series().setVisible(visible)
        marker.setVisible(True)  # 线条隐藏了，图例也会消失，要保证图例可见
        # 透明度设置
        alpha = 1.0 if visible else 0.4
        # 设置图例label的透明度
        label_brush = marker.labelBrush()
        label_color = label_brush.color()
        label_color.setAlphaF(alpha)
        label_brush.setColor(label_color)
        marker.setLabelBrush(label_brush)
        # 设置图例marker的透明度(存疑，似乎没效果)
        marker_brush = marker.brush()
        marker_color = marker_brush.color()
        marker_color.setAlphaF(alpha)
        marker_brush.setColor(marker_color)
        marker.setBrush(marker_brush)
        # 设置图例画笔透明度(存疑，似乎没效果)
        pen = marker.pen()
        color = pen.color()
        color.setAlphaF(alpha)
        pen.setColor(color)
        marker.setPen(pen)

    def legend_hovered(self, state):
        marker = self.sender()
        if not marker:
            return
        series = marker.series()
        if not series:
            return
        pen = series.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if state else -1))
        series.setPen(pen)

    def series_hovered(self, point, state):
        # 鼠标悬停信号槽函数：state表示鼠标是否在线上(布尔值)
        series = self.sender()  # 获取获得鼠标信号的那条线
        pen = series.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if state else -1))
        series.setPen(pen)

    def resizeEvent(self, event):
        super(LineStackChart, self).resizeEvent(event)
        # 当窗口大小改变时需要重新计算
        # 坐标系中左上角顶点
        self.point_top = self.chart.mapToPosition(
            QPointF(self.min_x, self.max_y))
        # 坐标原点坐标
        self.point_bottom = self.chart.mapToPosition(
            QPointF(self.min_x, self.min_y))
        self.step_x = (self.max_x - self.min_x) / \
                      (self.chart.axisX().tickCount() + 1)

    def mouseMoveEvent(self, event):
        super(LineStackChart, self).mouseMoveEvent(event)  # 原先的hover事件
        pos = event.pos()
        # 鼠标位置转为坐标点
        x = self.chart.mapToValue(pos).x()
        y = self.chart.mapToValue(pos).y()
        # print(self.chart.axisX().tickCount(), self.min_x, self.max_x)
        # step_x = (self.max_x - self.min_x) / (self.chart.axisX().tickCount() - 1)
        index = round((x - self.min_x) / self.step_x)
        # 坐标系中的所有正常显示的series的类型和点
        points = [(serie, serie.at(index))
                  for serie in self.chart.series()
                  if self.min_x <= x <= self.max_x and
                  self.min_y <= y <= self.max_y]
        # point_top = self.chart.mapToPosition(QPointF(self.min_x, self.max_y))  # y轴最高点
        # point_bottom = self.chart.mapToPosition(QPointF(self.min_x, self.min_y))
        if points:
            pos_x = self.chart.mapToPosition(QPointF(index * self.step_x + self.min_x, self.min_y))  # 算出当前鼠标所在的x位置
            # 自定义指示线
            self.line_item.setLine(pos_x.x(), self.point_top.y(),
                                   pos_x.x(), self.point_bottom.y())
            self.line_item.show()
            try:
                title = self.x_category[index]
            except Exception:
                title = ''
            tips_width = self.tips_tool.width()
            tips_height = self.tips_tool.height()
            # 如果鼠标位置离右侧的距离小于tip宽度
            x = pos.x() - tips_width if self.width() - \
                                     pos.x() - 20 < tips_width else pos.x()
            # 如果鼠标位置离底部的高度小于tip高度
            y = pos.y() - tips_height if self.height() - \
                                      pos.y() - 20 < tips_height else pos.y()
            # print(title, points, QPoint(x, y))
            self.tips_tool.show(
                title, points, QPoint(x, y))

        else:
            self.tips_tool.hide()
            self.line_item.hide()


