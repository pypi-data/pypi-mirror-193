## About
The docset must comply with the following format.
```python
## Classification
doc = {
    'filename'      : str,        # 图像文件名  
    'size'          : list,       # 图像大小 [height, wight, channel
    'image'         : bytes,      # 图像数据  
    'label'         : int,        # 标签id
    'label_name'    : str         # 标签名称
}

## Detection
doc = {
    'filename'      : str,        # 图像文件名    
    'size'          : list,       # 图像大小 [height, wight, channel]
    'image'         : bytes,      # 图像数据        
    'bbox': [{
        'box'       : list,       # box [xmin, ymin, xmax, ymax]
        'label'     : int,        # box的标签id
        'label_name': str         # box的标签名称
    }]               
}

## Segmentation
doc = { 
    'filename'      : str,        # 图像文件名 
    'size'          : list,       # 图像大小 [height, wight, channel]
    'image'         : bytes,      # 图像数据  
    'mask'          : np.ndarray, # int64
    'heatmap'       : np.ndarray  # float32
}
```


## Installation
#### Get from PyPI
```shell
pip install docsetviz
docsetviz
```

#### Build from source
##### Ubuntu
```shell
git clone https://gitlab.edgeai.org:8888/yannan1/datavisualization.git
cd docsetviz
pip install -r requirements.txt
python main.py
```
#### Windows
```shell
# Git clone source
git clone https://gitlab.edgeai.org:8888/yannan1/datavisualization.git

# Open cmd and go to the docsetviz directory
pip install -r requirements.txt
python main.py
```

## Usage
![usage.png](pictures%2Fusage.png)
##### 打开远程文件
click "打开远程文件", Enter the following information
![remote.png](pictures%2Fremote.png)

### Hotkeys
| function |    Hotkey    |
|:--------:|:------------:|
|   打开文件   |    Ctrl+O    |
|  打开远程文件  |    Ctrl+U    |
|  上一个图像   |      a       |
|  下一个图像   |      d       |
|   放大图像   |    Ctrl++    |
|   缩小画面   |    Ctrl+-    |
|   适配屏幕   |    Ctrl+F    |
|   适配图像   | Ctrl+Shift+F |

### Notice
1. 若Docset中包含多个任务的标签，将按Segmentation Detection Classification的顺序显示

## Error
##### 1. opencv and pyqt5 conflict
```
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "/home/yannan/anaconda3/lib/python3.9/site-packages/cv2/qt/plugins" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb, eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl.
```
##### resolution
```shell
## 方法1: 对opencv-python的版本没有特殊要求可采用此方法
pip uninstall opencv-python
pip install opencv-python-headless

## 方法2: conda安装pyqt
pip uninstall pyqt5
conda install pyqt
```

## TODO
2. 如果图片太大，边框的大小还是那么小，ob的框可随图像大小的比例改变 `/mnt/cephfs/data/dataset/global_wheat_challenge_2021/test.ds`
5. info显示不好看 x
3. 一次显示多张图片
4. 标签颜色看不清 x
 
## 已做
1. label_list降低透明度
2. 下载大文件页面卡顿，但下载未暂停 `/mnt/cephfs/data/dataset/global_wheat_challenge_2021/test.ds`
3. 放大图像后，左键可拖拽 
4. 左上角显示Docset名称
5. 图像列表 滚动条没有item选中滑动
6. toolbar 右键显示内容 
7. 多task mvtec_ad 
8. 字体的显示问题 `/mnt/cephfs/data/dataset/face_mask_detection/test.ds` `cifar10` `omniglot` `VisDA-2017`