from pygame import mixer
import threading
import time
from enum import Enum
from pathlib import Path

try:
    from mutagen import File
    MUTAGEN_AVAILABLE = True
except ImportError:
    MUTAGEN_AVAILABLE = False


class PlayStatus(Enum):
    STOPPED = "stopped"
    PLAYING = "playing"
    PAUSED = "paused"
    FINISHED = "finished"


class Player:
    """
    音频播放器类，支持播放、暂停、恢复、停止等功能
    使用 pygame.mixer 库
    """

    def __init__(self, logger):
        """
        初始化播放器

        Args:
            logger (logging): 日志记录器
        """
        self.logger = logger

        # 初始化 pygame mixer
        try:
            self.mixer = mixer
            self.mixer.init()
            self.logger.info("pygame.mixer 初始化成功")
        except Exception as e:
            self.logger.error(f"pygame.mixer 初始化失败: {e}")
            raise

        # 文件路径和音频信息
        self.filepath = None
        self.total_duration = 0
        self.samplerate = 44100
        self.channels = 2

        # 播放状态和位置
        self.status = PlayStatus.STOPPED
        self.current_position = 0.0
        self.start_position = 0.0
        self.pause_position = 0.0
        self.play_start_time = None

        # 线程同步
        self._lock = threading.Lock()
        self._stop_event = threading.Event()
        self._position_thread = None

    def load_audio(self, filepath):
        """
        加载音频文件

        Args:
            filepath (str): 音频文件路径

        Returns:
            bool: 是否成功加载
        """
        # 检查文件是否存在
        if not Path(filepath).exists():
            self.logger.error(f"音频文件不存在: {filepath}")
            return False

        # 停止当前播放（如果有）
        if self.status != PlayStatus.STOPPED:
            self.stop()

        self.filepath = filepath

        try:
            # 加载音频文件
            self.mixer.music.load(filepath)

            # 获取音频时长
            self.total_duration = self._get_audio_duration(filepath)

            # 重置播放位置
            self.current_position = 0.0
            self.start_position = 0.0
            self.pause_position = 0.0
            self.status = PlayStatus.STOPPED

            self.logger.info(f"成功加载音频文件: {Path(filepath).name}")
            self.logger.info(f"  时长: {self.total_duration:.2f}秒")
            return True

        except Exception as e:
            self.logger.error(f"加载音频文件失败: {e}")
            self.logger.error(f"  文件路径: {filepath}")
            self.logger.error(f"  错误类型: {type(e).__name__}")
            import traceback
            self.logger.error(f"  详细错误:\n{traceback.format_exc()}")
            self.filepath = None
            self.total_duration = 0
            return False

    def _get_audio_duration(self, filepath):
        """
        获取音频文件时长

        Args:
            filepath (str): 音频文件路径

        Returns:
            float: 时长（秒）
        """
        if MUTAGEN_AVAILABLE:
            try:
                audio_file = File(filepath)
                if audio_file and hasattr(audio_file, 'info') and audio_file.info.length:
                    return audio_file.info.length
            except Exception as e:
                self.logger.warning(f"使用 mutagen 获取时长失败: {e}")

        # 如果 mutagen 不可用或失败，使用 pygame 的方式
        # 注意：pygame 没有直接获取时长的方法，这里返回 0
        # 实际时长会在播放过程中动态更新
        self.logger.warning("无法获取音频时长，将在播放过程中更新")
        return 0.0

    def _update_position_thread(self):
        """更新当前播放位置的线程"""
        while not self._stop_event.is_set():
            with self._lock:
                if self.status == PlayStatus.PLAYING and self.play_start_time:
                    elapsed = time.time() - self.play_start_time
                    self.current_position = self.start_position + elapsed

                    # 检查是否播放完成
                    if self.total_duration > 0 and self.current_position >= self.total_duration:
                        self.status = PlayStatus.FINISHED
                        self.current_position = self.total_duration
                        break
            time.sleep(0.05)

    def play(self, start_time=0):
        """
        开始播放音频

        Args:
            start_time (float, optional): 开始播放的时间点（秒）

        Returns:
            bool: 是否成功开始播放
        """
        if self.status == PlayStatus.PLAYING:
            self.logger.info("音频已经在播放中")
            return False

        if self.filepath is None:
            self.logger.error("音频未加载，无法播放")
            return False

        with self._lock:
            # 设置播放位置
            self.start_position = max(0.0, min(start_time, self.total_duration))
            self.current_position = self.start_position
            self.play_start_time = time.time()

            try:
                # 开始播放
                self.mixer.music.play(start=0, loops=0)

                # 如果需要从指定位置开始播放
                if start_time > 0:
                    self.mixer.music.set_pos(start_time)

                self.status = PlayStatus.PLAYING

                # 启动位置更新线程
                self._stop_event.clear()
                self._position_thread = threading.Thread(target=self._update_position_thread, daemon=True)
                self._position_thread.start()

                self.logger.info(f"开始播放: {Path(self.filepath).name} 从位置: {start_time:.2f}秒 开始")
                return True

            except Exception as e:
                self.logger.error(f"播放失败: {e}")
                self.status = PlayStatus.STOPPED
                return False

    def pause(self):
        """
        暂停播放

        Returns:
            bool: 是否成功暂停
        """
        if self.status != PlayStatus.PLAYING:
            self.logger.info(f"当前状态为 {self.status.value}，无法暂停")
            return False

        with self._lock:
            try:
                self.mixer.music.pause()
                self.pause_position = self.current_position
                self.status = PlayStatus.PAUSED
                self.logger.info("播放已暂停")
                return True
            except Exception as e:
                self.logger.error(f"暂停失败: {e}")
                return False

    def resume(self):
        """
        恢复播放（从暂停位置继续）

        Returns:
            bool: 是否成功恢复
        """
        if self.status != PlayStatus.PAUSED:
            self.logger.info(f"当前状态为 {self.status.value}，无法恢复")
            return False

        with self._lock:
            try:
                self.mixer.music.unpause()
                self.start_position = self.pause_position
                self.play_start_time = time.time()
                self.status = PlayStatus.PLAYING

                # 重新启动位置更新线程
                self._stop_event.clear()
                self._position_thread = threading.Thread(target=self._update_position_thread, daemon=True)
                self._position_thread.start()

                self.logger.info("播放已恢复")
                return True
            except Exception as e:
                self.logger.error(f"恢复播放失败: {e}")
                return False

    def stop(self):
        """
        停止播放（重置到开始）

        Returns:
            bool: 是否成功停止
        """
        with self._lock:
            # 停止更新线程
            self._stop_event.set()

            # 停止音频播放
            try:
                self.mixer.music.stop()
            except Exception:
                pass

            # 重置状态
            self.filepath = None
            self.total_duration = 0
            self.current_position = 0.0
            self.start_position = 0.0
            self.pause_position = 0.0
            self.play_start_time = None
            self.status = PlayStatus.STOPPED

        self.logger.info("播放已停止")
        return True

    def set_volume(self, volume):
        """
        设置音量（0.0到1.0之间）

        Args:
            volume (float): 音量值（0.0到1.0）
        """
        with self._lock:
            self.mixer.music.set_volume(volume)
            self.volume = volume
            self.logger.info(f"音量设置为: {volume:.2f}")

    def is_finished(self):
        """
        检查音频是否播放完毕

        Returns:
            bool: 是否播放完毕
        """
        with self._lock:
            if self.status == PlayStatus.FINISHED:
                return True
            if self.total_duration > 0 and self.current_position >= self.total_duration:
                return True
            return False

    def get_current_time(self):
        """
        获取当前播放的时间点（秒）

        Returns:
            float: 当前播放时间（秒），如果未播放则返回-1.0
        """
        with self._lock:
            if self.status == PlayStatus.STOPPED:
                return -1.0
            elif self.status == PlayStatus.PAUSED:
                return self.pause_position
            elif self.status == PlayStatus.FINISHED:
                return self.total_duration
            else:
                return self.current_position

    def seek(self, time_seconds):
        """
        跳转到指定时间点

        Args:
            time_seconds (float): 目标时间（秒）

        Returns:
            bool: 是否成功跳转
        """
        if self.total_duration > 0 and (time_seconds < 0 or time_seconds > self.total_duration):
            self.logger.error(f"跳转时间超出范围: 0.0 - {self.total_duration:.2f}")
            return False

        # 如果正在播放，需要先暂停
        was_playing = self.status == PlayStatus.PLAYING

        if was_playing:
            self.pause()

        # 设置新位置
        success = False
        with self._lock:
            try:
                self.mixer.music.set_pos(time_seconds)

                self.start_position = time_seconds
                self.pause_position = time_seconds
                self.current_position = time_seconds

                self.logger.info(f"跳转到: {time_seconds:.2f}秒")
                success = True
            except Exception as e:
                self.logger.error(f"跳转失败: {e}")
                success = False

        # 如果之前正在播放，则继续播放
        if success and was_playing:
            return self.resume()

        return success

    def get_status(self):
        """
        获取当前播放状态

        Returns:
            PlayStatus: 播放状态
        """
        return self.status

    def get_audio_info(self):
        """
        获取音频文件信息

        Returns:
            dict: 音频信息字典
        """
        return {
            'filepath': self.filepath,
            'duration': self.total_duration,
            'samplerate': self.samplerate,
            'channels': self.channels,
            'format': Path(self.filepath).suffix[1:].upper() if self.filepath else None
        }

    def wait_until_finished(self, check_interval=0.1):
        """
        阻塞直到播放完成

        Args:
            check_interval (float): 检查间隔（秒）
        """
        while self.status == PlayStatus.PLAYING:
            time.sleep(check_interval)

    def __del__(self):
        """析构函数，确保资源被释放"""
        try:
            self.stop()
            self.mixer.quit()
        except Exception:
            pass
