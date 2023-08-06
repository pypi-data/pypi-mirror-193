#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
author：yannan1
since：2023-02-09
"""

import hashlib

from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import *


def new_icon(icon):
    return QIcon(':/' + icon)


def new_action(parent, text, slot=None, shortcut=None, icon=None,
               tip=None, checkable=False, enabled=True):
    """Create a new action and assign callbacks, shortcuts, etc."""
    a = QAction(text, parent)
    if icon is not None:
        a.setIcon(new_icon(icon))
    if shortcut is not None:
        if isinstance(shortcut, (list, tuple)):
            a.setShortcuts(shortcut)
        else:
            a.setShortcut(shortcut)
    if tip is not None:
        a.setToolTip(tip)
        a.setStatusTip(tip)
    if slot is not None:
        a.triggered.connect(slot)
    if checkable:
        a.setCheckable(True)
    a.setEnabled(enabled)
    return a


def add_actions(widget, actions):
    for action in actions:
        if action is None:
            widget.addSeparator()
        elif isinstance(action, QMenu):
            widget.addMenu(action)
        else:
            widget.addAction(action)


class Struct(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def format_shortcut(text):
    mod, key = text.split('+', 1)
    return '<b>%s</b>+<b>%s</b>' % (mod, key)


def generate_color_by_text(text: str) -> QColor:
    """
    根据文字生成颜色，一种label对应一个颜色
    Parameters
    ----------
    text: label_name

    Returns
    -------

    """
    s = text
    hash_code = int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16)
    r = int((hash_code / 255) % 255)
    g = int((hash_code / 65025) % 255)
    b = int((hash_code / 16581375) % 255)
    return QColor(r, g, b, 255)


def get_desktop_size() -> (int, int):
    """
    获得屏幕的尺寸
    Returns
    -------

    """
    desktop = QApplication.desktop()
    screen_rect = desktop.screenGeometry()
    height = screen_rect.height()
    width = screen_rect.width()
    return height, width
