#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
author：yannan1
since：2023-02-09
"""

import os
import cv2
import numpy as np
from collections import Counter

from docset import DocSet


class DocsetScaner:
    CLS, DET, SEG = range(3)
    TASK2ID = {
        'Classification': CLS,
        'Detection': DET,
        'Segmentation': SEG,
    }

    def __init__(self, path: str):
        self.docs = DocSet(path, 'r')
        self.name2idx: dict = self.get_scaner()
        self.shapes = []
        self.info = self.get_info()
        self.task = self.get_task()
        self.cur_color_mask = None
        self.docset_name = os.path.basename(path)

    def get_task(self):
        if 'Segmentation' in self.info['Task']:
            return self.TASK2ID['Segmentation']
        elif 'Detection' in self.info['Task']:
            return self.TASK2ID['Detection']
        return self.TASK2ID['Classification']

    def get_info(self) -> dict:
        return self.docs._meta_doc

    def len(self):
        return len(self.docs)

    def get_scaner(self) -> dict:
        name2idx = {}
        for idx, doc in enumerate(self.docs):
            filename = doc['filename']
            if filename in name2idx:
                filename = f'{filename}-{idx}'
            name2idx[filename] = idx

        return name2idx

    def get_all_filenames(self, is_sort=True):
        if is_sort:
            return sorted(list(self.name2idx.keys()))

        return list(self.name2idx.keys())

    def get_shapes_cls(self, idx):
        doc = self.docs[idx]
        shapes = [(doc['label_name'], [(0, 0)])]
        return shapes

    def get_shapes_ob(self, idx) -> list:
        doc = self.docs[idx]
        shapes = []
        for bbox in doc['bboxes']:
            x_min, y_min, x_max, y_max = bbox['box']
            label_name = bbox['label_name']
            points = [(x_min, y_min), (x_max, y_min), (x_max, y_max), (x_min, y_max)]
            shapes.append((label_name, points))
        return shapes

    def get_shapes_seg(self, idx):
        doc = self.docs[idx]
        shapes = []
        mask = byte2cv(doc['mask'])

        labels = Counter(mask.flatten().tolist()).keys()
        for label in labels:
            if label == 0:
                continue
            tmp = np.where(mask == label)
            points = zip(tmp[1], tmp[0])
            label_name = self.info['Labels'][str(label)]
            shapes.append((label_name, points))

        return shapes

    def get_shapes(self, idx):
        methods = [self.get_shapes_cls, self.get_shapes_ob, self.get_shapes_seg]
        return methods[self.task](idx)

    def __getitem__(self, idx):
        return self.docs[idx]

    def __del__(self):
        self.docs.close()


def cv2byte(cvimg):
    _, img_encode = cv2.imencode('.png', cvimg)
    img_bytes = img_encode.tobytes()
    return img_bytes


def byte2cv(img_byte, mode=0):
    img_buffer_numpy = np.frombuffer(img_byte, dtype=np.uint8)  # 将 图片字节码bytes  转换成一维的numpy数组 到缓存中
    cvimg = cv2.imdecode(img_buffer_numpy, mode)
    return cvimg
