import re
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsTextItem
from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QParallelAnimationGroup
from PySide6.QtCore import QEasingCurve
from PySide6.QtGui import QFont, QColor

from pathlib import Path


class LyricWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lyrics = []
        self.current_index = 0
        self.lyric_items = []
        self.animation_group = None
        self.animation_running = False
        self.lyric_offset = 0

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("歌词滚动")
        self.setFixedSize(1200, 200)

        self.view = QGraphicsView(self)
        self.view.setFixedSize(1200, 200)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setFrameShape(QGraphicsView.NoFrame)
        self.view.setBackgroundBrush(QColor("#1a1a1a"))

        self.scene = QGraphicsScene(0, 0, 500, 200, self)
        self.view.setScene(self.scene)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.view)
        self.setLayout(layout)

        self.positions = [30, 80, 140, 190]             # 歌词位置
        self.scales = [0.7, 1.0, 0.7, 0.0]            # 缩放比例
        self.opacities = [0.6, 1.0, 0.6, 0.0]           # 透明度

        for i in range(4):
            item = QGraphicsTextItem("")
            item.setFont(QFont("楷体", 16))
            item.setDefaultTextColor(QColor("white"))
            item.setPos(0, self.positions[i])
            item.setOpacity(self.opacities[i])
            item.setScale(self.scales[i])
            self.scene.addItem(item)
            self.lyric_items.append(item)

    def load_lrc(self, lrc_source):
        self.lyrics.clear()
        self.current_index = 0
        self.animation_running = False

        lines = self._read_lrc_content(lrc_source)
        self._parse_lrc_lines(lines)

        QTimer.singleShot(0, self._reset_and_update_display)

    def _read_lrc_content(self, lrc_source):
        if isinstance(lrc_source, Path):
            lrc_source = str(lrc_source)

        if not isinstance(lrc_source, str):
            return []

        if '\n' in lrc_source or '\r' in lrc_source:
            return lrc_source.splitlines()

        # 检查是否是歌词内容（以[开头并包含]）
        if lrc_source.startswith('[') and ']' in lrc_source:
            return [lrc_source]

        try:
            with open(lrc_source, 'r', encoding='utf-8') as f:
                return f.readlines()
        except (FileNotFoundError, OSError) as e:
            print(f"无法打开歌词文件: {lrc_source}, 错误: {e}")
            return []

    def _parse_lrc_lines(self, lines):
        # 支持两种时间戳格式：[mm:ss.ms] 和 [hh:mm:ss]
        pattern1 = re.compile(r'\[(\d{2}):(\d{2})\.(\d{2,3})\](.*)$')  # [mm:ss.ms]
        pattern2 = re.compile(r'\[(\d{2}):(\d{2}):(\d{2})\](.*)$')    # [hh:mm:ss]

        lyric_dict = {}

        for line in lines:
            line = line.strip()

            # 尝试匹配第一种格式 [mm:ss.ms]
            match = pattern1.match(line)
            if match:
                minutes = int(match.group(1))
                seconds = int(match.group(2))
                milliseconds_str = match.group(3)
                text = match.group(4).strip()

                if not text:
                    continue

                milliseconds = int(milliseconds_str)
                if len(milliseconds_str) == 2:
                    milliseconds *= 10

                timestamp = minutes * 60 * 1000 + seconds * 1000 + milliseconds
                # 调整精度为200ms
                timestamp = (timestamp // 200) * 200
                if timestamp in lyric_dict:
                    lyric_dict[timestamp] += '\n' + text
                else:
                    lyric_dict[timestamp] = text
                continue

            # 尝试匹配第二种格式 [hh:mm:ss]
            match = pattern2.match(line)
            if match:
                hours = int(match.group(1))
                minutes = int(match.group(2))
                seconds = int(match.group(3))
                text = match.group(4).strip()

                if not text:
                    continue

                timestamp = hours * 3600 * 1000 + minutes * 60 * 1000 + seconds * 1000
                # 调整精度为200ms
                timestamp = (timestamp // 200) * 200
                if timestamp in lyric_dict:
                    lyric_dict[timestamp] += '\n' + text
                else:
                    lyric_dict[timestamp] = text
                continue

        # 将字典转换为排序后的列表
        self.lyrics = sorted(lyric_dict.items(), key=lambda x: x[0])

    def _reset_and_update_display(self):
        self._reset_ui_state()
        self._update_display()

    def _reset_ui_state(self):
        if self.animation_group:
            self.animation_group.stop()
            self.animation_group = None
        self.animation_running = False

        for i, item in enumerate(self.lyric_items):
            item.setPlainText("")
            item.setY(self.positions[i])
            item.setScale(self.scales[i])
            item.setOpacity(self.opacities[i])

    def center_item(self, item):
        # 计算多行文本的宽度并处理两行对齐
        text = item.toPlainText()
        if '\n' in text:
            # 分割文本为多行
            lines = text.split('\n')
            if len(lines) >= 2:
                # 保存原始完整文本
                original_text = item.toPlainText()
                # 计算第一行的宽度
                item.setPlainText(lines[0])
                first_line_width = item.boundingRect().width()
                # 计算第二行的宽度
                item.setPlainText(lines[1])
                second_line_width = item.boundingRect().width()
                # 计算一个空格的宽度
                item.setPlainText(' ')
                space_width = item.boundingRect().width()
                # 比较两行宽度，在较窄的一行前面添加空格
                if space_width > 0:
                    if first_line_width < second_line_width:
                        # 第一行较窄，在第一行前面添加空格
                        spaces_needed = int((second_line_width - first_line_width) / (space_width+1))
                        lines[0] = ' ' * spaces_needed + lines[0]
                    elif second_line_width < first_line_width:
                        # 第二行较窄，在第二行前面添加空格
                        spaces_needed = int((first_line_width - second_line_width) / (space_width+1))
                        lines[1] = ' ' * spaces_needed + lines[1]
                    # 更新文本
                    new_text = '\n'.join(lines)
                    item.setPlainText(new_text)
                else:
                    # 如果空格宽度计算失败，保持原始文本不变
                    item.setPlainText(original_text)
                # 计算更新后文本的最大宽度
                max_width = 0
                # 使用更新后的文本
                current_text = item.toPlainText()
                for line in current_text.split('\n'):
                    item.setPlainText(line)
                    line_width = item.boundingRect().width()
                    if line_width > max_width:
                        max_width = line_width
                # 恢复更新后的完整文本
                item.setPlainText(current_text)
                text_width = max_width * item.scale()
            else:
                # 只有一行文本，直接计算宽度
                text_width = item.boundingRect().width() * item.scale()
        else:
            # 单行文本，直接计算宽度
            text_width = item.boundingRect().width() * item.scale()

        x = (500 - text_width) / 2
        item.setX(x)

    def create_animation(self, item, start_y, end_y, start_scale, end_scale,
                          start_opacity, end_opacity, duration):
        # 计算多行文本的最大宽度
        text = item.toPlainText()
        if '\n' in text:
            # 分割文本为多行
            lines = text.split('\n')
            max_width = 0
            # 临时设置单行文本以计算每一行的宽度
            original_text = item.toPlainText()
            for line in lines:
                item.setPlainText(line)
                line_width = item.boundingRect().width()
                if line_width > max_width:
                    max_width = line_width
            # 恢复原始文本
            item.setPlainText(original_text)
            text_width = max_width
        else:
            # 单行文本，直接计算宽度
            text_width = item.boundingRect().width()

        start_x = (500 - text_width * start_scale) / 2
        end_x = (500 - text_width * end_scale) / 2

        x_anim = QPropertyAnimation(item, b"x")
        x_anim.setStartValue(start_x)
        x_anim.setEndValue(end_x)
        x_anim.setDuration(duration)
        x_anim.setEasingCurve(QEasingCurve.OutCubic)

        y_anim = QPropertyAnimation(item, b"y")
        y_anim.setStartValue(start_y)
        y_anim.setEndValue(end_y)
        y_anim.setDuration(duration)
        y_anim.setEasingCurve(QEasingCurve.OutCubic)

        scale_anim = QPropertyAnimation(item, b"scale")
        scale_anim.setStartValue(start_scale)
        scale_anim.setEndValue(end_scale)
        scale_anim.setDuration(duration)
        scale_anim.setEasingCurve(QEasingCurve.OutCubic)

        opacity_anim = QPropertyAnimation(item, b"opacity")
        opacity_anim.setStartValue(start_opacity)
        opacity_anim.setEndValue(end_opacity)
        opacity_anim.setDuration(duration)
        opacity_anim.setEasingCurve(QEasingCurve.OutCubic)

        return x_anim, y_anim, scale_anim, opacity_anim

    def set_lyric_offset(self, offset_seconds: float):
        self.lyric_offset = int(offset_seconds * 1000)

    def get_lyric_offset(self) -> float:
        return self.lyric_offset / 1000

    def sync_to_time(self, play_time_ms):
        if not self.lyrics:
            return

        if self.animation_running:
            return

        adjusted_time = play_time_ms + self.lyric_offset
        new_index = self._find_lyric_index(adjusted_time)
        if new_index != self.current_index:
            self.current_index = new_index
            self._animate_scroll()
        else:
            # 即使索引不变，也更新显示，确保初始歌词正确显示
            self._update_display()

    def _find_lyric_index(self, play_time_ms):
        for i, (timestamp, _) in enumerate(self.lyrics):
            if timestamp > play_time_ms:
                return max(0, i - 1)
        return len(self.lyrics) - 1

    def _animate_scroll(self):
        if self.animation_group:
            self.animation_group.stop()

        self.animation_group = QParallelAnimationGroup(self)
        duration = 500
        self.animation_running = True

        for i, item in enumerate(self.lyric_items):
            if i == 0:
                end_y = -10
                end_scale = 0.0
                end_opacity = 0.0
            else:
                end_y = self.positions[i - 1]
                end_scale = self.scales[i - 1]
                end_opacity = self.opacities[i - 1]

            anims = self.create_animation(
                item,
                self.positions[i], end_y,
                self.scales[i], end_scale,
                self.opacities[i], end_opacity,
                duration
            )
            self.animation_group.addAnimation(anims[0])
            self.animation_group.addAnimation(anims[1])
            self.animation_group.addAnimation(anims[2])
            self.animation_group.addAnimation(anims[3])

        self.animation_group.finished.connect(self._on_animation_finished)
        self.animation_group.start()

    def _on_animation_finished(self):
        self.animation_running = False
        self._update_display()

    def _update_display(self):
        texts = []
        for offset in [-1, 0, 1, 2]:
            idx = self.current_index + offset
            if 0 <= idx < len(self.lyrics):
                texts.append(self.lyrics[idx][1])
            else:
                texts.append("")

        for i, item in enumerate(self.lyric_items):
            # 使用plain text格式，通过计算宽度确保文本居中
            text = texts[i]
            item.setPlainText(text)
            item.setY(self.positions[i])
            item.setScale(self.scales[i])
            item.setOpacity(self.opacities[i])
            self.center_item(item)
