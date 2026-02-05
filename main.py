import sys
import logging
from pathlib import Path
from datetime import datetime
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from res.signal_manager import SignalManager, SlotManager

def setup_logging():
    """
    配置日志系统
    """
    # 配置日志
    date_format = '%Y_%m_%d__%H_%M_%S'
    log_format = '%(asctime)s - %(levelname)s - %(message)s'

    # 创建logs目录
    path = Path('logging')
    path.mkdir(parents=True, exist_ok=True)

    # 只保留最近的5个日志文件
    for log_file in path.glob('*.log'):
        if len(list(path.glob('*.log'))) > 4:
            log_file.unlink()

    # 设置日志文件名
    log_filename = path / f'{datetime.now().strftime(date_format)}.log'

    # 配置日志系统
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.FileHandler(log_filename, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(__name__)

if __name__ == "__main__":
    # 初始化日志系统
    logger = setup_logging()

    # 初始化信号槽管理器
    signal_manager = SignalManager()
    slot_manager = SlotManager(logger)
    signal_manager.dict_signal.connect(slot_manager.handle_signal)

    # 初始化应用程序
    app = QApplication()
    # 设置logo
    app.setWindowIcon(QIcon(r'res\logo\logo_P.png'))
    # 设置关闭最后一个窗口也不退出程序
    QApplication.setQuitOnLastWindowClosed(False)
    signal_manager.send_signal({'action': '打开窗口', 'info': '打开主窗口', 'signal_manager': signal_manager, 'logger': logger})
    signal_manager.send_signal({'action': '创建托盘'})
    sys.exit(app.exec())



