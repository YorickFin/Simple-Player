from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPainter, QPalette

class MarqueeLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(200)
        self.scroll_timer = QTimer(self)
        self.scroll_timer.timeout.connect(self.scroll_text)
        self.scroll_offset = 0
        self.scroll_speed = 1
        self.text_content = ""

    def setText(self, text):
        self.text_content = text
        self.scroll_offset = 0
        font_metrics = self.fontMetrics()
        text_width = font_metrics.horizontalAdvance(text)
        if text_width > self.width():
            self.scroll_timer.start(50)
        else:
            self.scroll_timer.stop()
        self.update()

    def scroll_text(self):
        font_metrics = self.fontMetrics()
        text_width = font_metrics.horizontalAdvance(self.text_content)
        self.scroll_offset += self.scroll_speed
        if self.scroll_offset > text_width:
            self.scroll_offset = -self.width()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.palette().color(QPalette.Text))
        painter.drawText(
            -self.scroll_offset,
            self.height() // 2 + self.fontMetrics().ascent() // 2,
            self.text_content
        )