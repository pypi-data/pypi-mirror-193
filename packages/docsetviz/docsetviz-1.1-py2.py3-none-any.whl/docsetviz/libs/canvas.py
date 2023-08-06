#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
author：yannan1
since：2023-02-09
"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from libs.shape import Shape

CURSOR_DEFAULT = Qt.ArrowCursor
CURSOR_POINT = Qt.PointingHandCursor  # 向上的小手
CURSOR_GRAB = Qt.OpenHandCursor  # 打开的小手


class Canvas(QWidget):
    zoomRequest = pyqtSignal(int)
    scrollRequest = pyqtSignal(int, int)
    selectionChanged = pyqtSignal(bool)

    epsilon = 24.0

    def __init__(self, *args, **kwargs):
        super(Canvas, self).__init__(*args, **kwargs)
        # Initialise local state.
        self.shapes = []  # 显示的image的shapes
        self.current = None  # ？
        self.selected_shape = None  # 被选中的shape
        self.selected_shape_copy = None  # ？
        self.drawing_line_color = QColor(0, 0, 255)  # ?
        self.drawing_rect_color = QColor(0, 0, 255)  # ?
        self.line = Shape(line_color=self.drawing_line_color)  # ?
        self.scale = 1.0
        self.label_font_size = 8
        self.pixmap = QPixmap()
        self.visible = {}  # ？
        self.h_shape = None  # 高亮shape
        self._painter = QPainter()
        self._cursor = CURSOR_POINT  # CURSOR_DEFAULT
        # Set widget options.
        self.setMouseTracking(True)
        self.setFocusPolicy(Qt.WheelFocus)  # canvas获得焦点的方式为用键盘、点击鼠标和滚轮

        self.pan_initial_pos = QPoint()

    def enterEvent(self, ev):
        """鼠标移入事件， 当鼠标移入canvas后，鼠标变为self._cursor"""
        self.override_cursor(self._cursor)

    def leaveEvent(self, ev):
        """鼠标移除事件，当鼠标移出canvas后，鼠标图标重置"""
        self.restore_cursor()

    def focusOutEvent(self, ev):
        """控件失去焦点事件"""
        self.restore_cursor()

    def isVisible(self, shape) -> bool:
        """shape是否可见"""
        return self.visible.get(shape, True)

    def un_highlight(self, shape=None):
        """取消shape highlight"""
        if shape is None or shape == self.h_shape:
            if self.h_shape:
                self.h_shape.highlight_clear()
            self.h_shape = None

    def mouseMoveEvent(self, ev):
        """鼠标移动事件，Update line with last point and current coordinates."""
        pos = self.transform_pos(ev.pos())

        # Update coordinates in status bar if image is opened
        window = self.parent().window()
        if window.filename is not None:  # 如果控件中有显示图片
            self.parent().window().label_coordinates.setText(
                'X: %d; Y: %d' % (pos.x(), pos.y()))

        if Qt.LeftButton & ev.buttons():  # 按下左键后移动鼠标可移动图像
            delta = ev.pos() - self.pan_initial_pos
            self.scrollRequest.emit(delta.x(), Qt.Horizontal)
            self.scrollRequest.emit(delta.y(), Qt.Vertical)
            self.update()

        priority_list = self.shapes + ([self.selected_shape] if self.selected_shape else [])  #
        for shape in reversed([s for s in priority_list if self.isVisible(s)]):
            if shape.contains_point(pos):
                self.h_shape = shape
                self.override_cursor(CURSOR_GRAB)

                # Display annotation width and height while hovering inside
                point1 = self.h_shape[1]
                point3 = self.h_shape[3]
                current_width = abs(point1.x() - point3.x())
                current_height = abs(point1.y() - point3.y())
                self.parent().window().label_coordinates.setText(
                    'Width: %d, Height: %d / X: %d; Y: %d' % (current_width, current_height, pos.x(), pos.y()))
                break
        else:  # Nothing found, clear highlights, reset state.
            if self.h_shape:
                self.h_shape.highlight_clear()
                self.update()
            self.h_shape = None
            self.override_cursor(CURSOR_DEFAULT)

    def mousePressEvent(self, ev):
        """
        鼠标按下事件
        """
        pos = self.transform_pos(ev.pos())

        if ev.button() == Qt.LeftButton:  # 鼠标点击左键
            selection = self.select_shape_point(pos)

            if selection is None:
                QApplication.setOverrideCursor(QCursor(CURSOR_GRAB))  # 鼠标左键按下出现打开的小手
                self.pan_initial_pos = ev.pos()

        elif ev.button() == Qt.RightButton:  # 鼠标点击右键
            self.select_shape_point(pos)
        self.update()

    def mouseReleaseEvent(self, ev):
        """
        鼠标释放事件
        """
        if ev.button() == Qt.LeftButton and self.selected_shape:
            self.override_cursor(CURSOR_GRAB)

        elif ev.button() == Qt.LeftButton:
            QApplication.restoreOverrideCursor()

    def select_shape(self, shape):
        self.de_select_shape()  # 取消已选中shape高亮
        shape.selected = True
        self.selected_shape = shape
        self.selectionChanged.emit(True)
        self.update()

    def select_shape_point(self, point):
        """
        鼠标点击，如果点击的位置有shape，则让其高亮
        Parameters
        ----------
        point: 鼠标点击的位置

        Returns
        -------

        """
        self.de_select_shape()
        for shape in reversed(self.shapes):  # reversed() 返回反转迭代器
            if self.isVisible(shape) and shape.contains_point(point):
                self.select_shape(shape)
                return self.selected_shape
        return None

    def snap_point_to_canvas(self, x, y):
        """
        Moves a point x,y to within the boundaries of the canvas.
        :return: (x,y,snapped) where snapped is True if x or y were changed, False if not.
        """
        if x < 0 or x > self.pixmap.width() or y < 0 or y > self.pixmap.height():
            x = max(x, 0)
            y = max(y, 0)
            x = min(x, self.pixmap.width())
            y = min(y, self.pixmap.height())
            return x, y

        return x, y

    def de_select_shape(self):
        """取消选中shape高亮"""
        if self.selected_shape:
            self.selected_shape.selected = False
            self.selected_shape = None
            self.selectionChanged.emit(False)
            self.update()

    def paintEvent(self, event):
        if not self.pixmap:
            return super(Canvas, self).paintEvent(event)

        p = self._painter
        p.begin(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.setRenderHint(QPainter.HighQualityAntialiasing)
        p.setRenderHint(QPainter.SmoothPixmapTransform)

        p.scale(self.scale, self.scale)
        p.translate(self.offset_to_center())

        p.drawPixmap(0, 0, self.pixmap)
        Shape.scale = self.scale
        Shape.label_font_size = self.label_font_size
        for shape in self.shapes:
            if self.isVisible(shape):
                shape.paint(p)

        p.end()

    def transform_pos(self, point):
        """Convert from widget-logical coordinates to painter-logical coordinates."""
        return point / self.scale - self.offset_to_center()

    def offset_to_center(self):
        s = self.scale
        area = super(Canvas, self).size()
        w, h = self.pixmap.width() * s, self.pixmap.height() * s
        aw, ah = area.width(), area.height()
        x = (aw - w) / (2 * s) if aw > w else 0
        y = (ah - h) / (2 * s) if ah > h else 0
        return QPointF(x, y)

    def out_of_pixmap(self, p):
        w, h = self.pixmap.width(), self.pixmap.height()
        return not (0 <= p.x() <= w and 0 <= p.y() <= h)

    # These two, along with a call to adjustSize are required for the
    # scroll area.
    def sizeHint(self):
        return self.minimumSizeHint()

    def minimumSizeHint(self):
        if self.pixmap:
            return self.scale * self.pixmap.size()
        return super(Canvas, self).minimumSizeHint()

    def wheelEvent(self, ev):
        qt_version = 4 if hasattr(ev, "delta") else 5
        if qt_version == 4:
            if ev.orientation() == Qt.Vertical:
                v_delta = ev.delta()
                h_delta = 0
            else:
                h_delta = ev.delta()
                v_delta = 0
        else:
            delta = ev.angleDelta()
            h_delta = delta.x()
            v_delta = delta.y()

        mods = ev.modifiers()
        # if int(Qt.ControlModifier) | int(Qt.ShiftModifier) == int(mods) and v_delta:
        #     self.lightRequest.emit(v_delta)
        if Qt.ControlModifier == int(mods) and v_delta:
            self.zoomRequest.emit(v_delta)
        else:
            v_delta and self.scrollRequest.emit(v_delta, Qt.Vertical)
            h_delta and self.scrollRequest.emit(h_delta, Qt.Horizontal)
        ev.accept()

    def keyPressEvent(self, ev):
        key = ev.key()
        if key == Qt.Key_Escape and self.current:
            print('ESC press')
            self.current = None
            # self.drawingPolygon.emit(False)
            self.update()

    def load_pixmap(self, pixmap):
        self.pixmap = pixmap
        self.shapes = []
        self.repaint()

    def load_shapes(self, shapes):
        self.shapes = list(shapes)
        self.current = None
        self.repaint()

    def set_shape_visible(self, shape, value: bool):
        """设置shape是否可见"""
        self.visible[shape] = value
        self.repaint()

    def current_cursor(self):
        cursor = QApplication.overrideCursor()
        if cursor is not None:
            cursor = cursor.shape()
        return cursor

    def override_cursor(self, cursor):
        self._cursor = cursor
        if self.current_cursor() is None:
            QApplication.setOverrideCursor(cursor)  # 设置应用成语的光标
        else:
            QApplication.changeOverrideCursor(cursor)

    def restore_cursor(self):
        QApplication.restoreOverrideCursor()

    def reset_state(self):
        self.de_select_shape()
        self.un_highlight()
        self.selected_shape_copy = None

        self.restore_cursor()
        self.pixmap = None
        self.update()
