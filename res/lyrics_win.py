import re
import json
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QEvent, QTimer, QPropertyAnimation, QParallelAnimationGroup, QEasingCurve
from PySide6.QtGui import Qt, QFont, QColor
from PySide6.QtWidgets import QGraphicsScene, QGraphicsTextItem, QGraphicsView

from pathlib import Path

from res.ui import desktop_lyrics_ui
from res.qrc import desktop_lyrics_rc  # noqa: F401


class LyricsWindow(QWidget):

    def __init__(self, signal_manager, logger, parent=None):
        super(LyricsWindow, self).__init__(parent)
        self.signal_manager = signal_manager
        self.logger = logger
        self.ui = desktop_lyrics_ui.Ui_Form()
        self.ui.setupUi(self)
        # 设置窗口为无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        #将界面属性设置为半透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 不可编辑置顶
        self.setWindowFlags(self.windowFlags() | Qt.WindowDoesNotAcceptFocus | Qt.WindowStaysOnTopHint)

        self.ui.lockRButton.toggled.connect(self.lock_control)
        self.ui.transparentRButton.toggled.connect(self.transparent_control)

        # 初始化歌词相关属性
        self.init_lyric_attributes()
        self.init_lyric_ui()

        # 初始化窗口事件
        self.init_window_event()
        self.init_config()
        self.windowAdaptation()
        self.textAdaptation(r'res\qss\desktop_lyrics.qss', self)

    def init_config(self):
        with open(r'res\config\desktop_lyrics.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)

        # 应用配置
        self.move_event = not self.config['lock']
        self.ui.lockRButton.setChecked(self.config['lock'])
        self.ui.transparentRButton.setChecked(self.config['transparent'])
        if self.config['transparent']:
            # 背景窗口解除事件过滤器
            self.ui.background.removeEventFilter(self)
            self.ui.lockRButton.hide()
            self.ui.transparentRButton.hide()
            # 设置鼠标事件穿透
            self.setWindowFlags(self.windowFlags() | Qt.WindowTransparentForInput)
            self.show()
        if self.config['position']:
            self.move(self.config['position'][0], self.config['position'][1])

    def lock_control(self, checked):
        if checked:
            self.move_event = False
            self.config['lock'] = True
            if self.move_pos:
                self.config['position'] = [self.move_pos.x(), self.move_pos.y()]
        else:
            self.move_event = True
            self.config['lock'] = False

        with open(r'res\config\desktop_lyrics.json', 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)

    def transparent_control(self, checked):
        if checked:
            self.ui.background.setStyleSheet(
                """
                QFrame#background
                {
                    background-color: transparent;
                }
                """
            )
            self.config['transparent'] = True
            # 背景窗口解除事件过滤器
            self.ui.background.removeEventFilter(self)
            self.ui.lockRButton.hide()
            self.ui.transparentRButton.hide()
            # 设置鼠标事件穿透
            self.setWindowFlags(self.windowFlags() | Qt.WindowTransparentForInput)
            self.show()
        else:
            self.ui.background.setStyleSheet(
                """
                QFrame#background
                {
                    background-color: #1F2430;
                }
                """
            )
            self.config['transparent'] = False
            # 移除鼠标穿透
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowTransparentForInput)
            self.show()

        with open(r'res\config\desktop_lyrics.json', 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)

# ########################################## window_event ##########################################

    def init_window_event(self):
        self.move_pos = None
        # 扳机初始化
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

        self.desktop_size = [QApplication.instance().screens()[0].size().width(), QApplication.instance().screens()[0].size().height()]

        # 开启鼠标跟踪后, 鼠标离开窗口或进入窗口会触发 mouseMoveEvent 事件
        self.setMouseTracking(True)

        self.ui.background.installEventFilter(self)  # 背景窗口绑定事件过滤器

    def eventFilter(self, obj, event):
        if obj == self.ui.background:
            if event.type() == QEvent.Enter:    # 鼠标进入背景窗口
                self.ui.lockRButton.show()
                self.ui.transparentRButton.show()
            elif event.type() == QEvent.Leave:    # 鼠标离开背景窗口
                self.ui.lockRButton.hide()
                self.ui.transparentRButton.hide()
        return super(LyricsWindow, self).eventFilter(obj, event)

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton and self.move_event:
            # 鼠标在窗口中的位置
            self.cursor_win_pos = event.globalPosition() - self.pos()
            # 窗口宽高
            self.win_width = self.ui.background.size().width()
            self.win_height = self.ui.background.size().height()

            # 移动事件
            if self.cursor_win_pos.x() < self.win_width and self.cursor_win_pos.y() < self.win_height:
                self._move_drag = True
            event.accept()

    def mouseMoveEvent(self, event):

        if self.move_event:
            # 仅在左键按下时触发移动、拉伸事件
            if event.buttons() == Qt.LeftButton:
                # 移动事件
                if self._move_drag:
                    self.move_pos = event.globalPosition() - self.cursor_win_pos
                    self.move(self.move_pos.x(), self.move_pos.y())
            event.accept()

    def mouseReleaseEvent(self, event):
        self._move_drag = False
        event.accept()

    def windowAdaptation(self):
        """界面大小自适应"""
        if self.config.get('position') and self.config.get('size'):
            return

        screen_width, screen_height = self.desktop_size

        scale_factor = (screen_width - 1920) * (0.2 / 640)
        scale_w = 1.7 + scale_factor
        scale_h = 5 + scale_factor

        win_width = (screen_width / scale_w) + 18
        win_height = (screen_height / scale_h)

        self.resize(win_width, win_height)

    def textAdaptation(self, file_path, ui_object):
        """文字大小自适应"""
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

# ########################################## lyric_widget 移植 ##########################################

    def init_lyric_attributes(self):
        self.lyrics = []
        self.current_index = 0
        self.lyric_items = []
        self.animation_group = None
        self.animation_running = False
        self.lyric_offset = 0

    def init_lyric_ui(self):
        self.ui.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.graphicsView.setFrameShape(QGraphicsView.NoFrame)

        self.scene = QGraphicsScene(0, 0, 500, 200, self)
        self.ui.graphicsView.setScene(self.scene)

        self.positions = [30, 80, 140, 190]
        self.scales = [0.7, 1.0, 0.7, 0.0]
        self.opacities = [0.6, 1.0, 0.6, 0.0]

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

        if lrc_source.startswith('[') and ']' in lrc_source:
            return [lrc_source]

        try:
            with open(lrc_source, 'r', encoding='utf-8') as f:
                return f.readlines()
        except (FileNotFoundError, OSError) as e:
            print(f"无法打开歌词文件: {lrc_source}, 错误: {e}")
            return []

    def _parse_lrc_lines(self, lines):
        pattern1 = re.compile(r'\[(\d{2}):(\d{2})\.(\d{2,3})\](.*)$')
        pattern2 = re.compile(r'\[(\d{2}):(\d{2}):(\d{2})\](.*)$')

        lyric_dict = {}

        for line in lines:
            line = line.strip()

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
                timestamp = (timestamp // 200) * 200
                if timestamp in lyric_dict:
                    lyric_dict[timestamp] += '\n' + text
                else:
                    lyric_dict[timestamp] = text
                continue

            match = pattern2.match(line)
            if match:
                hours = int(match.group(1))
                minutes = int(match.group(2))
                seconds = int(match.group(3))
                text = match.group(4).strip()

                if not text:
                    continue

                timestamp = hours * 3600 * 1000 + minutes * 60 * 1000 + seconds * 1000
                timestamp = (timestamp // 200) * 200
                if timestamp in lyric_dict:
                    lyric_dict[timestamp] += '\n' + text
                else:
                    lyric_dict[timestamp] = text
                continue

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
        text = item.toPlainText()
        if '\n' in text:
            lines = text.split('\n')
            if len(lines) >= 2:
                original_text = item.toPlainText()
                item.setPlainText(lines[0])
                first_line_width = item.boundingRect().width()
                item.setPlainText(lines[1])
                second_line_width = item.boundingRect().width()
                item.setPlainText(' ')
                space_width = item.boundingRect().width()
                if space_width > 0:
                    if first_line_width < second_line_width:
                        spaces_needed = int((second_line_width - first_line_width) / (space_width+1))
                        lines[0] = ' ' * spaces_needed + lines[0]
                    elif second_line_width < first_line_width:
                        spaces_needed = int((first_line_width - second_line_width) / (space_width+1))
                        lines[1] = ' ' * spaces_needed + lines[1]
                    new_text = '\n'.join(lines)
                    item.setPlainText(new_text)
                else:
                    item.setPlainText(original_text)
                max_width = 0
                current_text = item.toPlainText()
                for line in current_text.split('\n'):
                    item.setPlainText(line)
                    line_width = item.boundingRect().width()
                    if line_width > max_width:
                        max_width = line_width
                item.setPlainText(current_text)
                text_width = max_width * item.scale()
            else:
                text_width = item.boundingRect().width() * item.scale()
        else:
            text_width = item.boundingRect().width() * item.scale()

        x = (500 - text_width) / 2
        item.setX(x)

    def create_animation(self, item, start_y, end_y, start_scale, end_scale,
                          start_opacity, end_opacity, duration):
        text = item.toPlainText()
        if '\n' in text:
            lines = text.split('\n')
            max_width = 0
            original_text = item.toPlainText()
            for line in lines:
                item.setPlainText(line)
                line_width = item.boundingRect().width()
                if line_width > max_width:
                    max_width = line_width
            item.setPlainText(original_text)
            text_width = max_width
        else:
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
            text = texts[i]
            item.setPlainText(text)
            item.setY(self.positions[i])
            item.setScale(self.scales[i])
            item.setOpacity(self.opacities[i])
            self.center_item(item)

