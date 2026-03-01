# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1200, 700)
        Form.setStyleSheet(u"*\n"
"{\n"
"	font: 10pt \"\u6977\u4f53\";\n"
"	font-size: 13pt;\n"
"	color: white;\n"
"}\n"
"\n"
"\n"
"/************************************ QWidget  ************************************/\n"
"\n"
"QWidget\n"
"{\n"
"	background-color: #1F2430;\n"
"}\n"
"\n"
"\n"
"/************************************ QPushButton  ************************************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QPushButton\n"
"{\n"
"	background-color: transparent;\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"/*\u60ac\u505c*/\n"
"QPushButton:hover\n"
"{\n"
"	color: #2196F3;\n"
"}\n"
"\n"
"/*\u6309\u4e0b*/\n"
"QPushButton:pressed\n"
"{\n"
"	padding-bottom: -2px;\n"
"	padding-left: 1px\n"
"}\n"
"\n"
"QPushButton#fontColorPButton,\n"
"QPushButton#strokeColorPButton\n"
"{\n"
"	background-color: transparent;\n"
"	border: 1px solid #FFFFFF;\n"
"}\n"
"\n"
"QPushButton#fontColorPButton:hover,\n"
"QPushButton#strokeColorPButton:hover\n"
"{\n"
"	border: 1px solid #2196F3;\n"
"}\n"
"\n"
"/************************************ QLabel  **************************"
                        "**********/\n"
"\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/************************************ QMessageBox  ************************************/\n"
"\n"
"QMessageBox\n"
"{\n"
"	background-color: #1F2430;\n"
"}\n"
"\n"
"QMessageBox QLabel\n"
"{\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QMessageBox QPushButton\n"
"{\n"
"	background-color: #3B4252;\n"
"	color: #FFFFFF;\n"
"	border: 1px solid #4C566A;\n"
"	border-radius: 4px;\n"
"	padding: 6px 16px;\n"
"	min-width: 60px;\n"
"}\n"
"\n"
"QMessageBox QPushButton:hover\n"
"{\n"
"	background-color: #4C566A;\n"
"}\n"
"\n"
"\n"
"/************************************ QScrollArea  ************************************/\n"
"QScrollArea\n"
"{\n"
"	background-color: transparent;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QScrollArea > QWidget > QWidget\n"
"{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/************************************ QLineEdit  ************************************/\n"
"\n"
"QLineEdit\n"
""
                        "{\n"
"	font: 10pt \"\u5b8b\u4f53\";\n"
"	font-size: 13pt;\n"
"	background-color: transparent;\n"
"	border: 1px solid #FFFFFF;\n"
"}\n"
"\n"
"QLineEdit::hover\n"
"{\n"
"	border: 1px solid #2196F3;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"	border: 1px solid #2196F3;\n"
"}\n"
"\n"
"/************************************ QComboBox  ************************************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QComboBox\n"
"{\n"
"	background-color: transparent;\n"
"	border: 1px solid #FFFFFF;\n"
"}\n"
"\n"
"/*\u9009\u9879\u6837\u5f0f*/\n"
"QComboBox QListView::item {\n"
"	margin: 10px;\n"
"	height: 10px;\n"
"}\n"
"\n"
"/*\u4e0b\u62c9\u9009\u9879\u6837\u5f0f*/\n"
"QComboBox QAbstractItemView\n"
"{\n"
"	background-color:#232936;\n"
"}\n"
"\n"
"/*\u60ac\u505c*/\n"
"QComboBox::hover\n"
"{\n"
"	border: 1px solid #2196F3;\n"
"}\n"
"\n"
"\n"
"/************************************ QListWidget  ************************************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QListWidget\n"
"{\n"
"	background-color: transparent;\n"
"	border-radius: 0"
                        "px;\n"
"	outline: 0px;\n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"/*\u9879\u76ee*/\n"
"QListWidget::item\n"
"{\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	margin-top: 5px;\n"
"	margin-bottom: 5px;\n"
"	margin-left: 5px;\n"
"	margin-right: 5px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/*\u60ac\u505c*/\n"
"QListWidget::item:hover\n"
"{\n"
"	background-color: rgba(91, 132, 176, 170);\n"
"	color: #2196F3;\n"
"}\n"
"\n"
"/*\u9009\u4e2d*/\n"
"QListWidget::item:selected\n"
"{\n"
"    background-color: rgba(91, 132, 176, 170);\n"
"}\n"
"\n"
"/*\u79bb\u5f00*/\n"
"QListWidget::item:selected:!active\n"
"{\n"
"	color: white;\n"
"}\n"
"\n"
"\n"
"/************************************ QTabWidget  ************************************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QTabWidget\n"
"{\n"
"	background-color: #2F3648;\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane\n"
"{\n"
"	border-top: 0px solid;\n"
"	padding-top: -20px;\n"
"	margin-top: 0px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar\n"
"{\n"
"    left: 0px;\n"
"}\n"
"\n"
"QTabBar::tab\n"
"{\n"
""
                        "    color: white;\n"
"    border: 0px solid;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    min-height: 0px;\n"
"    color: white;\n"
"    border: 0px solid;\n"
"    border-bottom: 0px solid;\n"
"}\n"
"\n"
"\n"
"/************************************ QTableView ************************************/\n"
"\n"
"/* \u9690\u85cf\u5355\u5143\u683c\u7ebf\u6846 */\n"
"QTableView\n"
"{\n"
"	selection-background-color: rgba(91, 132, 176, 170);\n"
"    selection-color: white;\n"
"    background-color: transparent;\n"
"	gridline-color: transparent;\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* \u9690\u85cf\u8868\u683c\u5185\u5bb9\u533a\u57df\u7684\u8fb9\u6846 */\n"
"QTableView::item\n"
"{\n"
"    border: none;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* \u786e\u4fdd\u9009\u4e2d\u72b6\u6001\u4e5f\u6ca1\u6709\u8fb9\u6846\u548c\u5206\u9694 */\n"
"QTableView::item:selected\n"
"{\n"
"    border: none;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
""
                        "    outline: none;\n"
"}\n"
"\n"
"/* \u786e\u4fdd\u9009\u4e2d\u884c\u6ca1\u6709\u5185\u90e8\u5206\u9694 */\n"
"QTableView::item:selected\n"
"{\n"
"    border-left: none;\n"
"    border-right: none;\n"
"    border-top: none;\n"
"    border-bottom: none;\n"
"}\n"
"\n"
"/* \u53bb\u9664\u7126\u70b9\u6307\u793a\u5668 */\n"
"QTableView:focus\n"
"{\n"
"    outline: none;\n"
"}\n"
"\n"
"QTableView::item:focus\n"
"{\n"
"    outline: none;\n"
"}\n"
"\n"
"\n"
"/************************************ QRadioButton  ************************************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QRadioButton#winMiniRButton::indicator:checked\n"
"{\n"
"	border-image: url(:/min/img/mini.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"QRadioButton#winMiniRButton::indicator:unchecked\n"
"{\n"
"	border-image: url(:/min/img/mini.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"/*\u60ac\u505c*/\n"
"QRadioButton#winMiniRButton::indicator:checked:hover\n"
"{\n"
"	border-image: url(:/min/img/minis.png);\n"
"	width: 15px;\n"
"	hei"
                        "ght: 15px;\n"
"}\n"
"QRadioButton#winMiniRButton::indicator:unchecked:hover\n"
"{\n"
"	border-image: url(:/min/img/minis.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"QRadioButton#winMiniRButton:pressed\n"
"{\n"
"	padding-bottom: -2px;\n"
"	padding-left: 1px\n"
"}\n"
"\n"
"/************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QRadioButton#winMaxRButton::indicator:checked\n"
"{\n"
"	border-image: url(:/nmax/img/nmax.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"QRadioButton#winMaxRButton::indicator:unchecked\n"
"{\n"
"	border-image: url(:/max/img/max.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"/*\u60ac\u505c*/\n"
"QRadioButton#winMaxRButton::indicator:checked:hover\n"
"{\n"
"	border-image: url(:/nmax/img/nmaxs.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton#winMaxRButton::indicator:unchecked:hover\n"
"{\n"
"	border-image: url(:/max/img/maxs.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"QRadioButton#winMaxRButton:pressed\n"
"{\n"
"	padding-bottom: -2px;\n"
""
                        "	padding-left: 1px\n"
"}\n"
"\n"
"/************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QRadioButton#winCloseRButton::indicator:checked\n"
"{\n"
"	border-image: url(:/close/img/close.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"QRadioButton#winCloseRButton::indicator:unchecked\n"
"{\n"
"	border-image: url(:/close/img/close.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"/*\u60ac\u505c*/\n"
"QRadioButton#winCloseRButton::indicator:checked:hover\n"
"{\n"
"	border-image: url(:/close/img/closes.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QRadioButton#winCloseRButton::indicator:unchecked:hover\n"
"{\n"
"	border-image: url(:/close/img/closes.png);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"\n"
"QRadioButton#winCloseRButton:pressed\n"
"{\n"
"	padding-bottom: -2px;\n"
"	padding-left: 1px\n"
"}\n"
"\n"
"/************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QRadioButton#playRButton1::indicator:checked,\n"
"QRadioButton#playRButton2::indicator:checked\n"
"{\n"
"	border-image: url(:/pause/img/pause.png);"
                        "\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"QRadioButton#playRButton1::indicator:unchecked,\n"
"QRadioButton#playRButton2::indicator:unchecked\n"
"{\n"
"	border-image: url(:/play/img/play.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"/*\u60ac\u505c*/\n"
"QRadioButton#playRButton1::indicator:checked:hover,\n"
"QRadioButton#playRButton2::indicator:checked:hover\n"
"{\n"
"	border-image: url(:/pause/img/pauses.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"QRadioButton#playRButton1::indicator:unchecked:hover,\n"
"QRadioButton#playRButton2::indicator:unchecked:hover\n"
"{\n"
"	border-image: url(:/play/img/plays.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"QRadioButton#playRButton1:pressed,\n"
"QRadioButton#playRButton2:pressed\n"
"{\n"
"	padding-bottom: -2px;\n"
"	padding-left: 1px\n"
"}\n"
"\n"
"/************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QRadioButton#pgupRButton1::indicator:checked,\n"
"QRadioButton#pgupRButton2::indicator:checked\n"
"{\n"
"	border-image: url(:/pgup/img/pg"
                        "up.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"QRadioButton#pgupRButton1::indicator:unchecked,\n"
"QRadioButton#pgupRButton2::indicator:unchecked\n"
"{\n"
"	border-image: url(:/pgup/img/pgup.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"/*\u60ac\u505c*/\n"
"QRadioButton#pgupRButton1::indicator:checked:hover,\n"
"QRadioButton#pgupRButton2::indicator:checked:hover\n"
"{\n"
"	border-image: url(:/pgup/img/pgups.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"QRadioButton#pgupRButton1::indicator:unchecked:hover,\n"
"QRadioButton#pgupRButton2::indicator:unchecked:hover\n"
"{\n"
"	border-image: url(:/pgup/img/pgups.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"QRadioButton#pgupRButton1:pressed,\n"
"QRadioButton#pgupRButton2:pressed\n"
"{\n"
"	padding-bottom: -2px;\n"
"	padding-left: 1px\n"
"}\n"
"\n"
"/************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QRadioButton#pgdnRButton1::indicator:checked,\n"
"QRadioButton#pgdnRButton2::indicator:checked\n"
"{\n"
"	border-image: url(:/pgdn/"
                        "img/pgdn.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"QRadioButton#pgdnRButton1::indicator:unchecked,\n"
"QRadioButton#pgdnRButton2::indicator:unchecked\n"
"{\n"
"	border-image: url(:/pgdn/img/pgdn.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"/*\u60ac\u505c*/\n"
"QRadioButton#pgdnRButton1::indicator:checked:hover,\n"
"QRadioButton#pgdnRButton2::indicator:checked:hover\n"
"{\n"
"	border-image: url(:/pgdn/img/pgdns.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"QRadioButton#pgdnRButton1::indicator:unchecked:hover,\n"
"QRadioButton#pgdnRButton2::indicator:unchecked:hover\n"
"{\n"
"	border-image: url(:/pgdn/img/pgdns.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"QRadioButton#pgdnRButton1:pressed,\n"
"QRadioButton#pgdnRButton2:pressed\n"
"{\n"
"	padding-bottom: -2px;\n"
"	padding-left: 1px\n"
"}\n"
"\n"
"/************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QRadioButton#volumeControlRButton1::indicator:checked,\n"
"QRadioButton#volumeControlRButton2::indicator:checked\n"
"{\n"
"	b"
                        "order-image: url(:/volume/img/volume.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"QRadioButton#volumeControlRButton1::indicator:unchecked,\n"
"QRadioButton#volumeControlRButton2::indicator:unchecked\n"
"{\n"
"	border-image: url(:/volume/img/volume.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"/*\u60ac\u505c*/\n"
"QRadioButton#volumeControlRButton1::indicator:checked:hover,\n"
"QRadioButton#volumeControlRButton2::indicator:checked:hover\n"
"{\n"
"	border-image: url(:/volume/img/volumes.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"QRadioButton#volumeControlRButton1::indicator:unchecked:hover,\n"
"QRadioButton#volumeControlRButton2::indicator:unchecked:hover\n"
"{\n"
"	border-image: url(:/volume/img/volumes.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"QRadioButton#volumeControlRButton1:pressed,\n"
"QRadioButton#volumeControlRButton2:pressed\n"
"{\n"
"	padding-bottom: -2px;\n"
"	padding-left: 1px\n"
"}\n"
"\n"
"/************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QRadioButton#"
                        "desktopLyricsRButton1::indicator:checked,\n"
"QRadioButton#desktopLyricsRButton1::indicator:checked\n"
"{\n"
"	border-image: url(:/close_desktop_lyrics/img/close_desktop_lyrics.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"QRadioButton#desktopLyricsRButton1::indicator:unchecked,\n"
"QRadioButton#desktopLyricsRButton2::indicator:unchecked\n"
"{\n"
"	border-image: url(:/open_desktop_lyrics/img/open_desktop_lyrics.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"/*\u60ac\u505c*/\n"
"QRadioButton#desktopLyricsRButton1::indicator:checked:hover,\n"
"QRadioButton#desktopLyricsRButton2::indicator:checked:hover\n"
"{\n"
"	border-image: url(:/close_desktop_lyrics/img/close_desktop_lyricss.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"QRadioButton#desktopLyricsRButton1::indicator:unchecked:hover,\n"
"QRadioButton#desktopLyricsRButton2::indicator:unchecked:hover\n"
"{\n"
"	border-image: url(:/open_desktop_lyrics/img/open_desktop_lyricss.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
""
                        "QRadioButton#desktopLyricsRButton1:pressed,\n"
"QRadioButton#desktopLyricsRButton2:pressed\n"
"{\n"
"	padding-bottom: -2px;\n"
"	padding-left: 1px\n"
"}\n"
"\n"
"\n"
"/************************************ QSlider ************************************/\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #82d7dc;\n"
"    border: 1px solid #82d7dc;\n"
"    width: 10px;\n"
"    margin: -5px -0.5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid;\n"
"    height: 3px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #67779e;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #dc82d7;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: #82d7dc;\n"
"    border: 1px solid #82d7dc;\n"
"    height: 10px;  /* \u5c06width\u6539\u4e3aheight */\n"
"    margin: -0.5px -5px;  /* \u8c03\u6574margin\u987a\u5e8f */\n"
"    border-radius: 5px;\n"
"}\n"
""
                        "\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid;\n"
"    width: 3px;  /* \u5c06height\u6539\u4e3awidth */\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: #dc82d7;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #67779e;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"/************************************ QScrollBar  ************************************/\n"
"\n"
"/*\u6eda\u52a8\u6761\u8fb9\u6846*/\n"
"QScrollBar\n"
"{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"/*\u6eda\u52a8\u6761*/\n"
"QScrollBar::handle\n"
"{\n"
"	border-radius: 3px;\n"
"    background: rgba(91, 132, 176, 170);\n"
"    margin-left: 1px;\n"
"    margin-right: 1px;\n"
"}\n"
"\n"
"/*\u6eda\u52a8\u6761\u9f20\u6807\u60ac\u505c*/\n"
"QScrollBar::handle:hover\n"
"{\n"
"    background: rgba(108, 156, 207, 170);\n"
"}\n"
"\n"
"/*\u4e0b\u65b9\u7bad\u5934*/\n"
"QScrollBar::add-line\n"
"{\n"
"    height: 0px;\n"
"	width: 0px;\n"
"}\n"
"\n"
"/*\u4e0a\u65b9"
                        "\u7bad\u5934*/\n"
"QScrollBar::sub-line\n"
"{\n"
"    height: 0px;\n"
"	width: 0px;\n"
"}\n"
"\n"
"/*\u6ed1\u5757\u5df2\u7ecf\u7ecf\u8fc7\u7684\u6ed1\u8f68\u533a\u57df\u7684\u989c\u8272*/\n"
"QScrollBar::add-page:vertical\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/*\u6ed1\u5757\u8fd8\u6ca1\u7ecf\u8fc7\u7684\u6ed1\u8f68\u533a\u57df\u7684\u989c\u8272*/\n"
"QScrollBar::sub-page\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/************************************ QMenu  ************************************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QMenu\n"
"{\n"
"	background-color: #2F3648;\n"
"	color: white;\n"
"	border: 1px solid #000000;\n"
"}\n"
"\n"
"/*\u5b50\u9879*/\n"
"QMenu::item\n"
"{\n"
"	height: 20px;\n"
"	margin: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"/*\u60ac\u6d6e\u5b50\u9879*/\n"
"QMenu::item:selected\n"
"{\n"
"	color: #2196F3;\n"
"	padding-bottom: -1px;\n"
"	padding-left: 1px\n"
"}")
        self.FormLayout = QHBoxLayout(Form)
        self.FormLayout.setObjectName(u"FormLayout")
        self.background = QTabWidget(Form)
        self.background.setObjectName(u"background")
        self.mainTab = QWidget()
        self.mainTab.setObjectName(u"mainTab")
        self.verticalLayout_3 = QVBoxLayout(self.mainTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 3, 0, 0)
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setSpacing(0)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.icon = QLabel(self.mainTab)
        self.icon.setObjectName(u"icon")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setMinimumSize(QSize(0, 0))
        self.icon.setMaximumSize(QSize(26, 26))
        self.icon.setSizeIncrement(QSize(0, 0))
        self.icon.setScaledContents(True)

        self.horizontalLayout_1.addWidget(self.icon)

        self.horizontalSpacer_8 = QSpacerItem(10, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_1.addItem(self.horizontalSpacer_8)

        self.label = QLabel(self.mainTab)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_1.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_1.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.winMiniRButton = QRadioButton(self.mainTab)
        self.RButtonGroup = QButtonGroup(Form)
        self.RButtonGroup.setObjectName(u"RButtonGroup")
        self.RButtonGroup.setExclusive(False)
        self.RButtonGroup.addButton(self.winMiniRButton)
        self.winMiniRButton.setObjectName(u"winMiniRButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.winMiniRButton.sizePolicy().hasHeightForWidth())
        self.winMiniRButton.setSizePolicy(sizePolicy2)
        self.winMiniRButton.setMinimumSize(QSize(26, 26))
        self.winMiniRButton.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_2.addWidget(self.winMiniRButton)

        self.winMaxRButton = QRadioButton(self.mainTab)
        self.RButtonGroup.addButton(self.winMaxRButton)
        self.winMaxRButton.setObjectName(u"winMaxRButton")
        sizePolicy2.setHeightForWidth(self.winMaxRButton.sizePolicy().hasHeightForWidth())
        self.winMaxRButton.setSizePolicy(sizePolicy2)
        self.winMaxRButton.setMinimumSize(QSize(26, 26))
        self.winMaxRButton.setMaximumSize(QSize(16777215, 21))
        self.winMaxRButton.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.winMaxRButton)

        self.winCloseRButton = QRadioButton(self.mainTab)
        self.RButtonGroup.addButton(self.winCloseRButton)
        self.winCloseRButton.setObjectName(u"winCloseRButton")
        sizePolicy2.setHeightForWidth(self.winCloseRButton.sizePolicy().hasHeightForWidth())
        self.winCloseRButton.setSizePolicy(sizePolicy2)
        self.winCloseRButton.setMinimumSize(QSize(26, 26))
        self.winCloseRButton.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_2.addWidget(self.winCloseRButton)


        self.horizontalLayout_1.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_1)

        self.verticalSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menuListWidget = QListWidget(self.mainTab)
        QListWidgetItem(self.menuListWidget)
        QListWidgetItem(self.menuListWidget)
        QListWidgetItem(self.menuListWidget)
        self.menuListWidget.setObjectName(u"menuListWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.menuListWidget.sizePolicy().hasHeightForWidth())
        self.menuListWidget.setSizePolicy(sizePolicy3)
        self.menuListWidget.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.menuListWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.subTabWidget = QTabWidget(self.mainTab)
        self.subTabWidget.setObjectName(u"subTabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_8 = QHBoxLayout(self.tab)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 4, 0, 0)
        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout_8.addWidget(self.tableView)

        self.subTabWidget.addTab(self.tab, "")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_4 = QVBoxLayout(self.tab_1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 3, 0, 0)
        self.folderListWidget = QListWidget(self.tab_1)
        QListWidgetItem(self.folderListWidget)
        self.folderListWidget.setObjectName(u"folderListWidget")
        self.folderListWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.verticalLayout_4.addWidget(self.folderListWidget)

        self.subTabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout = QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 4, 0, 0)
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 961, 1000))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 1000))
        self.horizontalLayout_12 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_18 = QSpacerItem(302, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_18)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 5)
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_6.addWidget(self.label_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.label_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 30, -1, 5)
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_10.addWidget(self.label_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)
        self.label_5.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.label_5)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.label_7)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)
        self.label_9.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.label_9)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)
        self.label_10.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.label_10)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)
        self.label_12.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.label_12)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)
        self.label_11.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.label_11)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 30, -1, 5)
        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        sizePolicy4.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy4)
        self.label_13.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_20.addWidget(self.label_13)


        self.verticalLayout_5.addLayout(self.horizontalLayout_20)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        sizePolicy4.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy4)
        self.label_14.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.label_14)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        sizePolicy4.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy4)
        self.label_15.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.label_15)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        self.label_16.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.label_16)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)
        self.label_17.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.label_17)

        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")
        sizePolicy4.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy4)
        self.label_18.setMinimumSize(QSize(0, 26))

        self.verticalLayout_5.addWidget(self.label_18)


        self.horizontalLayout_11.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, -1, -1, 5)
        self.label_21 = QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName(u"label_21")
        sizePolicy4.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy4)
        self.label_21.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_23.addWidget(self.label_21)


        self.verticalLayout_6.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.minTrayRButton = QRadioButton(self.scrollAreaWidgetContents)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.minTrayRButton)
        self.minTrayRButton.setObjectName(u"minTrayRButton")
        sizePolicy4.setHeightForWidth(self.minTrayRButton.sizePolicy().hasHeightForWidth())
        self.minTrayRButton.setSizePolicy(sizePolicy4)
        self.minTrayRButton.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_9.addWidget(self.minTrayRButton)

        self.quitRButton = QRadioButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.quitRButton)
        self.quitRButton.setObjectName(u"quitRButton")
        sizePolicy4.setHeightForWidth(self.quitRButton.sizePolicy().hasHeightForWidth())
        self.quitRButton.setSizePolicy(sizePolicy4)
        self.quitRButton.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_9.addWidget(self.quitRButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 30, -1, 5)
        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")
        sizePolicy4.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy4)
        self.label_20.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_22.addWidget(self.label_20)


        self.verticalLayout_6.addLayout(self.horizontalLayout_22)

        self.fontCBox = QComboBox(self.scrollAreaWidgetContents)
        self.fontCBox.setObjectName(u"fontCBox")
        sizePolicy4.setHeightForWidth(self.fontCBox.sizePolicy().hasHeightForWidth())
        self.fontCBox.setSizePolicy(sizePolicy4)
        self.fontCBox.setMinimumSize(QSize(0, 26))

        self.verticalLayout_6.addWidget(self.fontCBox)

        self.fontSizeLEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.fontSizeLEdit.setObjectName(u"fontSizeLEdit")
        sizePolicy1.setHeightForWidth(self.fontSizeLEdit.sizePolicy().hasHeightForWidth())
        self.fontSizeLEdit.setSizePolicy(sizePolicy1)
        self.fontSizeLEdit.setMinimumSize(QSize(0, 26))
        self.fontSizeLEdit.setMaximumSize(QSize(26, 16777215))

        self.verticalLayout_6.addWidget(self.fontSizeLEdit)

        self.fontColorPButton = QPushButton(self.scrollAreaWidgetContents)
        self.fontColorPButton.setObjectName(u"fontColorPButton")
        sizePolicy1.setHeightForWidth(self.fontColorPButton.sizePolicy().hasHeightForWidth())
        self.fontColorPButton.setSizePolicy(sizePolicy1)
        self.fontColorPButton.setMinimumSize(QSize(0, 26))
        self.fontColorPButton.setMaximumSize(QSize(26, 16777215))

        self.verticalLayout_6.addWidget(self.fontColorPButton)

        self.strokeSizeLEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.strokeSizeLEdit.setObjectName(u"strokeSizeLEdit")
        sizePolicy1.setHeightForWidth(self.strokeSizeLEdit.sizePolicy().hasHeightForWidth())
        self.strokeSizeLEdit.setSizePolicy(sizePolicy1)
        self.strokeSizeLEdit.setMinimumSize(QSize(0, 26))
        self.strokeSizeLEdit.setMaximumSize(QSize(26, 16777215))

        self.verticalLayout_6.addWidget(self.strokeSizeLEdit)

        self.strokeColorPButton = QPushButton(self.scrollAreaWidgetContents)
        self.strokeColorPButton.setObjectName(u"strokeColorPButton")
        sizePolicy1.setHeightForWidth(self.strokeColorPButton.sizePolicy().hasHeightForWidth())
        self.strokeColorPButton.setSizePolicy(sizePolicy1)
        self.strokeColorPButton.setMinimumSize(QSize(0, 26))
        self.strokeColorPButton.setMaximumSize(QSize(26, 16777215))

        self.verticalLayout_6.addWidget(self.strokeColorPButton)

        self.lyricPosLEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lyricPosLEdit.setObjectName(u"lyricPosLEdit")
        sizePolicy4.setHeightForWidth(self.lyricPosLEdit.sizePolicy().hasHeightForWidth())
        self.lyricPosLEdit.setSizePolicy(sizePolicy4)
        self.lyricPosLEdit.setMinimumSize(QSize(0, 26))

        self.verticalLayout_6.addWidget(self.lyricPosLEdit)

        self.lyricScalesLEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lyricScalesLEdit.setObjectName(u"lyricScalesLEdit")
        sizePolicy4.setHeightForWidth(self.lyricScalesLEdit.sizePolicy().hasHeightForWidth())
        self.lyricScalesLEdit.setSizePolicy(sizePolicy4)
        self.lyricScalesLEdit.setMinimumSize(QSize(0, 26))

        self.verticalLayout_6.addWidget(self.lyricScalesLEdit)

        self.lyricAlphaLEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lyricAlphaLEdit.setObjectName(u"lyricAlphaLEdit")
        sizePolicy4.setHeightForWidth(self.lyricAlphaLEdit.sizePolicy().hasHeightForWidth())
        self.lyricAlphaLEdit.setSizePolicy(sizePolicy4)
        self.lyricAlphaLEdit.setMinimumSize(QSize(0, 26))

        self.verticalLayout_6.addWidget(self.lyricAlphaLEdit)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 30, -1, 5)
        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")
        sizePolicy4.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy4)
        self.label_19.setMinimumSize(QSize(0, 26))

        self.horizontalLayout_21.addWidget(self.label_19)


        self.verticalLayout_6.addLayout(self.horizontalLayout_21)

        self.playPauseKeyLEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.playPauseKeyLEdit.setObjectName(u"playPauseKeyLEdit")
        sizePolicy4.setHeightForWidth(self.playPauseKeyLEdit.sizePolicy().hasHeightForWidth())
        self.playPauseKeyLEdit.setSizePolicy(sizePolicy4)
        self.playPauseKeyLEdit.setMinimumSize(QSize(0, 26))

        self.verticalLayout_6.addWidget(self.playPauseKeyLEdit)

        self.pgupKeyLEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.pgupKeyLEdit.setObjectName(u"pgupKeyLEdit")
        sizePolicy4.setHeightForWidth(self.pgupKeyLEdit.sizePolicy().hasHeightForWidth())
        self.pgupKeyLEdit.setSizePolicy(sizePolicy4)
        self.pgupKeyLEdit.setMinimumSize(QSize(0, 26))

        self.verticalLayout_6.addWidget(self.pgupKeyLEdit)

        self.pgdnKeyLEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.pgdnKeyLEdit.setObjectName(u"pgdnKeyLEdit")
        sizePolicy4.setHeightForWidth(self.pgdnKeyLEdit.sizePolicy().hasHeightForWidth())
        self.pgdnKeyLEdit.setSizePolicy(sizePolicy4)
        self.pgdnKeyLEdit.setMinimumSize(QSize(0, 26))

        self.verticalLayout_6.addWidget(self.pgdnKeyLEdit)

        self.volumeUpKeyLEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.volumeUpKeyLEdit.setObjectName(u"volumeUpKeyLEdit")
        sizePolicy4.setHeightForWidth(self.volumeUpKeyLEdit.sizePolicy().hasHeightForWidth())
        self.volumeUpKeyLEdit.setSizePolicy(sizePolicy4)
        self.volumeUpKeyLEdit.setMinimumSize(QSize(0, 26))

        self.verticalLayout_6.addWidget(self.volumeUpKeyLEdit)

        self.volumeDnKeyLEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.volumeDnKeyLEdit.setObjectName(u"volumeDnKeyLEdit")
        sizePolicy4.setHeightForWidth(self.volumeDnKeyLEdit.sizePolicy().hasHeightForWidth())
        self.volumeDnKeyLEdit.setSizePolicy(sizePolicy4)
        self.volumeDnKeyLEdit.setMinimumSize(QSize(0, 26))

        self.verticalLayout_6.addWidget(self.volumeDnKeyLEdit)


        self.horizontalLayout_11.addLayout(self.verticalLayout_6)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)

        self.horizontalSpacer_19 = QSpacerItem(302, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_19)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        self.subTabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.subTabWidget.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.subTabWidget)

        self.musicInfoBGFrame = QFrame(self.mainTab)
        self.musicInfoBGFrame.setObjectName(u"musicInfoBGFrame")
        self.musicInfoBGFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.musicInfoBGFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.musicInfoBGFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.musicLogoPButton = QPushButton(self.musicInfoBGFrame)
        self.musicLogoPButton.setObjectName(u"musicLogoPButton")
        sizePolicy1.setHeightForWidth(self.musicLogoPButton.sizePolicy().hasHeightForWidth())
        self.musicLogoPButton.setSizePolicy(sizePolicy1)
        self.musicLogoPButton.setMinimumSize(QSize(60, 60))
        self.musicLogoPButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_7.addWidget(self.musicLogoPButton)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer_6 = QSpacerItem(10, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.playSlider1 = QSlider(self.musicInfoBGFrame)
        self.playSlider1.setObjectName(u"playSlider1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.playSlider1.sizePolicy().hasHeightForWidth())
        self.playSlider1.setSizePolicy(sizePolicy5)
        self.playSlider1.setMinimum(0)
        self.playSlider1.setMaximum(9999)
        self.playSlider1.setSingleStep(1)
        self.playSlider1.setValue(20)
        self.playSlider1.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_5.addWidget(self.playSlider1)

        self.horizontalSpacer_7 = QSpacerItem(10, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.playSliderTxt1 = QLabel(self.musicInfoBGFrame)
        self.playSliderTxt1.setObjectName(u"playSliderTxt1")
        sizePolicy1.setHeightForWidth(self.playSliderTxt1.sizePolicy().hasHeightForWidth())
        self.playSliderTxt1.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.playSliderTxt1)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer_11 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)

        self.musicNameLabel = QLabel(self.musicInfoBGFrame)
        self.musicNameLabel.setObjectName(u"musicNameLabel")
        sizePolicy1.setHeightForWidth(self.musicNameLabel.sizePolicy().hasHeightForWidth())
        self.musicNameLabel.setSizePolicy(sizePolicy1)
        self.musicNameLabel.setMinimumSize(QSize(150, 26))
        self.musicNameLabel.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_4.addWidget(self.musicNameLabel)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_13)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pgupRButton1 = QRadioButton(self.musicInfoBGFrame)
        self.RButtonGroup.addButton(self.pgupRButton1)
        self.pgupRButton1.setObjectName(u"pgupRButton1")
        sizePolicy1.setHeightForWidth(self.pgupRButton1.sizePolicy().hasHeightForWidth())
        self.pgupRButton1.setSizePolicy(sizePolicy1)
        self.pgupRButton1.setMinimumSize(QSize(26, 26))

        self.horizontalLayout_4.addWidget(self.pgupRButton1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.playRButton1 = QRadioButton(self.musicInfoBGFrame)
        self.RButtonGroup.addButton(self.playRButton1)
        self.playRButton1.setObjectName(u"playRButton1")
        sizePolicy1.setHeightForWidth(self.playRButton1.sizePolicy().hasHeightForWidth())
        self.playRButton1.setSizePolicy(sizePolicy1)
        self.playRButton1.setMinimumSize(QSize(26, 26))

        self.horizontalLayout_4.addWidget(self.playRButton1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.pgdnRButton1 = QRadioButton(self.musicInfoBGFrame)
        self.RButtonGroup.addButton(self.pgdnRButton1)
        self.pgdnRButton1.setObjectName(u"pgdnRButton1")
        sizePolicy1.setHeightForWidth(self.pgdnRButton1.sizePolicy().hasHeightForWidth())
        self.pgdnRButton1.setSizePolicy(sizePolicy1)
        self.pgdnRButton1.setMinimumSize(QSize(26, 26))

        self.horizontalLayout_4.addWidget(self.pgdnRButton1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_16)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_17)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_14)

        self.desktopLyricsRButton1 = QRadioButton(self.musicInfoBGFrame)
        self.RButtonGroup.addButton(self.desktopLyricsRButton1)
        self.desktopLyricsRButton1.setObjectName(u"desktopLyricsRButton1")
        self.desktopLyricsRButton1.setMinimumSize(QSize(26, 26))

        self.horizontalLayout_4.addWidget(self.desktopLyricsRButton1)

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.playModeRButton1 = QRadioButton(self.musicInfoBGFrame)
        self.RButtonGroup.addButton(self.playModeRButton1)
        self.playModeRButton1.setObjectName(u"playModeRButton1")
        sizePolicy1.setHeightForWidth(self.playModeRButton1.sizePolicy().hasHeightForWidth())
        self.playModeRButton1.setSizePolicy(sizePolicy1)
        self.playModeRButton1.setMinimumSize(QSize(26, 26))

        self.horizontalLayout_4.addWidget(self.playModeRButton1)

        self.horizontalSpacer_9 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.volumeControlRButton1 = QRadioButton(self.musicInfoBGFrame)
        self.RButtonGroup.addButton(self.volumeControlRButton1)
        self.volumeControlRButton1.setObjectName(u"volumeControlRButton1")
        sizePolicy1.setHeightForWidth(self.volumeControlRButton1.sizePolicy().hasHeightForWidth())
        self.volumeControlRButton1.setSizePolicy(sizePolicy1)
        self.volumeControlRButton1.setMinimumSize(QSize(26, 26))

        self.horizontalLayout_4.addWidget(self.volumeControlRButton1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.musicInfoBGFrame)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.background.addTab(self.mainTab, "")
        self.playTab = QWidget()
        self.playTab.setObjectName(u"playTab")
        self.background.addTab(self.playTab, "")

        self.FormLayout.addWidget(self.background)


        self.retranslateUi(Form)

        self.background.setCurrentIndex(0)
        self.subTabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Simple Player", None))
        self.label.setText(QCoreApplication.translate("Form", u"Simple Player", None))
        self.winMiniRButton.setText("")
        self.winMaxRButton.setText("")
        self.winCloseRButton.setText("")

        __sortingEnabled = self.menuListWidget.isSortingEnabled()
        self.menuListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.menuListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"\u97f3\u4e50", None));
        ___qlistwidgetitem1 = self.menuListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5939", None));
        ___qlistwidgetitem2 = self.menuListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None));
        self.menuListWidget.setSortingEnabled(__sortingEnabled)

        self.subTabWidget.setTabText(self.subTabWidget.indexOf(self.tab), "")

        __sortingEnabled1 = self.folderListWidget.isSortingEnabled()
        self.folderListWidget.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.folderListWidget.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"\u9f20\u6807\u53f3\u952e\u4ee5\u6dfb\u52a0\u6216\u5220\u9664\u6587\u4ef6\u5939", None));
        self.folderListWidget.setSortingEnabled(__sortingEnabled1)

        self.subTabWidget.setTabText(self.subTabWidget.indexOf(self.tab_1), "")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5e38\u89c4\u8bbe\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5173\u95ed\u7a97\u53e3", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u684c\u9762\u6b4c\u8bcd", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5b57\u4f53", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5b57\u4f53\u5927\u5c0f", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u5b57\u4f53\u989c\u8272", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u63cf\u8fb9\u5927\u5c0f", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u63cf\u8fb9\u989c\u8272", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u6b4c\u8bcd\u4f4d\u7f6e", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u6b4c\u8bcd\u7f29\u653e\u6bd4", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u6b4c\u8bcd\u900f\u660e\u5ea6", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u5feb\u952e\u952e", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u64ad\u653e/\u6682\u505c", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e00\u66f2", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u66f2", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u97f3\u91cf +", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u97f3\u91cf -", None))
        self.label_21.setText("")
        self.minTrayRButton.setText(QCoreApplication.translate("Form", u"\u6700\u5c0f\u5316\u5230\u6258\u76d8", None))
        self.quitRButton.setText(QCoreApplication.translate("Form", u"\u9000\u51fa\u7a0b\u5e8f", None))
        self.label_20.setText("")
        self.fontColorPButton.setText("")
        self.strokeColorPButton.setText("")
        self.label_19.setText("")
        self.subTabWidget.setTabText(self.subTabWidget.indexOf(self.tab_2), "")
        self.subTabWidget.setTabText(self.subTabWidget.indexOf(self.tab_3), "")
        self.musicLogoPButton.setText("")
        self.playSliderTxt1.setText(QCoreApplication.translate("Form", u"00:00/00:00", None))
        self.musicNameLabel.setText("")
        self.pgupRButton1.setText("")
        self.playRButton1.setText("")
        self.pgdnRButton1.setText("")
        self.desktopLyricsRButton1.setText("")
        self.playModeRButton1.setText("")
        self.volumeControlRButton1.setText("")
        self.background.setTabText(self.background.indexOf(self.mainTab), "")
        self.background.setTabText(self.background.indexOf(self.playTab), "")
    # retranslateUi

