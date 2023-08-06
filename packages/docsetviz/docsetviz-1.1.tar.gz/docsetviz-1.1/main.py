#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
author：yannan1
since：2023-02-09
"""

import sys
from functools import partial

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt

from libs.utils import *
from libs.shape import Shape
from libs.canvas import Canvas
from libs.zoom_widget import ZoomWidget
from libs.tool_bar import ToolBar
from libs.hashable_qlist_widget_item import *
from libs.docset_scaner import DocsetScaner
from libs.remote_dialog import RemoteDialog

__appname__ = 'DocsetViz'


class WindowMixin(object):

    def menu(self, title: str, actions=None):
        """
        菜单栏
        Parameters
        ----------
        title: 菜单栏名称
        actions: 菜单事件

        Returns
        -------

        Examples
        -------
        self.menus = Struct(
            file=self.menu('文件'))
        add_actions(self.menus.file, (open, quit))

        """
        menu = self.menuBar().addMenu(title)
        if actions:
            add_actions(menu, actions)
        return menu

    def toolbar(self, title, actions=None):
        """
        左侧工具栏
        Parameters
        ----------
        title: 名称
        actions: 事件

        Returns
        -------

        Examples
        -------
        self.tools = self.toolbar('Tools')  # 左侧菜单栏

        """
        toolbar = ToolBar(title)
        # toolbar.setObjectName(u'%sToolBar' % title)  # setObjectName 可与findChild一起使用
        # toolbar.setOrientation(Qt.Vertical)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  # 设置工具栏的按钮样式，文字在图标下方
        if actions:
            add_actions(toolbar, actions)
        self.addToolBar(Qt.LeftToolBarArea, toolbar)  # 将toolbar放置在左侧
        return toolbar


class MainWindow(QMainWindow, WindowMixin):
    FIT_WINDOW, FIT_WIDTH, MANUAL_ZOOM = list(range(3))

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(__appname__)

        self.m_img_list = []  # 图片列表
        self.img_count = len(self.m_img_list)  # docset中的图片数量
        self.cur_img_idx = 0  # 当前显示的图片index
        self.scaner = None  # docset scaner

        self.items_to_shapes = {}  # label_item与之对应的shape
        self.shapes_to_items = {}  # ?

        """
        list_layout 右上角
        """
        list_layout = QVBoxLayout()
        list_layout.setContentsMargins(0, 0, 0, 0)

        # 选择是否要绘制label和显示label name的checkbox
        self.paint_shapes_checkbox = QCheckBox('显示标签')
        self.paint_shapes_checkbox.setChecked(True)
        self.paint_shapes_checkbox.stateChanged.connect(self.toggle_paint_shapes_option)
        self.display_label_option = QCheckBox('显示类别')
        self.display_label_option.setChecked(False)
        self.display_label_option.stateChanged.connect(self.toggle_display_label_option)
        list_layout.addWidget(self.paint_shapes_checkbox)
        list_layout.addWidget(self.display_label_option)

        # 输入图片名，显示特定图片
        specific_image_layout = QHBoxLayout()
        image_name_label = QLabel('图片名称: ')
        self.image_name_line_edit = QLineEdit()
        self.submit_button = QPushButton('确认')
        self.submit_button.setEnabled(False)
        self.submit_button.clicked.connect(self.toggle_show_specific_image)
        specific_image_layout.addWidget(image_name_label)
        specific_image_layout.addWidget(self.image_name_line_edit)
        specific_image_layout.addWidget(self.submit_button)

        specific_image_container = QWidget()
        specific_image_container.setLayout(specific_image_layout)
        list_layout.addWidget(specific_image_container)

        self.label_list = QListWidget()  # 显示label名称的控件
        self.label_list.itemSelectionChanged.connect(self.label_selection_changed)  # 单击选择item时，发出信号
        self.label_list.itemChanged.connect(self.label_item_changed)  # item的状态是否可见
        list_layout.addWidget(self.label_list)

        label_list_container = QWidget()
        label_list_container.setLayout(list_layout)

        self.dock = QDockWidget('选项', self)
        # self.dock.setObjectName('labels')
        self.dock.setWidget(label_list_container)

        """
        file_list_layout 右下角文件列表
        """
        self.file_list_widget = QListWidget()
        self.file_list_widget.itemDoubleClicked.connect(self.file_item_double_clicked)  # 双击选择文件
        file_list_layout = QVBoxLayout()
        file_list_layout.setContentsMargins(0, 0, 0, 0)
        file_list_layout.addWidget(self.file_list_widget)
        file_list_container = QWidget()
        file_list_container.setLayout(file_list_layout)
        self.file_dock = QDockWidget('图片列表', self)
        # self.file_dock.setObjectName('files')
        self.file_dock.setWidget(file_list_container)

        self.canvas = Canvas(parent=self)  # 中间区域

        scroll = QScrollArea()
        scroll.setWidget(self.canvas)
        scroll.setWidgetResizable(True)
        self.scroll_bars = {
            Qt.Vertical: scroll.verticalScrollBar(),
            Qt.Horizontal: scroll.horizontalScrollBar()
        }
        self.scroll_area = scroll
        self.canvas.scrollRequest.connect(self.scroll_request)

        # 设置窗口中控件的位置
        self.setCentralWidget(self.scroll_area)  # 设置中心控件
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)  # 设置屏幕右侧区域
        self.addDockWidget(Qt.RightDockWidgetArea, self.file_dock)
        self.file_dock.setFeatures(QDockWidget.DockWidgetFloatable)
        # QDockWidget.DockWidgetClosable 设置可关闭
        # QDockWidget.DockWidgetFloatable 设置可悬浮
        self.dock_features = QDockWidget.DockWidgetClosable | QDockWidget.DockWidgetFloatable
        self.dock.setFeatures(self.dock.features() ^ self.dock_features)

        # Actions
        action = partial(new_action, self)
        open = action('打开文件', self.open, 'Ctrl+O', 'open', 'openFileDetail')
        quit = action('退出', self.close, 'Ctrl+Q', 'quit', 'quitApp')
        open_remote = action('打开远程文件', self.open_remote, 'Ctrl+U', None, None)
        open_prev_image = action('上一个图像', self.open_prev_image, 'a', 'prev', 'prevImgDetail', enabled=False)
        open_next_image = action('下一个图像', self.open_next_image, 'd', 'next', 'nextImgDetail', enabled=False)
        info = action('文件信息', self.show_info, None, None, None, enabled=False)

        self.remote_dialog = RemoteDialog(parent=self)

        # 显示图片区域的缩放操作
        self.canvas.zoomRequest.connect(self.zoom_request)
        self.zoom_widget = ZoomWidget()
        zoom = QWidgetAction(self)
        zoom.setDefaultWidget(self.zoom_widget)
        self.zoom_widget.setEnabled(False)  # 按钮灰色，不可点击

        zoom_in = action('放大画面', partial(self.add_zoom, 10),
                         'Ctrl++', 'zoom-in', 'zoominDetail', enabled=False)
        zoom_out = action('缩小画面', partial(self.add_zoom, -10),
                          'Ctrl+-', 'zoom-out', 'zoomoutDetail', enabled=False)
        zoom_org = action('原始大小', partial(self.set_zoom, 100),
                          'Ctrl+=', 'zoom', 'originalsizeDetail', enabled=False)
        fit_window = action('适配屏幕', self.set_fit_window,
                            'Ctrl+F', 'fit-window', 'fitWinDetail',
                            checkable=True, enabled=False)
        fit_width = action('适配图像', self.set_fit_width,
                           'Ctrl+Shift+F', 'fit-width', 'fitWidthDetail',
                           checkable=True, enabled=False)
        # Group zoom controls into a list for easier toggling.
        self.zoom_mode = self.MANUAL_ZOOM
        self.scalers = {
            self.FIT_WINDOW: self.scale_fit_window,
            self.FIT_WIDTH: self.scale_fit_width,
            # Set to one to scale to 100% when loading files.
            self.MANUAL_ZOOM: lambda: 1,
        }
        self.zoom_widget.valueChanged.connect(self.paint_canvas)  # 中间区域值改变时重新绘制

        # Store actions for further handling.
        self.actions = Struct(open=open,
                              zoom=zoom, zoomIn=zoom_in, zoomOut=zoom_out, zoomOrg=zoom_org,
                              fitWindow=fit_window, fitWidth=fit_width,
                              zoomActions=(self.zoom_widget, zoom_in, zoom_out,
                                           zoom_org, fit_window, fit_width),
                              fileMenuActions=(open, quit),
                              beginner=(open, open_remote, open_prev_image, open_next_image,
                                        zoom_in, zoom, zoom_out, fit_window, fit_width, info),
                              afterOpenActions=(open_prev_image, open_next_image, info))

        # 菜单栏
        # self.menus = Struct(
        #     file=self.menu('文件'))
        # add_actions(self.menus.file, (open, quit))

        """
        左侧菜单栏
        """
        self.tools = self.toolbar('Tools')  # 左侧菜单栏
        self.populate_mode_actions()  # 加载左侧菜单栏
        self.setContextMenuPolicy(Qt.NoContextMenu) # 禁用主窗口的上下文菜单, 设置后在toolbar右键就不会出现菜单了

        """
        底部状态栏
        """
        self.statusBar().showMessage('%s started.' % __appname__)
        self.statusBar().show()
        self.label_coordinates = QLabel('')  # 状态栏右侧显示x, y, width, height
        self.statusBar().addPermanentWidget(self.label_coordinates)  # 在状态栏中永久添加给定的窗口小控件

        # Application state.
        self.image = QImage()  # 中间区域显示的图片数据
        self.filename = None  # 中间区域显示的图片名称
        self.zoom_level = 100
        self.fit_window = False

        height, width = get_desktop_size()  # 获得屏幕的长宽
        position = QPoint(0, 0)
        saved_position = position
        # Fix the multiple monitors issue
        for i in range(QApplication.desktop().screenCount()):
            if QApplication.desktop().availableGeometry(i).contains(saved_position):
                position = saved_position
                break
        self.resize(width, height)
        self.move(position)

    def populate_mode_actions(self):
        """
        加载左侧菜单栏的
        """
        tool = self.actions.beginner
        self.tools.clear()
        add_actions(self.tools, tool)

    def init_actions(self, value: bool = True) -> None:
        """
        打开docset文件后，使得控件可用
        Parameters
        ----------
        value: 是否enable

        Returns
        -------

        """
        for z in self.actions.zoomActions:
            z.setEnabled(value)

        for z in self.actions.afterOpenActions:
            z.setEnabled(value)
        self.submit_button.setEnabled(True)

    def status_bar_show_message(self, message: str, timeout: int = 5000) -> None:
        """
        状态栏显示信息
        Parameters
        ----------
        message: 显示的信息
        timeout: 显示的时长

        Returns
        -------

        """
        self.statusBar().showMessage(message, timeout)

    def reset_state(self) -> None:
        self.items_to_shapes.clear()
        self.shapes_to_items.clear()
        self.label_list.clear()
        self.filename = None
        self.image = QImage()
        self.canvas.reset_state()
        self.label_coordinates.clear()

    def label_list_current_item(self):
        """
        label_list 当前选中的label
        Returns
        -------

        """
        items = self.label_list.selectedItems()
        if items:
            return items[0]
        return None

    def add_label(self, shape):
        item = HashableQListWidgetItem(shape.label)
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Checked)

        r, g, b = shape.line_color.red(), shape.line_color.green(), shape.line_color.blue()
        label_color = QColor(r, g, b, 100)
        item.setBackground(label_color)

        self.items_to_shapes[item] = shape
        self.shapes_to_items[shape] = item
        self.label_list.addItem(item)

    def load_labels(self, index):
        s = []
        shapes = self.scaner.get_shapes(index)
        for label, points in shapes:
            is_paint_label = self.display_label_option.isChecked()
            line_color = generate_color_by_text(label)

            shape = Shape(label=label,
                          paint_label=is_paint_label,
                          line_color=line_color,
                          task=self.scaner.task)
            # points = [(x_min, y_min), (x_max, y_min), (x_max, y_max), (x_min, y_max)] # ob
            for x, y in points:
                # Ensure the labels are within the bounds of the image. If not, fix them.
                x, y = self.canvas.snap_point_to_canvas(x, y)
                shape.add_point(QPointF(x, y))

            shape.close()
            s.append(shape)

            self.add_label(shape)
        self.canvas.load_shapes(s)  # ?

    def label_selection_changed(self) -> None:
        """
        label_list里label被选中
        Returns
        -------

        """
        item = self.label_list_current_item()
        if item:
            self.canvas.select_shape(self.items_to_shapes[item])  # ?

    def label_item_changed(self, item):
        """
        label_list的label是否可见
        """
        shape = self.items_to_shapes.get(item, None)
        if shape:
            self.canvas.set_shape_visible(shape, item.checkState() == Qt.Checked)

    def file_item_double_clicked(self, item) -> None:
        filename = item.text()
        self.cur_img_idx = self.scaner.name2idx.get(filename)
        self.load_file(filename)

    def scroll_request(self, delta, orientation):
        units = - delta / (8 * 15)
        bar = self.scroll_bars[orientation]
        bar.setValue(int(bar.value() + bar.singleStep() * units))

    def set_zoom(self, value):
        self.actions.fitWidth.setChecked(False)
        self.actions.fitWindow.setChecked(False)
        self.zoom_mode = self.MANUAL_ZOOM
        # Arithmetic on scaling factor often results in float
        # Convert to int to avoid type errors
        self.zoom_widget.setValue(int(value))

    def add_zoom(self, increment=10):
        self.set_zoom(self.zoom_widget.value() + increment)

    def zoom_request(self, delta):
        # get the current scrollbar positions
        # calculate the percentages ~ coordinates
        h_bar = self.scroll_bars[Qt.Horizontal]
        v_bar = self.scroll_bars[Qt.Vertical]

        # get the current maximum, to know the difference after zooming
        h_bar_max = h_bar.maximum()
        v_bar_max = v_bar.maximum()

        # get the cursor position and canvas size
        # calculate the desired movement from 0 to 1
        # where 0 = move left
        #       1 = move right
        # up and down analogous
        cursor = QCursor()
        pos = cursor.pos()
        relative_pos = QWidget.mapFromGlobal(self, pos)

        cursor_x = relative_pos.x()
        cursor_y = relative_pos.y()

        w = self.scroll_area.width()
        h = self.scroll_area.height()

        # the scaling from 0 to 1 has some padding
        # you don't have to hit the very leftmost pixel for a maximum-left movement
        margin = 0.1
        move_x = (cursor_x - margin * w) / (w - 2 * margin * w)
        move_y = (cursor_y - margin * h) / (h - 2 * margin * h)

        # clamp the values from 0 to 1
        move_x = min(max(move_x, 0), 1)
        move_y = min(max(move_y, 0), 1)

        # zoom in
        units = delta // (8 * 15)
        scale = 10
        self.add_zoom(scale * units)

        # get the difference in scrollbar values
        # this is how far we can move
        d_h_bar_max = h_bar.maximum() - h_bar_max
        d_v_bar_max = v_bar.maximum() - v_bar_max

        # get the new scrollbar values
        new_h_bar_value = int(h_bar.value() + move_x * d_h_bar_max)
        new_v_bar_value = int(v_bar.value() + move_y * d_v_bar_max)

        h_bar.setValue(new_h_bar_value)
        v_bar.setValue(new_v_bar_value)

    def set_fit_window(self, value=True):
        if value:
            self.actions.fitWidth.setChecked(False)
        self.zoom_mode = self.FIT_WINDOW if value else self.MANUAL_ZOOM
        self.adjust_scale()

    def set_fit_width(self, value=True):
        if value:
            self.actions.fitWindow.setChecked(False)
        self.zoom_mode = self.FIT_WIDTH if value else self.MANUAL_ZOOM
        self.adjust_scale()

    def scale_fit_window(self):
        """Figure out the size of the pixmap in order to fit the main widget."""
        e = 2.0  # So that no scrollbars are generated.
        w1 = self.centralWidget().width() - e
        h1 = self.centralWidget().height() - e
        a1 = w1 / h1
        # Calculate a new scale value based on the pixmap's aspect ratio.
        w2 = self.canvas.pixmap.width() - 0.0
        h2 = self.canvas.pixmap.height() - 0.0
        a2 = w2 / h2
        return w1 / w2 if a2 >= a1 else h1 / h2

    def scale_fit_width(self):
        # The epsilon does not seem to work too well here.
        w = self.centralWidget().width() - 2.0
        return w / self.canvas.pixmap.width()

    def load_file(self, filename: str = None) -> bool:
        """
        显示特定图片
        Parameters
        ----------
        filename: 显示的图片名

        Returns
        -------

        """
        self.reset_state()  # 重置状态
        self.canvas.setEnabled(False)  # 设置canvas不可用，因为本次调用占用

        index = self.scaner.name2idx.get(filename, 0)  # 要显示的图片index
        if index is not None and filename in self.m_img_list:  # 如果index不为空
            arr_idx = self.m_img_list.index(filename)
            self.cur_img_idx = arr_idx
            file_widget_item = self.file_list_widget.item(arr_idx)
            file_widget_item.setSelected(True)
            self.file_list_widget.setCurrentRow(self.cur_img_idx) # 滚动条随显示的行滚动
        else:
            self.error_message(u'Error opening file',
                               u"<p>Make sure <i>%s</i> is a valid image file." % filename)
            self.status_bar_show_message("Error reading %s" % filename)
            return False

        self.status_bar_show_message("Loaded %s" % filename)
        self.filename = filename  # 设置当前展示的图片名

        self.image = read(self.scaner[index]['image'])
        self.canvas.load_pixmap(self.image)
        if self.paint_shapes_checkbox.isChecked():
            self.load_labels(index)

        self.canvas.setEnabled(True)
        self.adjust_scale(initial=True)  # ?
        self.paint_canvas()  # ?
        self.init_actions(True)

        counter = self.counter_str()
        self.setWindowTitle(f'{__appname__} {self.scaner.docset_name}  {filename} {counter}')

        # 最后一个item为选中状态
        if self.label_list.count():
            self.label_list.setCurrentItem(self.label_list.item(self.label_list.count() - 1))
            self.label_list.item(self.label_list.count() - 1).setSelected(True)

        self.canvas.setFocus(True)
        return True

    def counter_str(self) -> str:
        """
        生成数量字符串
        Returns
        -------

        """
        return '[{} / {}]'.format(self.cur_img_idx + 1, self.img_count)

    def resizeEvent(self, event):
        if self.canvas and not self.image.isNull() \
                and self.zoom_mode != self.MANUAL_ZOOM:
            self.adjust_scale()
        super(MainWindow, self).resizeEvent(event)

    def paint_canvas(self):
        assert not self.image.isNull(), "cannot paint null image"
        self.canvas.scale = 0.01 * self.zoom_widget.value()
        self.canvas.label_font_size = int(0.01 * max(self.image.width(), self.image.height())*self.canvas.scale/2)
        self.canvas.adjustSize()
        self.canvas.update()

    def adjust_scale(self, initial=False):
        value = self.scalers[self.FIT_WINDOW if initial else self.zoom_mode]()
        self.zoom_widget.setValue(int(100 * value))

    def open(self):
        filters = "docset file (%s)" % ' '.join(['*.ds'])
        ds_path, _ = QFileDialog.getOpenFileName(self, "打开", './', filters)
        self.import_ds_images(ds_path)

    def open_remote(self):
        ds_path = self.remote_dialog.pop_up()
        self.import_ds_images(ds_path)

    def import_ds_images(self, ds_path):
        if not ds_path:
            return

        self.scaner = DocsetScaner(ds_path)
        self.filename = None
        self.file_list_widget.clear()
        self.m_img_list = self.scaner.get_all_filenames()
        self.img_count = self.scaner.len()

        print(self.file_list_widget.verticalScrollBar().value())
        for filename in self.m_img_list:
            item = QListWidgetItem(filename)
            self.file_list_widget.addItem(item)

        self.open_next_image()

    def open_prev_image(self, _value=False):
        if self.img_count <= 0:
            return

        if self.filename is None:
            return

        if self.cur_img_idx - 1 >= 0:
            self.cur_img_idx -= 1
            filename = self.m_img_list[self.cur_img_idx]
            if filename:
                self.load_file(filename)

    def open_next_image(self, _value=False):
        if self.img_count <= 0:
            return

        if not self.m_img_list:
            return

        filename = None
        if self.filename is None:
            filename = self.m_img_list[0]
            self.cur_img_idx = 0
        else:
            if self.cur_img_idx + 1 < self.img_count:
                self.cur_img_idx += 1
                filename = self.m_img_list[self.cur_img_idx]

        if filename:
            self.load_file(filename)

    def error_message(self, title, message):
        return QMessageBox.critical(self, title,
                                    '<p><b>%s</b></p>%s' % (title, message))

    def show_info(self):
        info = self.scaner.get_info()
        msg = "Data Name: {}\n" \
              "Task: {}\n" \
              "Source: {}\n" \
              "License: {}\n" \
              "Description: {}" \
            .format(info['Data Name'], info['Task'], info['Source'], info['License'], info['Description'])

        info_box = QMessageBox(self)
        info_box.setTextInteractionFlags(Qt.TextSelectableByMouse)
        info_box.setText(msg)
        info_box.setWindowTitle('信息')
        info_box.exec()

    def toggle_display_label_option(self):
        if self.filename is not None and self.scaner.task != self.scaner.SEG:
            self.load_file(self.filename)

    def toggle_paint_shapes_option(self):
        if self.filename is not None:
            self.load_file(self.filename)

    def toggle_show_specific_image(self):
        filename = self.image_name_line_edit.text()
        self.cur_img_idx = self.scaner.name2idx.get(filename, 0)
        if filename.strip() == '':
            QMessageBox.about(self, "提示", "文件名不可为空")
        else:
            self.load_file(filename)
            self.image_name_line_edit.clear()


def read(image_bytes):
    img_pix = QPixmap()
    img_pix.loadFromData(image_bytes)
    return img_pix


def get_main_app(argv=None):
    """
    Standard boilerplate Qt application code.
    Do everything but app.exec_() -- so that we can test the application in one thread
    """
    if not argv:
        argv = []
    app = QApplication(argv)
    app.setApplicationName(__appname__)
    app.setWindowIcon(new_icon("app"))
    win = MainWindow()
    win.show()
    return app, win


def main():
    """construct main app and run it"""
    app, _win = get_main_app(sys.argv)
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())
