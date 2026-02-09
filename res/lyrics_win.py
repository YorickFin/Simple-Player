import re
import json
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QEvent, QTimer, QPropertyAnimation, QParallelAnimationGroup, QEasingCurve
from PySide6.QtGui import Qt, QFont, QColor, QPainter, QPainterPath, QPen, QBrush
from PySide6.QtWidgets import QGraphicsScene, QGraphicsTextItem, QGraphicsView

from pathlib import Path

from res.ui import desktop_lyrics_ui
from res.qrc import desktop_lyrics_rc  # noqa: F401


class OutlinedTextItem(QGraphicsTextItem):
    def __init__(self, text="", stroke_color=QColor(0, 0, 0), stroke_width=2):
        super().__init__(text)
        self.stroke_color = stroke_color
        self.stroke_width = stroke_width

    def paint(self, painter, option, widget=None):
        painter.save()

        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        doc = self.document()

        for block in doc.toPlainText().split('\n'):
            if not block:
                continue

            path = QPainterPath()
            path.addText(0, 0, self.font(), block)

            rect = self.boundingRect()
            x = (rect.width() - path.boundingRect().width()) / 2
            y = (rect.height() - path.boundingRect().height()) / 2 + path.boundingRect().height()

            painter.translate(x, y)

            pen = QPen(self.stroke_color, self.stroke_width)
            pen.setJoinStyle(Qt.RoundJoin)
            pen.setCapStyle(Qt.RoundCap)

            painter.strokePath(path, pen)
            painter.fillPath(path, QBrush(self.defaultTextColor()))

            painter.translate(-x, -y)
            break

        painter.restore()


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

        self.ui.lockRButton.toggled.connect(self.set_lock)
        self.ui.transparentRButton.toggled.connect(self.set_transparent)

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

        # 窗口锁定配置
        self.move_event = not self.config['lock']
        self.ui.lockRButton.setChecked(self.config['lock'])

        # 透明窗口配置
        self.ui.transparentRButton.setChecked(self.config['transparent'])
        if self.config['transparent']:
            # 背景窗口解除事件过滤器
            self.ui.background.removeEventFilter(self)
            self.ui.lockRButton.hide()
            self.ui.transparentRButton.hide()
            # 设置鼠标事件穿透
            self.setWindowFlags(self.windowFlags() | Qt.WindowTransparentForInput)
            self.show()

        # 窗口位置配置
        if self.config['win_pos']:
            self.move(self.config['win_pos'][0], self.config['win_pos'][1])

        # 字体配置
        font_family = self.config.get('font', '楷体')
        font_size = self.config.get('font_size', 16)
        self.lyric_font = QFont(font_family, font_size)
        self.lyric_font.setStyleStrategy(QFont.PreferAntialias)

        # 字体颜色
        font_color = self.config.get('font_color', '#FFFFFF')
        self.font_color = QColor(font_color)

        # 描边配置
        stroke_color = self.config.get('stroke_color', '#000000')
        stroke_width = self.config.get('stroke_width', 10)
        self.stroke_color = QColor(stroke_color)
        self.stroke_width = stroke_width

        # 歌词位置配置
        self.lyric_pos = self.config.get('lyric_pos', [20, 80, 150, 210])
        self.lyric_scales = self.config.get('lyric_scales', [0.8, 1.0, 0.8, 0.0])
        self.lyric_opacities = self.config.get('lyric_opacities', [0.5, 1.0, 0.5, 0.0])

        # 应用到UI
        self._apply_lyric_config()

    def set_lock(self, checked):
        if checked:
            self.move_event = False
            self.config['lock'] = True
            if self.move_pos:
                self.config['win_pos'] = [self.move_pos.x(), self.move_pos.y()]
        else:
            self.move_event = True
            self.config['lock'] = False

        self._save_config()

    def set_transparent(self, checked):
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

        self._save_config()

    def _apply_lyric_config(self):
        for i, item in enumerate(self.lyric_items):
            item.setFont(self.lyric_font)
            item.setDefaultTextColor(self.font_color)
            item.stroke_color = self.stroke_color
            item.stroke_width = self.stroke_width
            item.setY(self.lyric_pos[i])
            item.setScale(self.lyric_scales[i])
            item.setOpacity(self.lyric_opacities[i])

    def set_font(self, font_family: str):
        self.config['font'] = font_family
        self.lyric_font.setFamily(font_family)
        self._save_config()
        self._apply_lyric_config()

    def set_font_size(self, font_size: int):
        self.config['font_size'] = font_size
        self.lyric_font.setPointSize(font_size)
        self._save_config()
        self._apply_lyric_config()

    def set_font_color(self, font_color: str):
        self.config['font_color'] = font_color
        self.font_color = QColor(font_color)
        self._save_config()
        self._apply_lyric_config()

    def set_stroke_color(self, stroke_color: str):
        self.config['stroke_color'] = stroke_color
        self.stroke_color = QColor(stroke_color)
        self._save_config()
        self._apply_lyric_config()

    def set_stroke_width(self, stroke_width: int):
        self.config['stroke_width'] = stroke_width
        self.stroke_width = stroke_width
        self._save_config()
        self._apply_lyric_config()

    def _save_config(self):
        with open(r'res\config\desktop_lyrics.json', 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)

    def set_lyric_pos(self, lyric_pos: list):
        self.config['lyric_pos'] = lyric_pos
        self.lyric_pos = lyric_pos
        self._save_config()
        self._apply_lyric_config()

    def set_lyric_scales(self, lyric_scales: list):
        self.config['lyric_scales'] = lyric_scales
        self.lyric_scales = lyric_scales
        self._save_config()
        self._apply_lyric_config()

    def set_lyric_opacities(self, lyric_opacities: list):
        self.config['lyric_opacities'] = lyric_opacities
        self.lyric_opacities = lyric_opacities
        self._save_config()
        self._apply_lyric_config()

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
        if self.config.get('win_pos') and self.config.get('size'):
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

        # 设置视图为固定大小，避免滚动
        view_width = int(self.width()) + 160
        view_height = int(self.height())
        print(view_width, view_height)
        self.ui.graphicsView.setFixedSize(view_width, view_height)
        self.ui.graphicsView.setSceneRect(0, 0, view_width, view_height)

        # 创建场景
        self.scene = QGraphicsScene(0, 0, view_width, view_height, self)
        self.scene.setBackgroundBrush(Qt.transparent)
        self.ui.graphicsView.setScene(self.scene)

        # 设置视图不更新背景，减少重绘
        self.ui.graphicsView.setViewportUpdateMode(QGraphicsView.MinimalViewportUpdate)
        self.ui.graphicsView.setOptimizationFlag(QGraphicsView.DontAdjustForAntialiasing, True)
        self.ui.graphicsView.setRenderHint(QPainter.Antialiasing, False)
        self.ui.graphicsView.setRenderHint(QPainter.TextAntialiasing, True)
        self.ui.graphicsView.setRenderHint(QPainter.SmoothPixmapTransform, False)

        for i in range(4):
            item = OutlinedTextItem("", stroke_color=QColor(0, 0, 0), stroke_width=10)
            item.setTextWidth(view_width)
            item.setFlag(QGraphicsTextItem.ItemIgnoresTransformations, False)
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
            item.setHtml("")
            item.setY(self.lyric_pos[i])
            item.setScale(self.lyric_scales[i])
            item.setOpacity(self.lyric_opacities[i])

    def _format_text_as_html(self, text):
        """将文本格式化为HTML，实现自动换行和居中"""
        if not text:
            return ""

        # 将换行符转换为HTML换行
        text = text.replace('\n', '<br>')

        # 创建HTML内容，使用div居中
        html = f"""
        <div style="
            text-align: center;
            font-family: '{self.lyric_font.family()}';
            font-size: {self.lyric_font.pointSize()}pt;
            color: white;
            line-height: 1.2;
        ">
            {text}
        </div>
        """
        return html

    def center_item(self, item):
        """使用HTML居中文本，无需计算宽度"""
        text = item.toPlainText()
        if not text:
            return

        # 设置HTML格式的文本，自动居中
        html_text = self._format_text_as_html(text)
        item.setHtml(html_text)

        # 设置文本宽度为视图宽度，使文本自动换行
        item.setTextWidth(self.scene.width())

    def create_animation(self, item, start_y, end_y, start_scale, end_scale,
                          start_opacity, end_opacity, duration):
        start_x = 0
        end_x = 0

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
                end_y = self.lyric_pos[i - 1]
                end_scale = self.lyric_scales[i - 1]
                end_opacity = self.lyric_opacities[i - 1]

            anims = self.create_animation(
                item,
                self.lyric_pos[i], end_y,
                self.lyric_scales[i], end_scale,
                self.lyric_opacities[i], end_opacity,
                duration
            )
            self.animation_group.addAnimation(anims[0])
            self.animation_group.addAnimation(anims[1])
            self.animation_group.addAnimation(anims[2])
            self.animation_group.addAnimation(anims[3])

            if self.lyric_scales[i] > 0:
                compensated_width = self.scene.width() / self.lyric_scales[i]
                item.setTextWidth(compensated_width)

            anims[2].valueChanged.connect(
                lambda val, item=item, start_scale=self.lyric_scales[i], end_scale=end_scale:
                    self._update_text_width_during_animation(item, val, start_scale, end_scale)
            )

        self.animation_group.finished.connect(self._on_animation_finished)
        self.animation_group.start()

    def _update_text_width_during_animation(self, item, current_scale, start_scale, end_scale):
        if current_scale > 0:
            compensated_width = self.scene.width() / current_scale
            item.setTextWidth(compensated_width)

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

            if text:
                html_text = self._format_text_as_html(text)
                item.setHtml(html_text)
            else:
                item.setHtml("")

            item.setY(self.lyric_pos[i])
            item.setScale(self.lyric_scales[i])
            item.setOpacity(self.lyric_opacities[i])

            if self.lyric_scales[i] > 0:
                compensated_width = self.scene.width() / self.lyric_scales[i]
                item.setTextWidth(compensated_width)