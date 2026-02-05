
import random
import time
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QObject, Signal, QTimer, Qt
from PySide6.QtGui import QIcon, QPixmap
from threading import Thread, Event
from pathlib import Path

from res.main_win import MainWindow
from res.TrayAction import TrayAction
from res.tablemodel import create_rounded_pixmap
from src.player import Player
from src.audio_extract import AudioExtractor

class SignalManager(QObject):
    """信号管理器"""

    dict_signal = Signal(dict)
    update_slider_signal = Signal(int, str)
    update_music_name_signal = Signal(str)

    def send_signal(self, value: dict):
        """发送信号"""
        self.dict_signal.emit(value)

class SlotManager(QObject):
    """槽管理器"""

    update_slider_signal = Signal(int, str)
    play_finished_signal = Signal()
    start_timer_signal = Signal()

    def __init__(self, logger):
        super().__init__()
        self.logger = logger

        self.signal_manager = None

        self.main_window = None
        self.tray_action = None

        self.play_flag = False      # 播放标志
        self.play_status = None     # 播放状态
        self.play_mode = None       # 播放模式
        self.current_music = None   # 当前播放音乐
        self.play_list = []         # 播放列表
        self.played_list = []       # 已播放列表
        self.music_dict = {}        # 名称与路径的映射
        self.player = Player(logger)

        self.stop_event = Event()
        self.slider_timer = None
        self.timer_last_start = 0.0

    def handle_signal(self, value: dict):
        """处理信号"""
        self.logger.info(value)
        branch = {
            '打开窗口': lambda: self.open_window(value),
            '激活窗口': lambda: self.activate_window(),
            '创建托盘': lambda: self.create_tray(),
            '退出程序': lambda: self.exit_program(),

            'seek': lambda: self.player.seek(value['info']),
            'play_music': lambda: self.play_music(value),
            'play_control': lambda: self.play_control(value),
            'set_play_mode': lambda: self.set_play_mode(value),
            'set_volume': lambda: self.player.set_volume(value['volume']),
            'clear_played_list': lambda: self.clear_played_list(),
        }
        branch.get(value.get('action'), lambda: print(f'action not found: {value}'))()

    def play_music(self, value: dict):
        """播放"""
        self.stop_current_playback()
        self.music_dict = value['music_dict']
        self.play_list = list(value['music_dict'].values())
        self.play_mode = value['play_mode']
        self.play_flag = True
        Thread(target=self.play_mode_control, args=(value['music_path'],)).start()

    def stop_current_playback(self):
        """停止当前播放"""
        if self.play_flag:
            self.play_flag = False
            self.stop_event.set()
            self.player.stop()
            self.stop_event.clear()
        self.stop_slider_timer()

    def play_control(self, value: dict):
        """播放控制"""
        if value['info'] == 'resume':
            self.player.resume()

        elif value['info'] == 'pause':
            self.player.pause()

        elif value['info'] == 'pgup':
            self.stop_current_playback()
            music_path = self.played_list[-2] if len(self.played_list) > 1 else self.played_list[-1]
            self.play_flag = True
            Thread(target=self.play_mode_control, args=(music_path,)).start()

        elif value['info'] == 'pgdn':
            self.stop_current_playback()
            if self.play_mode == 'random_play':
                music_path = random.choice(self.play_list)
                while music_path in self.played_list:
                    music_path = random.choice(self.play_list)
            else:
                index = self.play_list.index(self.current_music)
                if index == len(self.play_list) - 1:
                    music_path = self.play_list[0]
                else:
                    music_path = self.play_list[index + 1]
            self.play_flag = True
            Thread(target=self.play_mode_control, args=(music_path,)).start()

    def play_mode_control(self, music_path: str):
        """播放模式控制"""
        while self.play_flag:
            self.set_play_info(music_path)
            self.start_timer_signal.emit()

            self.current_music = music_path
            self.played_list.append(music_path)

            self.player.load_audio(music_path)
            self.player.play()

            stuck_count = 0
            max_stuck = 10
            while self.play_flag and not self.player.is_finished():
                if self.stop_event.wait(timeout=0.05):
                    break
                current_time = self.player.get_current_time()
                if current_time == -1.0:
                    stuck_count += 1
                    if stuck_count > max_stuck:
                        self.logger.warning(f"播放器可能卡住，强制切换下一首: {Path(music_path).name}")
                        self.player.stop()
                        break
                else:
                    stuck_count = 0

            if not self.play_flag:
                break

            if self.play_mode == 'loop_one_song':
                continue

            elif self.play_mode == 'ordered_play':
                index = self.play_list.index(self.current_music)
                if index == len(self.play_list) - 1:
                    music_path = self.play_list[0]
                else:
                    music_path = self.play_list[index + 1]

            elif self.play_mode == 'random_play':
                music_path = random.choice(self.play_list)
                while music_path in self.played_list:
                    music_path = random.choice(self.play_list)

    def set_play_mode(self, value: dict):
        """设置播放模式"""
        self.play_mode = value['play_mode']

    def clear_played_list(self):
        """清空已播放列表"""
        self.play_list.clear()
        self.played_list.clear()
        self.current_music = None

    def set_play_info(self, music_path: str):
        """设置播放信息"""
        audio_info = AudioExtractor().extract(music_path, extract_cover=True)
        self.main_window.ui.playSlider1.setRange(0, int(audio_info.duration))
        # self.main_window.ui.playSlider2.setRange(0, int(audio_info.duration))
        self.main_window.ui.playSlider1.setValue(0)
        # self.main_window.ui.playSlider2.setValue(0)
        self.main_window.ui.playSliderTxt1.setText(f'00:00/{AudioExtractor().format_duration(audio_info.duration)}')
        # self.main_window.ui.playSliderTxt2.setText(f'00:00/{AudioExtractor().format_duration(audio_info.duration)}')

        music_name = Path(music_path).stem
        self.signal_manager.update_music_name_signal.emit(music_name)
        cover_data = audio_info.cover_data
        if not cover_data:
            cover_data = r'res\img\music.png'
            pixmap = QPixmap(cover_data)
        else:
            pixmap = QPixmap()
            if not pixmap.loadFromData(cover_data):
                pixmap = QPixmap(r'res\img\music.png')
        if not pixmap.isNull():
            pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.main_window.ui.musicLogoPButton.setIcon(QIcon(create_rounded_pixmap(pixmap, radius=18)))

    def update_ui_slider(self, value: int, text: str):
        """在主线程中更新UI"""
        # 检查主窗口是否存在
        if not self.main_window:
            self.logger.warning("主窗口不存在，无法更新UI")
            return

        # 检查滑块是否被按下
        if self.main_window.slider_pressed:
            return

        # 检查UI元素是否存在
        if not hasattr(self.main_window, 'ui'):
            self.logger.warning("UI对象不存在，无法更新UI")
            return

        try:
            # 检查播放滑块是否存在
            if hasattr(self.main_window.ui, 'playSlider1'):
                # 更新滑块值
                self.main_window.ui.playSlider1.setValue(int(value))

            # 检查时间文本标签是否存在
            if hasattr(self.main_window.ui, 'playSliderTxt1'):
                # 更新时间文本
                self.main_window.ui.playSliderTxt1.setText(text)

            # 确保界面可见时强制更新
            if self.main_window.isVisible():
                # 强制更新UI
                self.main_window.ui.playSlider1.update()
                if hasattr(self.main_window.ui, 'playSliderTxt1'):
                    self.main_window.ui.playSliderTxt1.update()

        except Exception as e:
            self.logger.error(f"更新UI滑块时出错: {e}")

    def start_slider_timer(self):
        """启动进度条定时器"""
        self.stop_slider_timer()
        self.slider_timer = QTimer()
        # 设置定时器为单次触发，确保在界面切后台时仍然运行
        self.slider_timer.setSingleShot(False)
        # 连接timeout信号到更新方法
        self.slider_timer.timeout.connect(self.update_play_slider)
        # 启动定时器，间隔1000毫秒
        self.slider_timer.start(1000)
        # 记录定时器启动时间
        self.timer_last_start = time.time()

    def stop_slider_timer(self):
        """停止进度条定时器"""
        if self.slider_timer:
            self.slider_timer.stop()
            self.slider_timer = None

    def update_play_slider(self):
        """更新播放进度条"""
        # 检查播放标志
        if not self.play_flag:
            self.stop_slider_timer()
            return

        # 检查定时器状态，确保定时器正常运行
        if self.slider_timer and not self.slider_timer.isActive():
            self.logger.warning("滑块定时器异常停止，正在重启")
            self.start_slider_timer()

        # 检查定时器是否长时间未启动，可能是界面切后台导致
        current_time = time.time()
        if current_time - self.timer_last_start > 60:  # 超过60秒未更新，重新启动定时器
            self.logger.warning("滑块定时器长时间未更新，正在重启")
            self.start_slider_timer()

        # 获取当前播放时间
        value = self.player.get_current_time()

        # 如果获取失败，不立即停止定时器，而是继续尝试
        if value == -1.0:
            # 不立即停止定时器，而是等待下次尝试
            self.logger.debug("获取播放时间失败，继续尝试")
            return

        # 计算总时长
        total_duration = self.main_window.ui.playSlider1.maximum()
        if total_duration <= 0:
            # 如果总时长未设置，尝试从播放器获取
            total_duration = self.player.get_total_duration() if hasattr(self.player, 'get_total_duration') else 0

        # 格式化时间文本
        text = f'{AudioExtractor().format_duration(value)}/{AudioExtractor().format_duration(total_duration)}'

        # 发送更新信号
        self.signal_manager.update_slider_signal.emit(value, text)

    def open_window(self, value: dict):
        """打开窗口"""
        if value['info'] == '打开主窗口':
            self.signal_manager = value['signal_manager']
            self.logger = value['logger']
            self.main_window = MainWindow(self.signal_manager, self.logger)
            self.signal_manager.update_slider_signal.connect(self.update_ui_slider)
            self.signal_manager.update_music_name_signal.connect(self.update_music_name)
            self.start_timer_signal.connect(self.start_slider_timer)
            self.main_window.show()

    def update_music_name(self, music_name: str):
        """在主线程中更新音乐名称"""
        self.main_window.ui.musicNameLabel.setText(music_name)

    def activate_window(self):
        """激活窗口"""
        self.main_window.show()
        self.main_window.activateWindow()

    def create_tray(self):
        """创建托盘"""
        self.tray_action = TrayAction(self.signal_manager, self.logger)

    def exit_program(self):
        """退出程序"""
        self.stop_current_playback()
        self.tray_action.cleanTray()
        QApplication.instance().quit()