import time
from pygame import mixer
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
    音频播放器类, 支持播放、暂停、恢复、停止等功能
    使用 pygame.mixer 库
    """

    def __init__(self, logger):
        """
        初始化播放器

        Args:
            logger (logging): 日志记录器
        """
        self.logger = logger

        try:
            self.mixer = mixer
            self.mixer.init()
            self.logger.info("pygame.mixer 初始化成功")
        except Exception as e:
            self.logger.error(f"pygame.mixer 初始化失败: {e}")
            raise

        self.filepath = None
        self.samplerate = 44100
        self.channels = 2

        self.status = PlayStatus.STOPPED
        self.seek_offset = 0.0
        self.last_current_time = 0.0  # 上次成功获取的播放时间
        self.last_time_update = 0.0  # 上次更新时间的时间戳

    def load_audio(self, filepath):
        """
        加载音频文件

        Args:
            filepath (str): 音频文件路径

        Returns:
            bool: 是否成功加载
        """
        if not Path(filepath).exists():
            self.logger.error(f"音频文件不存在: {filepath}")
            return False

        if self.status != PlayStatus.STOPPED:
            self.stop()

        self.filepath = filepath

        try:
            self.mixer.music.load(filepath)
            self.status = PlayStatus.STOPPED
            self.logger.info(f"成功加载音频文件: {Path(filepath).name}")
            return True

        except Exception as e:
            self.logger.error(f"加载音频文件失败: {e}")
            self.logger.error(f"  文件路径: {filepath}")
            self.logger.error(f"  错误类型: {type(e).__name__}")
            import traceback
            self.logger.error(f"  详细错误:\n{traceback.format_exc()}")
            self.filepath = None
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

        self.logger.warning("无法获取音频时长, 将在播放过程中更新")
        return 0.0

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
            self.logger.error("音频未加载, 无法播放")
            return False

        try:
            self.mixer.music.play(start=0, loops=0)

            if start_time > 0:
                self.mixer.music.set_pos(start_time)
                self.seek_offset = start_time
            else:
                self.seek_offset = 0.0

            self.status = PlayStatus.PLAYING

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
            self.logger.info(f"当前状态为 {self.status.value}, 无法暂停")
            return False

        try:
            self.mixer.music.pause()
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
            self.logger.info(f"当前状态为 {self.status.value}, 无法恢复")
            return False

        try:
            self.mixer.music.unpause()
            self.status = PlayStatus.PLAYING
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
        try:
            self.mixer.music.stop()
        except Exception:
            pass

        self.filepath = None
        self.status = PlayStatus.STOPPED

        self.logger.info("播放已停止")
        return True

    def set_volume(self, volume):
        """
        设置音量（0.0到1.0之间）

        Args:
            volume (float): 音量值（0.0到1.0）
        """
        self.mixer.music.set_volume(volume)
        self.volume = volume
        self.logger.info(f"音量设置为: {volume:.2f}")

    def is_finished(self):
        """
        检查音频是否播放完毕

        Returns:
            bool: 是否播放完毕
        """
        if self.status == PlayStatus.FINISHED:
            return True
        if not self.mixer.music.get_busy() and self.status == PlayStatus.PLAYING:
            self.status = PlayStatus.FINISHED
            return True
        return False

    def get_current_time(self):
        """
        获取当前播放的时间点（秒）

        Returns:
            float: 当前播放时间（秒）, 如果未播放则返回-1.0
        """
        # 如果播放器已停止, 返回-1.0
        if self.status == PlayStatus.STOPPED:
            return -1.0

        # 获取当前时间戳
        current_time = time.time()

        try:
            # 尝试从pygame.mixer获取当前播放位置
            pos = self.mixer.music.get_pos()

            # 如果获取成功（pos != -1）
            if pos != -1:
                # 计算当前播放时间
                current_play_time = self.seek_offset + (pos / 1000.0)
                # 更新缓存的时间值
                self.last_current_time = current_play_time
                # 更新上次更新时间的时间戳
                self.last_time_update = current_time
                # 返回计算得到的时间
                return current_play_time
            else:
                # 如果获取失败（pos == -1）, 使用缓存的时间值
                # 计算从上一次更新到现在的时间差
                time_diff = current_time - self.last_time_update
                # 如果时间差小于60秒（避免长时间暂停后时间跳变）
                if time_diff < 60:
                    # 根据播放器状态决定是否递增时间
                    if self.status == PlayStatus.PLAYING:
                        # 播放状态下, 递增时间
                        estimated_time = self.last_current_time + time_diff
                        # 更新上次更新时间的时间戳
                        self.last_time_update = current_time
                        # 更新缓存的时间值
                        self.last_current_time = estimated_time
                        # 返回估计的时间
                        return estimated_time
                    else:
                        # 暂停或其他状态下, 返回缓存的时间
                        return self.last_current_time
                else:
                    # 时间差过大, 返回缓存的时间
                    return self.last_current_time

        except Exception as e:
            # 发生异常时, 使用缓存的时间值
            self.logger.error(f"获取当前播放时间失败: {e}")
            # 计算从上一次更新到现在的时间差
            time_diff = current_time - self.last_time_update
            # 如果时间差小于60秒
            if time_diff < 60:
                # 根据播放器状态决定是否递增时间
                if self.status == PlayStatus.PLAYING:
                    # 播放状态下, 递增时间
                    estimated_time = self.last_current_time + time_diff
                    # 更新上次更新时间的时间戳
                    self.last_time_update = current_time
                    # 更新缓存的时间值
                    self.last_current_time = estimated_time
                    # 返回估计的时间
                    return estimated_time
                else:
                    # 暂停或其他状态下, 返回缓存的时间
                    return self.last_current_time
            else:
                # 时间差过大, 返回缓存的时间
                return self.last_current_time

    def seek(self, time_seconds):
        """
        跳转到指定时间点

        Args:
            time_seconds (float): 目标时间（秒）

        Returns:
            bool: 是否成功跳转
        """
        try:
            self.mixer.music.set_pos(time_seconds)
            pos = self.mixer.music.get_pos()
            self.seek_offset = time_seconds - (pos / 1000.0)
            # 更新缓存的时间值
            self.last_current_time = time_seconds
            # 更新上次更新时间的时间戳
            self.last_time_update = time.time()
            self.logger.info(f"跳转到: {time_seconds:.2f}秒")
            return True
        except Exception as e:
            # 即使跳转失败, 也更新缓存的时间值, 确保UI显示正确
            self.last_current_time = time_seconds
            self.last_time_update = time.time()
            self.logger.error(f"跳转失败: {e}")
            return False

    def get_status(self):
        """
        获取当前播放状态

        Returns:
            PlayStatus: 播放状态
        """
        return self.status

    def __del__(self):
        """析构函数, 确保资源被释放"""
        try:
            self.stop()
            self.mixer.quit()
        except Exception:
            pass
