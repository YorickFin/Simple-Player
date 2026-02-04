# cython: language_level=3

import re
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QWidget, QApplication
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtCore import Qt

# 窗口配置
class WindowSuper(QWidget):

    def init_ui(self):
        self.setWindowFlag(Qt.FramelessWindowHint)		#将界面设置为无框
        self.setAttribute(Qt.WA_TranslucentBackground)	#将界面属性设置为半透明
        self.shadow = QGraphicsDropShadowEffect()		#设定一个阴影, 半径为10, 颜色为#444444, 定位为0, 0
        self.shadow.setBlurRadius(4)
        self.shadow.setColor(QColor(2, 10, 25))
        self.shadow.setOffset(0, 0)
        self.ui.background.setGraphicsEffect(self.shadow)	#为frame设定阴影效果
        self.ui.icon.setPixmap(QPixmap(r"res\logo\logo_P.png"))

        self.desktop_size = [QApplication.instance().screens()[0].size().width(), QApplication.instance().screens()[0].size().height()]


#   --------------------------------------------------移动功能-------------------------------------------------

    def mousePressEvent(self, event):		#鼠标左键按下时获取鼠标坐标, 按下右键取消
        if event.button() == Qt.LeftButton:
            self._move_drag = True
            self.m_Position = event.globalPosition() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):	#鼠标在按下左键的情况下移动时, 根据坐标移动界面
        # 移动事件
        if Qt.LeftButton and self._move_drag:
            m_Point = event.globalPosition() - self.m_Position
            self.move(m_Point.x(), m_Point.y())
            event.accept()

    def mouseReleaseEvent(self, event):	#鼠标按键释放时, 取消移动
        self._move_drag = False


#   ------------------------------------------------界面大小自适应----------------------------------------------

    def windowAdaptation(self):
        # 获取当前屏幕分辨率
        screen_width, screen_height = self.desktop_size

        # 计算缩放系数（基于分辨率的线性插值）
        # 宽度缩放系数公式：scale_w = 1.7 + (screen_width - 1920) * (0.2 / 640)
        # 高度缩放系数公式：scale_h = 1.6 + (screen_width - 1920) * (0.2 / 640)
        scale_factor = (screen_width - 1920) * (0.2 / 640)
        scale_w = 1.7 + scale_factor
        scale_h = 1.6 + scale_factor

        # 计算窗口大小（添加18px的边框补偿）
        win_width = (screen_width / scale_w) + 18
        win_height = (screen_height / scale_h)

        # 计算窗口位置（水平居中，垂直微调）
        pos_x = (screen_width / 2) - (win_width / 2)
        pos_y = (screen_height / 2) - (win_height / 1.8)

        # 应用新尺寸和位置
        self.resize(win_width, win_height)
        self.move(pos_x, pos_y)


#   ------------------------------------------------文字大小自适应----------------------------------------------

    def textAdaptation(self, file_path, ui_object):
        # 基准分辨率（2560x1440）
        base_width = 2560

        # 计算非线性缩放因子（平方根函数使变化更平缓）
        scale_factor = (self.desktop_size[0] / base_width) ** 0.5

        # 读取qss
        with open(file_path, 'r', encoding="utf-8") as f:
            qss = f.read()

        # 修改字体大小（使用非线性缩放）
        def scale_font(match):
            original_size = int(match.group(1))
            # 应用非线性缩放并四舍五入
            scaled_size = max(8, round(original_size * scale_factor))  # 最小8pt保证可读性
            return f'{scaled_size}pt;'

        qss = re.sub(r'(\d+)pt;', scale_font, qss)

        # 应用qss
        ui_object.setStyleSheet(qss)