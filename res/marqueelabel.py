from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPainter, QPalette

class MarqueeLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(200)
        self.scroll_timer = QTimer(self)
        self.scroll_timer.timeout.connect(self.scroll_text)
        # 定时器间隔
        self.scroll_timer.setInterval(100)
        self.scroll_offset = 0
        # 滚动速度
        self.scroll_speed = 2
        self.text_content = ""
        self.text_width = 0
        self.is_scrolling = False
        # 窗口可见性标志
        self.is_visible = True

    def setText(self, text):
        self.text_content = text
        self.scroll_offset = 0
        self.text_width = self.fontMetrics().horizontalAdvance(text)

        # 只有当文本长度超过标签宽度且窗口可见时才启动滚动
        if self.text_width > self.width() and self.is_visible:
            if not self.is_scrolling:
                self.scroll_timer.start()
                self.is_scrolling = True
        else:
            if self.is_scrolling:
                self.scroll_timer.stop()
                self.is_scrolling = False
        self.update()

    def scroll_text(self):
        # 只有当窗口可见时才滚动
        if not self.is_visible:
            return

        self.scroll_offset += self.scroll_speed
        # 当文本完全滚动出视野后，重新开始
        if self.scroll_offset > self.text_width:
            self.scroll_offset = -self.width()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.palette().color(QPalette.Text))
        y_pos = self.height() // 2 + self.fontMetrics().ascent() // 2

        # 绘制主文本
        painter.drawText(-self.scroll_offset, y_pos, self.text_content)
        painter.end()

    def showEvent(self, event):
        # 窗口显示时更新可见性标志并重启滚动
        self.is_visible = True
        if self.text_width > self.width() and not self.is_scrolling:
            self.scroll_timer.start()
            self.is_scrolling = True
        super().showEvent(event)

    def hideEvent(self, event):
        # 窗口隐藏时更新可见性标志并停止滚动
        self.is_visible = False
        if self.is_scrolling:
            self.scroll_timer.stop()
            self.is_scrolling = False
        super().hideEvent(event)