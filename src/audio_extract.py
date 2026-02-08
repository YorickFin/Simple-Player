import os
from typing import Optional, Dict
from dataclasses import dataclass
from pathlib import Path

try:
    from mutagen import File
    from mutagen.mp3 import MP3
    from mutagen.flac import FLAC
    from mutagen.mp4 import MP4
    from mutagen.oggvorbis import OggVorbis
    from mutagen.oggopus import OggOpus
    from mutagen.asf import ASF
    from mutagen.id3 import ID3, APIC
except ImportError:
    raise ImportError("请先安装mutagen: pip install mutagen")


@dataclass
class AudioInfo:
    """音频信息数据类"""
    filepath: str
    duration: float  # 时长（秒）
    bitrate: int  # 比特率（kbps）
    sample_rate: int  # 采样率（Hz）
    channels: int  # 声道数
    has_cover: bool  # 是否有封面
    format: str  # 文件格式
    cover_data: Optional[bytes] = None  # 封面图片数据
    cover_mime_type: Optional[str] = None  # 封面MIME类型
    title: Optional[str] = None  # 标题
    artist: Optional[str] = None  # 艺术家
    album: Optional[str] = None  # 专辑
    lyrics: Optional[str] = None  # 歌词


class AudioExtractor:
    """音频元数据提取器"""

    # 支持的音频格式
    SUPPORTED_FORMATS = {
        '.mp3': 'MP3',
        '.flac': 'FLAC',
        '.ogg': 'OGG',
        '.opus': 'Opus',
        '.wma': 'WMA',
        '.wav': 'WAV',
        '.aiff': 'AIFF',
    }

    def __init__(self):
        self._file_handlers = {
            'mp3': self._extract_mp3,
            'flac': self._extract_flac,
            'm4a': self._extract_mp4,
            'ogg': self._extract_ogg,
            'opus': self._extract_opus,
            'wma': self._extract_asf,
        }

    def extract(self, filepath: str, extract_cover: bool = True) -> AudioInfo:
        """
        提取音频文件的元数据

        Args:
            filepath: 音频文件路径
            extract_cover: 是否提取封面

        Returns:
            AudioInfo对象
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"文件不存在: {filepath}")

        # 获取文件扩展名
        ext = Path(filepath).suffix.lower()

        # 检查是否支持该格式
        if ext not in self.SUPPORTED_FORMATS:
            raise ValueError(f"不支持的文件格式: {ext}。支持格式: {list(self.SUPPORTED_FORMATS.keys())}")

        # 根据扩展名选择处理方法
        handler_key = ext.lstrip('.').lower()
        if handler_key in self._file_handlers:
            return self._file_handlers[handler_key](filepath, extract_cover)
        else:
            # 默认处理方式
            return self._extract_generic(filepath, extract_cover)

    def _extract_mp3(self, filepath: str, extract_cover: bool) -> AudioInfo:
        """提取MP3文件信息"""
        try:
            audio = MP3(filepath)
        except Exception:
            # 如果MP3解析失败, 尝试使用通用的ID3
            audio = ID3(filepath)
            info = File(filepath)
            duration = info.info.length if hasattr(info, 'info') else 0
            bitrate = info.info.bitrate if hasattr(info, 'info') else 0
            sample_rate = info.info.sample_rate if hasattr(info, 'info') else 0
        else:
            duration = audio.info.length
            bitrate = audio.info.bitrate
            sample_rate = audio.info.sample_rate

        # 提取基本信息
        channels = getattr(audio.info, 'channels', 2)

        # 提取封面
        cover_data = None
        cover_mime_type = None
        has_cover = False

        if extract_cover and hasattr(audio, 'tags'):
            for tag in audio.tags.values():
                if isinstance(tag, APIC):
                    cover_data = tag.data
                    cover_mime_type = tag.mime
                    has_cover = True
                    break

        # 提取元数据
        title = self._get_tag(audio, 'TIT2', 'title')
        artist = self._get_tag(audio, 'TPE1', 'artist')
        album = self._get_tag(audio, 'TALB', 'album')
        lyrics = self._get_lyrics_mp3(audio)

        return AudioInfo(
            filepath=filepath,
            duration=duration,
            bitrate=bitrate // 1000 if bitrate else 0,
            sample_rate=sample_rate,
            channels=channels,
            has_cover=has_cover,
            format='MP3',
            cover_data=cover_data,
            cover_mime_type=cover_mime_type,
            title=title,
            artist=artist,
            album=album,
            lyrics=lyrics
        )

    def _extract_flac(self, filepath: str, extract_cover: bool) -> AudioInfo:
        """提取FLAC文件信息"""
        audio = FLAC(filepath)

        # 提取音频信息
        duration = audio.info.length
        bitrate = audio.info.bitrate
        sample_rate = audio.info.sample_rate
        channels = audio.info.channels

        # 提取封面
        cover_data = None
        cover_mime_type = None
        has_cover = False

        if extract_cover:
            for picture in audio.pictures:
                if picture.type == 3:  # 3 表示封面图片
                    cover_data = picture.data
                    cover_mime_type = picture.mime
                    has_cover = True
                    break

        # 提取元数据
        title = self._get_tag(audio, 'TITLE', 'title')
        artist = self._get_tag(audio, 'ARTIST', 'artist')
        album = self._get_tag(audio, 'ALBUM', 'album')
        lyrics = self._get_tag(audio, 'LYRICS', 'UNSYNCEDLYRICS')

        return AudioInfo(
            filepath=filepath,
            duration=duration,
            bitrate=bitrate // 1000 if bitrate else 0,
            sample_rate=sample_rate,
            channels=channels,
            has_cover=has_cover,
            format='FLAC',
            cover_data=cover_data,
            cover_mime_type=cover_mime_type,
            title=title,
            artist=artist,
            album=album,
            lyrics=lyrics
        )

    def _extract_mp4(self, filepath: str, extract_cover: bool) -> AudioInfo:
        """提取MP4/AAC文件信息"""
        audio = MP4(filepath)

        # 提取音频信息
        duration = audio.info.length
        bitrate = audio.info.bitrate
        sample_rate = audio.info.sample_rate
        channels = audio.info.channels

        # 提取封面
        cover_data = None
        cover_mime_type = None
        has_cover = False

        if extract_cover and 'covr' in audio:
            cover_data = audio['covr'][0]
            cover_mime_type = 'image/jpeg'  # MP4封面通常是JPEG
            has_cover = True

        # 提取元数据
        title = self._get_tag(audio, '\xa9nam', 'title')
        artist = self._get_tag(audio, '\xa9ART', 'artist')
        album = self._get_tag(audio, '\xa9alb', 'album')
        lyrics = self._get_tag(audio, '\xa9lyr')

        return AudioInfo(
            filepath=filepath,
            duration=duration,
            bitrate=bitrate // 1000 if bitrate else 0,
            sample_rate=sample_rate,
            channels=channels,
            has_cover=has_cover,
            format='MP4/AAC',
            cover_data=cover_data,
            cover_mime_type=cover_mime_type,
            title=title,
            artist=artist,
            album=album,
            lyrics=lyrics
        )

    def _extract_ogg(self, filepath: str, extract_cover: bool) -> AudioInfo:
        """提取OGG Vorbis文件信息"""
        audio = OggVorbis(filepath)
        return self._extract_ogg_common(audio, filepath, extract_cover, 'OGG Vorbis')

    def _extract_opus(self, filepath: str, extract_cover: bool) -> AudioInfo:
        """提取Opus文件信息"""
        audio = OggOpus(filepath)
        return self._extract_ogg_common(audio, filepath, extract_cover, 'Opus')

    def _extract_ogg_common(self, audio, filepath: str, extract_cover: bool, format_name: str) -> AudioInfo:
        """提取OGG格式通用信息"""
        duration = audio.info.length
        bitrate = audio.info.bitrate
        sample_rate = audio.info.sample_rate
        channels = audio.info.channels

        # OGG格式通常不直接嵌入封面, 而是通过元数据引用
        cover_data = None
        cover_mime_type = None
        has_cover = False

        # 提取元数据
        title = self._get_tag(audio, 'TITLE', 'title')
        artist = self._get_tag(audio, 'ARTIST', 'artist')
        album = self._get_tag(audio, 'ALBUM', 'album')
        lyrics = self._get_tag(audio, 'LYRICS')

        # 检查是否有封面URL
        if 'METADATA_BLOCK_PICTURE' in audio or 'COVERART' in audio:
            has_cover = True

        return AudioInfo(
            filepath=filepath,
            duration=duration,
            bitrate=bitrate // 1000 if bitrate else 0,
            sample_rate=sample_rate,
            channels=channels,
            has_cover=has_cover,
            format=format_name,
            cover_data=cover_data,
            cover_mime_type=cover_mime_type,
            title=title,
            artist=artist,
            album=album,
            lyrics=lyrics
        )

    def _extract_asf(self, filepath: str, extract_cover: bool) -> AudioInfo:
        """提取WMA文件信息"""
        audio = ASF(filepath)

        duration = audio.info.length
        bitrate = audio.info.bitrate
        sample_rate = audio.info.sample_rate
        channels = audio.info.channels

        # 提取封面
        cover_data = None
        cover_mime_type = None
        has_cover = False

        if extract_cover and 'WM/Picture' in audio:
            for picture in audio['WM/Picture']:
                cover_data = picture.value
                cover_mime_type = picture.mime
                has_cover = True
                break

        # 提取元数据
        title = self._get_tag(audio, 'Title', 'title')
        artist = self._get_tag(audio, 'Author', 'artist')
        album = self._get_tag(audio, 'WM/AlbumTitle', 'album')
        lyrics = self._get_tag(audio, 'WM/Lyrics', 'Lyrics')

        return AudioInfo(
            filepath=filepath,
            duration=duration,
            bitrate=bitrate // 1000 if bitrate else 0,
            sample_rate=sample_rate,
            channels=channels,
            has_cover=has_cover,
            format='WMA',
            cover_data=cover_data,
            cover_mime_type=cover_mime_type,
            title=title,
            artist=artist,
            album=album,
            lyrics=lyrics
        )

    def _extract_generic(self, filepath: str, extract_cover: bool) -> AudioInfo:
        """通用音频文件信息提取"""
        audio = File(filepath)

        # 尝试获取音频信息
        duration = getattr(audio.info, 'length', 0) if audio.info else 0
        bitrate = getattr(audio.info, 'bitrate', 0) if audio.info else 0
        sample_rate = getattr(audio.info, 'sample_rate', 0) if audio.info else 0
        channels = getattr(audio.info, 'channels', 2) if audio.info else 2

        # 获取格式信息
        mime_type = getattr(audio, 'mime', [''])[0] if hasattr(audio, 'mime') else ''
        format_name = mime_type.split('/')[-1].upper() if mime_type else 'Unknown'

        return AudioInfo(
            filepath=filepath,
            duration=duration,
            bitrate=bitrate // 1000 if bitrate else 0,
            sample_rate=sample_rate,
            channels=channels,
            has_cover=False,  # 通用方法不提取封面
            format=format_name,
            cover_data=None,
            cover_mime_type=None,
            title=None,
            artist=None,
            album=None
        )

    def _get_lyrics_mp3(self, audio) -> Optional[str]:
        """提取MP3歌词"""
        if not hasattr(audio, 'tags') or audio.tags is None:
            return None

        for key, value in audio.tags.items():
            if key.startswith('USLT') or key.startswith('SYLT'):
                if hasattr(value, 'text'):
                    return value.text
        return None

    def _get_tag(self, audio, *possible_keys):
        """从音频文件中获取标签值"""
        if not hasattr(audio, 'tags') or audio.tags is None:
            return None

        for key in possible_keys:
            if key in audio.tags:
                value = audio.tags[key]
                if isinstance(value, list):
                    return str(value[0]) if value else None
                return str(value)
        return None

    def format_duration(self, duration: float) -> str:
        """格式化时长（秒）为 HH:MM:SS 格式"""
        hours = int(duration // 3600)
        minutes = int((duration % 3600) // 60)
        seconds = int(duration % 60)

        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            return f"{minutes:02d}:{seconds:02d}"

    def get_supported_formats(self) -> Dict[str, str]:
        """获取支持的音频格式"""
        return self.SUPPORTED_FORMATS.copy()


# 使用示例
if __name__ == "__main__":
    # 创建提取器实例
    extractor = AudioExtractor()

    # 示例文件列表（请替换为实际文件路径）
    sample_files = [
        r'E:\备份\音乐\日常\A-Lin - 给我一个理由忘记.mp3'
    ]

    for filepath in sample_files:
        if not os.path.exists(filepath):
            print(f"文件不存在, 跳过: {filepath}")
            continue

        try:
            # 提取音频信息（包含封面）
            audio_info = extractor.extract(filepath, extract_cover=True)

            print(f"文件路径: {audio_info.filepath}")
            print(f"格式: {audio_info.format}")
            print(f"时长: {audio_info.duration:.2f}秒 ({extractor.format_duration(audio_info.duration)})")
            print(f"比特率: {audio_info.bitrate} kbps")
            print(f"采样率: {audio_info.sample_rate} Hz")
            print(f"声道数: {audio_info.channels}")
            print(f"是否有封面: {'是' if audio_info.has_cover else '否'}")
            print(f"标题: {audio_info.title or '未知'}")
            print(f"艺术家: {audio_info.artist or '未知'}")
            print(f"专辑: {audio_info.album or '未知'}")
            print(f"歌词: {'有' if audio_info.lyrics else '无'}")
            if audio_info.lyrics:
                print(f"歌词预览: {audio_info.lyrics[:100]}..." if len(audio_info.lyrics) > 100 else f"歌词: {audio_info.lyrics}")

        except Exception as e:
            print(f"处理文件时出错 {filepath}: {e}")