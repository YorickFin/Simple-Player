
import shutil
import random
import time
import subprocess
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QObject, Signal, QTimer, Qt
from PySide6.QtGui import QIcon, QPixmap
from threading import Thread, Event
from pathlib import Path
from collections import deque

from res.main_win import MainWindow
from res.TrayAction import TrayAction
from res.tablemodel import create_rounded_pixmap
from src.player import Player
from src.audio_extract import AudioExtractor
from res.lyrics_win import LyricsWindow



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
    update_desktop_lyrics_signal = Signal(str)
    sync_desktop_lyrics_signal = Signal(float)

    def __init__(self, logger):
        super().__init__()
        self.logger = logger

        self.signal_manager = None

        self.main_window = None
        self.lyric_window = None
        self.tray_action = None

        self.play_flag = False                          # 播放标志
        self.play_status = None                         # 播放状态
        self.play_mode = None                           # 播放模式
        self.current_music = None                       # 当前播放音乐
        self.play_list = []                             # 播放列表
        self.played_deque = None                        # 已播放列表
        self.music_dict = {}                            # 名称与路径的映射
        self.player = Player(logger)

        self.stop_event = Event()
        self.slider_timer = None
        self.timer_last_start = 0.0

        self.ZonyLrcTools_path = Path(r'plugins\ZonyLrcTools\ZonyLrcTools.Cli.exe')

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
            'clear_play_info': lambda: self.clear_play_info(),
            'open_desktop_lyrics': lambda: self.open_desktop_lyrics(),
            'close_desktop_lyrics': lambda: self.close_desktop_lyrics(),
        }
        branch.get(value.get('action'), lambda: print(f'action not found: {value}'))()

    def play_music(self, value: dict):
        """播放"""
        self.stop_current_playback()
        self.music_dict = value['music_dict']
        self.play_list = list(value['music_dict'].values())
        self.played_deque = deque(maxlen=min(len(self.play_list) // 2, 10))
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
        try:
            info = value.get('info')

            if info == 'resume':
                self.player.resume()

            elif info == 'pause':
                self.player.pause()

            elif info == 'pgup':
                # 停止当前播放
                self.stop_current_playback()

                # 如果已播放列表为空, 在播放列表里随机选择一首
                if not self.played_deque or len(self.played_deque) == 1:
                    music_path = random.choice(self.play_list)
                else:
                    # 获取上一首音乐路径
                    self.played_deque.pop()
                    music_path = self.played_deque.pop()

                # 启动播放线程
                self.play_flag = True
                Thread(target=self.play_mode_control, args=(music_path,), daemon=True).start()

            elif info == 'pgdn':
                # 停止当前播放
                self.stop_current_playback()

                # 随机播放模式
                if self.play_mode == 'random_play':
                    # 随机选择一首未播放的歌曲
                    music_path = random.choice(self.play_list)
                    while music_path in self.played_deque:
                        music_path = random.choice(self.play_list)

                # 顺序播放模式
                else:
                    # 顺序播放模式
                    if not self.current_music:
                        # 如果当前没有播放歌曲, 从第一首开始
                        music_path = self.play_list[0]
                    else:
                        index = self.play_list.index(self.current_music)
                        if index == len(self.play_list) - 1:
                            # 如果是最后一首, 循环到第一首
                            music_path = self.play_list[0]
                        else:
                            # 否则播放下一首
                            music_path = self.play_list[index + 1]

                # 启动播放线程
                self.play_flag = True
                Thread(target=self.play_mode_control, args=(music_path,), daemon=True).start()
        except Exception as e:
            self.logger.error(f"播放控制失败: {e}")
            import traceback
            self.logger.error(f"详细错误:\n{traceback.format_exc()}")

    def play_mode_control(self, music_path: str):
        """播放模式控制"""
        try:
            while self.play_flag:

                # 加载音频
                if not self.player.load_audio(music_path):
                    self.logger.error(f"加载音频失败: {music_path}")
                    # 尝试播放下一首
                    music_path = self.get_next_music(music_path)
                    continue

                # 播放音频
                if not self.player.play():
                    self.logger.error(f"播放失败: {music_path}")
                    # 尝试播放下一首
                    music_path = self.get_next_music(music_path)
                    continue

                # 设置播放信息
                self.set_play_info(music_path)
                # 启动进度条定时器
                self.start_timer_signal.emit()

                # 更新当前播放信息
                self.current_music = music_path

                # 添加到已播放列表
                self.played_deque.append(music_path)

                # 更新桌面歌词
                self.update_desktop_lyrics(music_path)

                # 等待音乐播放完毕或停止
                stuck_count = 0
                max_stuck = 10
                while self.play_flag and not self.player.is_finished():
                    # 增加超时时间, 减少CPU占用
                    if self.stop_event.wait(timeout=0.2):
                        # 如果收到停止信号, 退出循环
                        break

                    # 每0.2秒检查一次播放状态
                    current_time = self.player.get_current_time()
                    if current_time == -1.0:
                        # 播放时间获取失败, 可能是播放器卡住
                        stuck_count += 1
                        if stuck_count > max_stuck:
                            self.logger.warning(f"播放器可能卡住, 强制切换下一首: {Path(music_path).name}")
                            self.player.stop()
                            break
                    else:
                        # 播放正常, 重置卡住计数
                        stuck_count = 0

                # 检查是否需要退出循环
                if not self.play_flag:
                    break

                # 根据播放模式获取下一首音乐
                if self.play_mode == 'loop_one_song':
                    # 单曲循环模式, 继续播放当前歌曲
                    continue
                else:
                    # 获取下一首音乐
                    music_path = self.get_next_music(music_path)
                    if not music_path:
                        # 如果没有下一首音乐, 退出循环
                        self.logger.warning("没有可播放的音乐, 退出播放模式")
                        break
        except Exception as e:
            self.logger.error(f"播放模式控制失败: {e}")
            import traceback
            self.logger.error(f"详细错误:\n{traceback.format_exc()}")
        finally:
            # 确保在异常情况下停止播放器
            if self.player:
                self.player.stop()

    def get_next_music(self, current_music: str):
        """根据播放模式获取下一首音乐"""
        try:
            if not self.play_list:
                return None

            # 顺序播放模式
            if self.play_mode == 'ordered_play':
                index = self.play_list.index(current_music)
                if index == len(self.play_list) - 1:
                    # 如果是最后一首, 循环到第一首
                    return self.play_list[0]
                else:
                    # 否则播放下一首
                    return self.play_list[index + 1]

            # 随机播放模式
            elif self.play_mode == 'random_play':
                music_path = random.choice(self.play_list)
                while music_path in self.played_deque:
                    music_path = random.choice(self.play_list)
                return music_path

        except Exception as e:
            self.logger.error(f"获取下一首音乐失败: {e}")
            # 出错时返回播放列表的第一首
            return self.play_list[0] if self.play_list else None

    def set_play_mode(self, value: dict):
        """设置播放模式"""
        self.play_mode = value['play_mode']

    def clear_play_info(self):
        """清空已播放列表"""
        self.play_list.clear()
        self.current_music = None
        if self.played_deque is not None:
            self.played_deque.clear()

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
            self.logger.warning("主窗口不存在, 无法更新UI")
            return

        # 检查滑块是否被按下
        if self.main_window.slider_pressed:
            return

        # 检查UI元素是否存在
        if not hasattr(self.main_window, 'ui'):
            self.logger.warning("UI对象不存在, 无法更新UI")
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
        # 设置定时器为单次触发, 确保在界面切后台时仍然运行
        self.slider_timer.setSingleShot(False)
        # 连接timeout信号到更新方法
        self.slider_timer.timeout.connect(self.update_play_slider)
        # 启动定时器, 间隔1000毫秒
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

        # 检查定时器状态, 确保定时器正常运行
        if self.slider_timer and not self.slider_timer.isActive():
            self.logger.warning("滑块定时器异常停止, 正在重启")
            self.start_slider_timer()

        # 检查定时器是否长时间未启动, 可能是界面切后台导致
        current_time = time.time()
        if current_time - self.timer_last_start > 60:  # 超过60秒未更新, 重新启动定时器
            self.logger.warning("滑块定时器长时间未更新, 正在重启")
            self.start_slider_timer()

        # 获取当前播放时间
        value = self.player.get_current_time()

        # 如果获取失败, 不立即停止定时器, 而是继续尝试
        if value == -1.0:
            # 不立即停止定时器, 而是等待下次尝试
            self.logger.debug("获取播放时间失败, 继续尝试")
            return

        # 更新定时器最后启动时间, 避免频繁重启
        self.timer_last_start = current_time

        # 计算总时长
        total_duration = self.main_window.ui.playSlider1.maximum()
        if total_duration <= 0:
            # 如果总时长未设置, 尝试从播放器获取
            total_duration = self.player.get_total_duration() if hasattr(self.player, 'get_total_duration') else 0

        # 格式化时间文本
        text = f'{AudioExtractor().format_duration(value)}/{AudioExtractor().format_duration(total_duration)}'

        # 发送更新信号
        self.signal_manager.update_slider_signal.emit(value, text)

        # 同步桌面歌词
        self.sync_desktop_lyrics(value)

    def update_music_name(self, music_name: str):
        """在主线程中更新音乐名称"""
        self.main_window.ui.musicNameLabel.setText(music_name)

    def open_desktop_lyrics(self):
        """打开桌面歌词窗口"""
        self.lyric_window = LyricsWindow(self.signal_manager, self.logger)
        self.lyric_window.show()

        self.lyric_window.set_lyric_offset(0.5)

        if self.current_music:
            self.update_desktop_lyrics(self.current_music)
            current_time = self.player.get_current_time()
            if current_time >= 0:
                self.sync_desktop_lyrics(current_time)

    def close_desktop_lyrics(self):
        """关闭桌面歌词窗口"""
        self.lyric_window.close()

    def update_desktop_lyrics(self, music_path: str):
        """更新桌面歌词（线程安全，通过信号调用）"""
        self.update_desktop_lyrics_signal.emit(music_path)

    def _update_desktop_lyrics_slot(self, music_path: str):
        """更新桌面歌词的槽函数（在主线程执行）"""
        if not self.lyric_window:
            return

        path = Path(music_path)
        lrc = path.with_suffix('.lrc')
        audio_info = AudioExtractor().extract(music_path, extract_cover=False)
        if audio_info.lyrics:
            self.logger.info(f"找到嵌入歌词: {path}")
            self.lyric_window.load_lrc(audio_info.lyrics)
        elif lrc.exists():
            self.logger.info(f"找到歌词文件: {lrc}")
            self.lyric_window.load_lrc(lrc)
        elif self.ZonyLrcTools_path.exists():
            self.logger.info(f"尝试从网络获取歌词: {path}")
            temp_dir = Path(r'res\temp')
            if temp_dir.exists():
                shutil.rmtree(temp_dir)
            temp_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy(path, temp_dir / path.name)
            process = subprocess.Popen(
                f'"{self.ZonyLrcTools_path}" download -d "{temp_dir}" -l -n 2',
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            process.wait()
            # 检查是否成功下载歌词
            lrc_file = temp_dir / f"{path.stem}.lrc"
            if lrc_file.exists():
                self.logger.info(f"成功下载歌词到: {lrc_file}")
                shutil.copy(lrc_file, lrc)
                self.lyric_window.load_lrc(lrc_file)
            else:
                self.logger.error(f"从网络下载歌词失败: {path}")
            shutil.rmtree(temp_dir)
        else:
            self.logger.info(f"未能从网络或文件中找到歌词: {path}")
            self.lyric_window.lyric_.clear()
            self.lyric_window._update_display()

    def sync_desktop_lyrics(self, play_time_seconds: float):
        """同步桌面歌词到播放时间（线程安全，通过信号调用）"""
        self.sync_desktop_lyrics_signal.emit(play_time_seconds)

    def _sync_desktop_lyrics_slot(self, play_time_seconds: float):
        """同步桌面歌词的槽函数（在主线程执行）"""
        if self.lyric_window and self.lyric_window.isVisible():
            self.lyric_window.sync_to_time(int(play_time_seconds * 1000))

    def open_window(self, value: dict):
        """打开窗口"""
        if value['info'] == '打开主窗口':
            self.signal_manager = value['signal_manager']
            self.logger = value['logger']
            self.main_window = MainWindow(self.signal_manager, self.logger)
            self.signal_manager.update_slider_signal.connect(self.update_ui_slider)
            self.signal_manager.update_music_name_signal.connect(self.update_music_name)
            self.start_timer_signal.connect(self.start_slider_timer)
            self.update_desktop_lyrics_signal.connect(self._update_desktop_lyrics_slot)
            self.sync_desktop_lyrics_signal.connect(self._sync_desktop_lyrics_slot)
            self.main_window.show()

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