from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPainter, QPalette

class MarqueeLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(200)
        self.scroll_timer = QTimer(self)
        self.scroll_timer.timeout.connect(self.scroll_text)
        self.scroll_timer.setInterval(80)
        self.scroll_offset = 0
        self.scroll_speed = 1
        self.text_content = ""
        self.text_width = 0
        self.is_scrolling = False

    def setText(self, text):
        self.text_content = text
        self.scroll_offset = 0
        self.text_width = self.fontMetrics().horizontalAdvance(text)
        if self.text_width > self.width():
            if not self.is_scrolling:
                self.scroll_timer.start()
                self.is_scrolling = True
        else:
            if self.is_scrolling:
                self.scroll_timer.stop()
                self.is_scrolling = False
        self.update()

    def scroll_text(self):
        self.scroll_offset += self.scroll_speed
        if self.scroll_offset > self.text_width:
            self.scroll_offset = -self.width()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.palette().color(QPalette.Text))
        y_pos = self.height() // 2 + self.fontMetrics().ascent() // 2
        painter.drawText(-self.scroll_offset, y_pos, self.text_content)
        painter.end()