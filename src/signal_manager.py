

import os
import time
import random
from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QIcon, QPixmap
from threading import Thread
from pathlib import Path

from res.main_win import MainWindow
from res.TrayAction import TrayAction
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

    def __init__(self, logger):
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
        self.player = Player(logger)

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
        self.main_window.ui.playRButton1.setEnabled(False)
        self.main_window.ui.playRButton1.setChecked(True)
        self.main_window.ui.playRButton1.setEnabled(True)

        # self.main_window.ui.playRButton2.setEnabled(False)
        # self.main_window.ui.playRButton2.setChecked(True)
        # self.main_window.ui.playRButton2.setEnabled(True)

        self.play_flag = False
        time.sleep(0.3)
        self.play_list = value['music_list']
        self.play_mode = value['play_mode']
        self.play_flag = True
        Thread(target=self.play_mode_control, args=(value['music_path'],)).start()

    def play_control(self, value: dict):
        """播放控制"""
        if value['info'] == 'resume':
            self.player.resume()

        elif value['info'] == 'pause':
            self.player.pause()

        elif value['info'] == 'pgup':
            self.play_flag = False
            time.sleep(0.3)
            self.play_flag = True
            music_path = self.played_list[-2] if len(self.played_list) > 1 else self.played_list[-1]
            Thread(target=self.play_mode_control, args=(music_path,)).start()

        elif value['info'] == 'pgdn':
            self.play_flag = False
            time.sleep(0.3)
            self.play_flag = True
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
            Thread(target=self.play_mode_control, args=(music_path,)).start()

    def play_mode_control(self, music_path: str):
        """播放模式控制"""
        while self.play_flag:
            self.set_play_info(music_path)
            Thread(target=self.update_play_slider).start()

            self.current_music = music_path
            self.played_list.append(music_path)

            self.player.load_audio(music_path)
            self.player.play()
            while not self.player.is_finished():
                time.sleep(0.1)

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
        """设置播放进度条"""
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
            self.main_window.ui.musicLogoPushButton.setIcon(QIcon(QPixmap(cover_data)))
        else:
            pixmap = QPixmap()
            pixmap.loadFromData(cover_data)
            self.main_window.ui.musicLogoPushButton.setIcon(QIcon(pixmap))

    def update_ui_slider(self, value: int, text: str):
        """在主线程中更新UI"""
        if self.main_window.slider_pressed:
            return
        self.main_window.ui.playSlider1.setValue(value)
        self.main_window.ui.playSliderTxt1.setText(text)

    def update_play_slider(self):
        """更新播放进度条"""
        while self.play_flag:
            time.sleep(1)
            value = self.player.get_current_time()
            if value == -1.0:
                self.signal_manager.update_slider_signal.emit(0, '00:00/00:00')
                break
            text = f'{AudioExtractor().format_duration(value)}/{AudioExtractor().format_duration(self.main_window.ui.playSlider1.maximum())}'
            self.signal_manager.update_slider_signal.emit(value, text)

    def open_window(self, value: dict):
        """打开窗口"""
        if value['info'] == '打开主窗口':
            self.signal_manager = value['signal_manager']
            self.logger = value['logger']
            self.main_window = MainWindow(self.signal_manager, self.logger)
            self.signal_manager.update_slider_signal.connect(self.update_ui_slider)
            self.signal_manager.update_music_name_signal.connect(self.update_music_name)
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
        self.tray_action.cleanTray()
        os._exit(0)