#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
author：yannan1
since：2023-02-09
"""

import sys

from PyQt5.QtGui import *

DEFAULT_LINE_COLOR = QColor(0, 255, 0, 128)
DEFAULT_SELECT_LINE_COLOR = QColor(255, 255, 255)
DEFAULT_SELECT_FILL_COLOR = QColor(0, 128, 255, 155)


class Shape(object):
    CLS, DET, SEG = range(3)

    # The following class variables influence the drawing
    # of _all_ shape objects.
    line_color = DEFAULT_LINE_COLOR
    select_line_color = DEFAULT_SELECT_LINE_COLOR
    select_fill_color = DEFAULT_SELECT_FILL_COLOR
    scale = 1.0
    label_font_size = 8

    def __init__(self, label=None, line_color=None, paint_label=False, task=CLS):
        self.label = label
        self.points = []
        self.selected = False
        self.task = task
        self.paint_label = paint_label

        self._highlight_index = None
        self._closed = False
        self.is_seg = False
        self.line_color = line_color

    def close(self):
        self._closed = True

    def add_point(self, point):
        if self.task == self.SEG:
            point = point.toPoint()
        self.points.append(point)

    def is_closed(self):
        return self._closed

    def set_open(self):
        self._closed = False

    def paint_cls(self, painter):
        if self.paint_label:
            pen = QPen(self.line_color)
            painter.setPen(pen)
            min_y = int(1.25 * self.label_font_size)
            min_y = min_y - min_y * 0.015
            font = QFont()
            font.setPointSize(self.label_font_size)
            font.setBold(True)
            font.setLetterSpacing(QFont.PercentageSpacing, 75)  # 设置字体间距
            painter.setFont(font)
            painter.drawText(0, min_y, self.label)

    def paint_seg(self, painter):
        if self.points:
            pen = QPen(self.line_color)
            painter.setPen(pen)
            painter.drawPoints(QPolygon(self.points))

    def paint_ob(self, painter):
        if self.points:
            color = self.select_line_color if self.selected else self.line_color
            pen = QPen(color)
            pen.setWidth(max(1, int(round(2.0 / self.scale))))
            painter.setPen(pen)

            line_path = QPainterPath()
            line_path.moveTo(self.points[0])

            for i, p in enumerate(self.points):
                line_path.lineTo(p)
            if self.is_closed():
                line_path.lineTo(self.points[0])

            painter.drawPath(line_path)

            # Draw text at the top-left
            if self.paint_label:
                min_x = sys.maxsize
                min_y = sys.maxsize
                min_y_label = int(1.25 * self.label_font_size)
                for point in self.points:
                    min_x = min(min_x, point.x())
                    min_y = min(min_y, point.y())
                if min_x != sys.maxsize and min_y != sys.maxsize:
                    font = QFont()
                    # print(self.label_font_size)
                    font.setPointSize(self.label_font_size)
                    font.setBold(True)
                    # font.setLetterSpacing(QFont.PercentageSpacing, 75)  # 设置字体间距
                    # font.setFamily('SimHei')  # 设置字体为黑体
                    painter.setFont(font)
                    if self.label is None:
                        self.label = ""
                    if min_y < min_y_label:
                        min_y += min_y_label
                    min_y = min_y - min_y * 0.015
                    painter.drawText(int(min_x), int(min_y), self.label)

            if self.selected:
                painter.fillPath(line_path, self.select_fill_color)

    def paint(self, painter):
        methods = [self.paint_cls, self.paint_ob, self.paint_seg]
        return methods[self.task](painter)

    def contains_point(self, point) -> bool:
        """
        当前shape是否包含该point
        Parameters
        ----------
        point: 鼠标点击的位置点

        Returns
        -------
        shape是否包含point

        """
        return self.make_path().contains(point)

    def make_path(self):
        """将 self.points 转为 QPainterPath """
        path = QPainterPath(self.points[0])
        for p in self.points[1:]:
            path.lineTo(p)
        return path

    def highlight_clear(self):
        self._highlight_index = None

    def __len__(self):
        return len(self.points)

    def __getitem__(self, key):
        return self.points[key]

    def __setitem__(self, key, value):
        self.points[key] = value
