
import json
import time
from PySide6.QtWidgets import (QTableView, QHeaderView, QFileDialog,
                            QMenu, QSlider, QLabel, QWidgetAction)
from PySide6.QtCore import QTimer, QStandardPaths, QPoint
from PySide6.QtGui import QAction, QEnterEvent, QPixmap, QIcon, QCursor, Qt
from pathlib import Path
from threading import Thread

from res.ui import main_ui
from res.qrc import main_rc  # noqa: F401
from res.tablemodel import TableModel, RoundedImageDelegate, create_rounded_pixmap
from res.win_super import WindowSuper
from res.marqueelabel import MarqueeLabel
from src.audio_extract import AudioExtractor

class MainWindow(WindowSuper):

    def __init__(self, signal_manager, logger, parent=None):
        super(MainWindow, self).__init__(parent)
        self.signal_manager = signal_manager
        self.logger = logger
        self.audio_extractor = AudioExtractor()

        self.ui = main_ui.Ui_Form()
        self.ui.setupUi(self)
        self.init_ui()
        self.init_window_event()

        self.replace_music_name_label()
        self.init_config()

        self.ui.background.setStyleSheet("QFrame#background{border-image: url('res/background/bgd.jpg');}")
        default_pixmap = QPixmap(r'res\img\music.png').scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.musicLogoPButton.setIcon(QIcon(create_rounded_pixmap(default_pixmap, radius=18)))

        self.windowAdaptation()
        self.textAdaptation(r'res\qss\main.qss', self)

        self.play_num = 0
        self.data = []
        self.music_dict = {}
        self.slider_pressed = False
        self.last_activity_time = time.time()  # 上次活动时间戳

        # tableview
        self.init_tableview()

        # menuListWidget
        self.ui.subTabWidget.setCurrentIndex(3)
        self.ui.menuListWidget.itemClicked.connect(lambda item: self.on_menu_change(self.ui.menuListWidget.currentRow()))

        # folderListWidget
        self.default_option_management()
        self.load_folder_config()
        self.ui.folderListWidget.customContextMenuRequested.connect(self.folder_list_menu)
        self.ui.folderListWidget.itemClicked.connect(lambda item: self.fill_tableview(item.text()))

        # playModeRButton
        self.load_playMode_imga()
        self.ui.playModeRButton1.clicked.connect(self.playMode)
        # self.ui.playModeRButton2.clicked.connect(self.playMode)

        # volumeControlRButton
        self.volume_menu(self.config['volume'])
        self.on_volume_changed(self.config['volume'])
        self.ui.volumeControlRButton1.clicked.connect(lambda: self.show_volume_slider(self.ui.volumeControlRButton1))
        # self.ui.volumeControlRButton2.clicked.connect(lambda: self.show_volume_slider(self.ui.volumeControlRButton2))

        # play_control
        self.ui.playRButton1.toggled.connect(self.play_control)
        # self.ui.playRButton2.toggled.connect(self.play_control)
        self.ui.pgupRButton1.clicked.connect(self.pgup_music)
        # self.ui.pgupRButton2.clicked.connect(self.pgup_music)
        self.ui.pgdnRButton1.clicked.connect(self.pgdn_music)
        # self.ui.pgdnRButton2.clicked.connect(self.pgdn_music)
        self.ui.playSlider1.sliderPressed.connect(self.on_slider_pressed)
        self.ui.playSlider1.sliderReleased.connect(self.on_slider_released)
        # self.ui.playSlider2.sliderReleased.connect(lambda: self.seek(self.ui.playSlider2.value()))


# ########################################## replace_music_name_label ##########################################

    def replace_music_name_label(self):
        old_label = self.ui.musicNameLabel
        parent = old_label.parent()
        layout = self.ui.horizontalLayout_4

        new_label = MarqueeLabel(parent)
        new_label.setObjectName("musicNameLabel")
        new_label.setMinimumSize(150, 26)
        new_label.setMaximumSize(150, 16777215)

        index = layout.indexOf(old_label)
        layout.removeWidget(old_label)
        old_label.deleteLater()

        layout.insertWidget(index, new_label)
        self.ui.musicNameLabel = new_label

# ########################################## init_config ##########################################

    def init_config(self):
        with open('res/config/config.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        with open('res/config/music_config.json', 'r', encoding='utf-8') as f:
            self.music_config = json.load(f)

        with open('res/qss/loop_one_song.qss', 'r', encoding='utf-8') as f:
            self.loop_one_song_qss = f.read()
        with open('res/qss/ordered_play.qss', 'r', encoding='utf-8') as f:
            self.ordered_play_qss = f.read()
        with open('res/qss/random_play.qss', 'r', encoding='utf-8') as f:
            self.random_play_qss = f.read()

        for folder_path in self.config['folder_list']:
            Thread(target=self.get_music_files, args=(folder_path,)).start()

# ########################################## menuListWidget ##########################################

    def on_menu_change(self, index):
        self.ui.subTabWidget.setCurrentIndex(index)
        if index == 0:
            self.ui.subTabWidget.setCurrentIndex(3)
            self.load_all_music()
            self.ui.subTabWidget.setCurrentIndex(index)

    def load_all_music(self):
        self.data.clear()
        self.music_dict.clear()
        if len(self.music_config) != 0:
            self.data.clear()
            for music_files in self.music_config:
                for music_file in self.music_config[music_files]:
                    music_file = Path(music_file)
                    audio_info = self.audio_extractor.extract(music_file, extract_cover=True)

                    file_stem = music_file.stem
                    if audio_info.has_cover:
                        cover_data = audio_info.cover_data
                    else:
                        cover_data = r'res\img\music.png'
                    self.music_dict[file_stem] = str(music_file)
                    self.data.append([cover_data, file_stem, self.audio_extractor.format_duration(audio_info.duration)])

            if hasattr(self, 'table_model') and self.table_model:
                self.table_model.update_data(self.data)
            else:
                self.table_model = TableModel(self.data)
                self.table_view = self.ui.tableView
                self.table_view.setModel(self.table_model)
                self.table_view.selectionModel().currentChanged.connect(self.on_play)

            # 临时阻止 selectionModel 的信号，避免误触发播放
            self.table_view.selectionModel().blockSignals(True)
            self.ui.subTabWidget.setCurrentIndex(0)
            self.table_view.selectionModel().blockSignals(False)

            QTimer.singleShot(0, self.resize_table_view)

# ########################################## folderListWidget ##########################################

    def default_option_management(self):
        # 获取所有项对象
        items = [self.ui.folderListWidget.item(i) for i in range(self.ui.folderListWidget.count())]
        if len(items) > 1:  # 有其它项时删除默认项
            for item in items:
                text = item.text()
                if text == '鼠标右键以添加或删除文件夹':
                    taken_item = self.ui.folderListWidget.takeItem(self.ui.folderListWidget.row(item))
                    del taken_item

        elif len(items) == 0:   # 没有项时添加默认项
            self.ui.folderListWidget.addItem('鼠标右键以添加或删除文件夹')

    def load_folder_config(self):
        for folder_path in self.config['folder_list']:
            self.ui.folderListWidget.addItem(folder_path)
        self.default_option_management()

    def folder_list_menu(self, position):
        self.folder_list_Qmenu = QMenu(self)
        self.add_folder_action = QAction('添加文件夹', self)
        self.remove_folder_action = QAction('删除文件夹', self)

        if self.ui.folderListWidget.itemAt(position):
            self.folder_list_Qmenu.addAction(self.add_folder_action)
            self.folder_list_Qmenu.addAction(self.remove_folder_action)

            self.add_folder_action.triggered.connect(self.add_folder)
            self.remove_folder_action.triggered.connect(lambda: self.remove_folder(self.ui.folderListWidget.currentItem().text()))

            self.folder_list_Qmenu.exec(QPoint(QCursor.pos().x() + 8, QCursor.pos().y() - 5))
        else:
            self.folder_list_Qmenu.addAction(self.add_folder_action)
            self.add_folder_action.triggered.connect(self.add_folder)
            self.folder_list_Qmenu.exec(QPoint(QCursor.pos().x() + 8, QCursor.pos().y() - 5))

    def add_folder(self):
        if self.config['default_open_folder']:
            open_folder = self.config['default_open_folder']
        else:
            open_folder = QStandardPaths.writableLocation(QStandardPaths.MusicLocation)
        options = QFileDialog.Options(0)
        options |= QFileDialog.ReadOnly
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹", open_folder, options=options)
        if folder_path:
            folder_path = Path(folder_path)
            if str(folder_path) not in self.config['folder_list']:
                self.ui.folderListWidget.addItem(str(folder_path))
                self.config['folder_list'].append(str(folder_path))
            self.config['default_open_folder'] = str(folder_path.parent)
            with open('res/config/config.json', 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=4)
        Thread(target=self.get_music_files, args=(folder_path,)).start()
        self.default_option_management()

    def remove_folder(self, folder_path: str):
        taken_item = self.ui.folderListWidget.takeItem(self.ui.folderListWidget.row(self.ui.folderListWidget.findItems(folder_path, Qt.MatchExactly)[0]))
        del taken_item
        if folder_path in self.config['folder_list']:
            self.config['folder_list'].remove(folder_path)
            self.music_config.pop(folder_path)
            with open('res/config/config.json', 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=4)
            with open('res/config/music_config.json', 'w', encoding='utf-8') as f:
                json.dump(self.music_config, f, ensure_ascii=False, indent=4)
        self.default_option_management()

    def get_music_files(self, path):
        path = Path(path)
        music_files = list(path.glob('*.mp3')) + \
                      list(path.glob('*.wav')) + \
                      list(path.glob('*.flac'))
        self.music_config[str(path)] = [str(music_file) for music_file in music_files]
        with open('res/config/music_config.json', 'w', encoding='utf-8') as f:
            json.dump(self.music_config, f, ensure_ascii=False, indent=4)

    def fill_tableview(self, item):
        self.data.clear()
        self.music_dict.clear()
        music_files = self.music_config[item]
        for music_file in music_files:
            music_file = Path(music_file)
            audio_info = self.audio_extractor.extract(music_file, extract_cover=True)

            file_stem = music_file.stem
            if audio_info.has_cover:
                cover_data = audio_info.cover_data
            else:
                cover_data = r'res\img\music.png'
            self.music_dict[file_stem] = str(music_file)
            self.data.append([cover_data, file_stem, self.audio_extractor.format_duration(audio_info.duration)])

        if hasattr(self, 'table_model') and self.table_model:
            self.table_model.update_data(self.data)
        else:
            self.table_model = TableModel(self.data)
            self.table_view = self.ui.tableView
            self.table_view.setModel(self.table_model)
            self.table_view.selectionModel().currentChanged.connect(self.on_play)

        # 临时阻止 selectionModel 的信号，避免误触发播放
        self.table_view.selectionModel().blockSignals(True)
        self.ui.subTabWidget.setCurrentIndex(0)
        self.table_view.selectionModel().blockSignals(False)

        QTimer.singleShot(0, self.resize_table_view)

# ########################################## tableview ##########################################

    def init_tableview(self):
        self.table_view = self.ui.tableView
        # 隐藏表头
        self.table_view.horizontalHeader().setVisible(False)
        self.table_view.verticalHeader().setVisible(False)

        # 禁用网格显示
        self.table_view.setShowGrid(False)

        # 设置选择模式: 选择整行
        self.table_view.setSelectionMode(QTableView.SingleSelection)
        self.table_view.setSelectionBehavior(QTableView.SelectRows)

        # 禁用默认方式列宽调整
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

        # 设置第0列的图片圆角显示
        self.rounded_delegate = RoundedImageDelegate(radius=8)
        self.table_view.setItemDelegateForColumn(0, self.rounded_delegate)

    def resize_table_view(self):
        """调整表格视图"""
        if not self.table_view:
            return

        total_width = self.table_view.viewport().width()
        if total_width <= 0:
            return

        column0_width = int(total_width * 0.1)
        column1_width = int(total_width * 0.8)
        column2_width = total_width - column0_width - column1_width

        # 调整列宽
        self.table_view.setColumnWidth(0, column0_width)
        self.table_view.setColumnWidth(1, column1_width)
        self.table_view.setColumnWidth(2, column2_width)
        # 调整行高
        self.table_view.verticalHeader().setDefaultSectionSize(60)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        QTimer.singleShot(0, self.resize_table_view)

    def on_play(self, current):
        if not self.ui.playRButton1.isChecked():
            self.ui.playRButton1.setChecked(True)

        self.signal_manager.send_signal({'action': 'clear_played_list'})

        signal_info = {
            'action': 'play_music',
            'music_path': self.music_dict[self.table_model._data[current.row()][1]],
            'music_dict': self.music_dict,
            'play_mode': self.config['play_mode'],
        }
        self.signal_manager.send_signal(signal_info)

# ########################################## playModeRButton ##########################################

    def load_playMode_imga(self):
        mode = {
            'ordered_play': self.ordered_play_qss,
            'random_play': self.random_play_qss,
            'loop_one_song': self.loop_one_song_qss,
        }
        self.ui.playModeRButton1.setStyleSheet(mode[self.config['play_mode']])
        # self.ui.playModeRButton2.setStyleSheet(mode[self.config['play_mode']])

    def playMode(self):
        modes = ['ordered_play', 'random_play', 'loop_one_song']
        current_index = modes.index(self.config['play_mode'])
        self.config['play_mode'] = modes[(current_index + 1) % 3]

        self.load_playMode_imga()
        with open('res/config/config.json', 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)
        self.signal_manager.send_signal({'action': 'set_play_mode', 'play_mode': self.config['play_mode']})

# ########################################## volumeControlRButton ##########################################

    def volume_menu(self, volume):
        self.volume_QMenu = QMenu(self)
        self.volume_QMenu.setWindowFlags(self.volume_QMenu.windowFlags() | Qt.FramelessWindowHint)
        self.volume_QMenu.setAttribute(Qt.WA_TranslucentBackground)
        self.volume_QMenu.setStyleSheet("""
            QMenu {
                background-color: rgba(47, 54, 72, 230);
                border-radius: 5px;
                padding: 6px;
                border: 0px solid;
            }
            QMenu::item {
                background-color: rgba(47, 54, 72, 230);
            }
        """)

        self.volume_slider = QSlider(Qt.Vertical)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(volume)
        self.volume_slider.setFixedWidth(26)
        self.volume_slider.valueChanged.connect(self.on_volume_changed)
        self.volume_slider.sliderReleased.connect(self.save_volume)

        slider_action = QWidgetAction(self.volume_QMenu)
        slider_action.setDefaultWidget(self.volume_slider)
        self.volume_QMenu.addAction(slider_action)

        self.volume_label = QLabel(f"{volume}%")
        self.volume_label.setAlignment(Qt.AlignCenter)
        self.volume_label.setFixedWidth(26)
        label_action = QWidgetAction(self.volume_QMenu)
        label_action.setDefaultWidget(self.volume_label)
        self.volume_QMenu.addAction(label_action)

    def show_volume_slider(self, ui):
        """显示音量滑块菜单"""
        # 计算菜单显示位置
        btn_rect = ui.rect()
        global_pos = ui.mapToGlobal(btn_rect.bottomLeft())
        # 显示菜单
        self.volume_QMenu.exec(QPoint(global_pos.x() -8, global_pos.y() - 140))

    def on_volume_changed(self, value):
        """音量改变时的处理"""
        self.config['volume'] = value
        self.volume_label.setText(f"{value}%")
        self.signal_manager.send_signal({'action': 'set_volume', 'volume': value / 100})

    def save_volume(self):
        """保存音量"""
        with open('res/config/config.json', 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)

# ########################################## play_control ##########################################

    def play_control(self, checked: bool):
        if checked:
            self.signal_manager.send_signal({'action': 'play_control', 'info': 'resume'})
        else:
            self.signal_manager.send_signal({'action': 'play_control', 'info': 'pause'})

    def pgup_music(self):
        self.signal_manager.send_signal({'action': 'play_control', 'info': 'pgup'})

    def pgdn_music(self):
        self.signal_manager.send_signal({'action': 'play_control', 'info': 'pgdn'})

    def seek(self, value: int):
        self.signal_manager.send_signal({'action': 'seek', 'info': value})

    def on_slider_pressed(self):
        self.slider_pressed = True

    def on_slider_released(self):
        self.slider_pressed = False
        self.seek(self.ui.playSlider1.value())

# ########################################## window_event ##########################################

    def init_window_event(self):
        # 扳机初始化
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False

        self.double_click_timer = 0.0

        self.ui.winMaxRButton.toggled.connect(self.window_max_min)
        self.ui.winMiniRButton.clicked.connect(lambda: self.showMinimized())
        self.ui.winCloseRButton.clicked.connect(self.close_event)

        # 开启鼠标跟踪后，鼠标离开窗口或进入窗口会触发 mouseMoveEvent 事件
        self.setMouseTracking(True)

        self.ui.background.installEventFilter(self)  # 背景窗口绑定事件过滤器

    def eventFilter(self, obj, event):
        # 鼠标进入其它控件后还原为标准鼠标样式
        if isinstance(event, QEnterEvent):
            self.setCursor(QCursor(Qt.ArrowCursor))
        return super(MainWindow, self).eventFilter(obj, event)

    def mousePressEvent(self, event):
        # 更新活动时间戳
        self.update_activity_time()

        self.double_click_event()
        if event.button() == Qt.LeftButton and self.ui.winMaxRButton.isChecked() is False:
            # 鼠标在窗口中的位置
            self.cursor_win_pos = event.globalPosition() - self.pos()
            # 窗口宽高
            self.win_width = self.ui.background.size().width()
            self.win_height = self.ui.background.size().height()

            # 移动事件
            if self.cursor_win_pos.x() < self.win_width and self.cursor_win_pos.y() < self.win_height:
                self._move_drag = True

            # 右下角边界拉伸事件
            if self.cursor_win_pos.x() > self.win_width - 5 and self.cursor_win_pos.y() > self.win_height - 5:
                self._corner_drag = True

            # 底部边界拉伸事件
            if self.cursor_win_pos.x() < self.win_width and self.cursor_win_pos.y() > self.win_height - 5:
                self._bottom_drag = True

            # 右侧边界拉伸事件
            if self.cursor_win_pos.x() > self.win_width - 5 and self.cursor_win_pos.y() < self.win_height:
                self._right_drag = True

            event.accept()

    def mouseMoveEvent(self, event):
        # 更新活动时间戳
        self.update_activity_time()

        if self.ui.winMaxRButton.isChecked() is False:
            # 仅在左键按下时触发移动、拉伸事件
            if event.buttons() == Qt.LeftButton:
                # 移动事件
                if self._move_drag:
                    move_pos = event.globalPosition() - self.cursor_win_pos
                    self.move(move_pos.x(), move_pos.y())

                # 右下角边界拉伸事件
                elif self._corner_drag:
                    self.resize(event.position().x() + 9, event.position().y() + 9)

                # 底部边界拉伸事件
                elif self._bottom_drag:
                    self.resize(self.width(), event.position().y() + 9)

                # 右侧边界拉伸事件
                elif self._right_drag:
                    self.resize(event.position().x() + 9, self.height())


            # 鼠标在窗口中的位置
            self.cursor_win_pos = event.globalPosition() - self.pos()
            # 窗口宽高
            self.win_width = self.ui.background.size().width()
            self.win_height = self.ui.background.size().height()

            # 右下光标样式事件
            if self.cursor_win_pos.x() > self.win_width - 5 and self.cursor_win_pos.y() > self.win_height - 5:
                self.setCursor(QCursor(Qt.SizeFDiagCursor))
            # 底部光标样式事件
            elif self.cursor_win_pos.x() < self.win_width and self.cursor_win_pos.y() > self.win_height - 5:
                self.setCursor(QCursor(Qt.SizeVerCursor))
            # 右侧光标样式事件
            elif self.cursor_win_pos.x() > self.win_width - 5 and self.cursor_win_pos.y() < self.win_height:
                self.setCursor(QCursor(Qt.SizeHorCursor))
            else:
                self.setCursor(QCursor(Qt.ArrowCursor))

            event.accept()

    def mouseReleaseEvent(self, event):
        self._move_drag = False
        self._corner_drag = False
        self._bottom_drag = False
        self._right_drag = False
        event.accept()

    def window_max_min(self, state: bool):
        if state:
            self.ui.FormLayout.setContentsMargins(0, 0, 0, 0)
            self.showMaximized()
        else:
            self.showNormal()
            self.ui.FormLayout.setContentsMargins(9, 9, 9, 9)
            QTimer.singleShot(0, self.resize_table_view)

    def double_click_event(self):
        if time.time() - self.double_click_timer < 0.35:
            self.ui.winMaxRButton.setChecked(not self.ui.winMaxRButton.isChecked())
        self.double_click_timer = time.time()

    def close_event(self):
        self.ui.winMaxRButton.setChecked(False)
        self.close()

    # ########################################## 界面活动检测 ##########################################

    def update_activity_time(self):
        """更新活动时间戳"""
        self.last_activity_time = time.time()

    def keyPressEvent(self, event):
        """键盘按下事件"""
        super(MainWindow, self).keyPressEvent(event)
        # 更新活动时间戳
        self.update_activity_time()

    def showEvent(self, event):
        """窗口显示事件"""
        super(MainWindow, self).showEvent(event)
        # 更新活动时间戳
        self.update_activity_time()
        # 当窗口重新显示时，强制更新UI
        self.force_update_ui()

    def focusInEvent(self, event):
        """窗口获得焦点事件"""
        super(MainWindow, self).focusInEvent(event)
        # 更新活动时间戳
        self.update_activity_time()
        # 当窗口获得焦点时，强制更新UI
        self.force_update_ui()

    def force_update_ui(self):
        """强制更新UI元素"""
        self.logger.info("强制更新UI元素")

        try:
            # 强制更新音乐名称标签
            if hasattr(self.ui, 'musicNameLabel'):
                self.ui.musicNameLabel.update()
                self.ui.musicNameLabel.repaint()

            # 强制更新播放滑块
            if hasattr(self.ui, 'playSlider1'):
                self.ui.playSlider1.update()
                self.ui.playSlider1.repaint()

            # 强制更新时间文本
            if hasattr(self.ui, 'playSliderTxt1'):
                self.ui.playSliderTxt1.update()
                self.ui.playSliderTxt1.repaint()

            # 强制更新整个窗口
            self.update()
            self.repaint()

        except Exception as e:
            self.logger.error(f"强制更新UI时出错: {e}")

    def is_long_time_inactive(self, threshold=60):
        """检测是否长时间未活动

        Args:
            threshold (int): 阈值，单位为秒，默认为60秒

        Returns:
            bool: 是否长时间未活动
        """
        return time.time() - self.last_activity_time > threshold