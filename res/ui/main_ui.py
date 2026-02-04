# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QTabWidget, QTableView, QVBoxLayout,
    QWidget)

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
"/************************************ QFrame ************************************/\n"
"\n"
"QFrame#background\n"
"{\n"
"	background-color: #2F3648;\n"
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
"\n"
"/************************************ QLabel  ************************************/\n"
"\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"/************************************ QListWidget  ************************************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QListWidget\n"
"{\n"
"	background-color: transparent;\n"
"	bor"
                        "der-radius: 0px;\n"
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
"	background-color: transparent;\n"
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
"QTab"
                        "Bar::tab\n"
"{\n"
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
"  "
                        "  padding: 0px;\n"
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
"	w"
                        "idth: 15px;\n"
"	height: 15px;\n"
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
"	pa"
                        "dding-bottom: -2px;\n"
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
"	border-image: url"
                        "(:/pause/img/pause.png);\n"
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
"	border-"
                        "image: url(:/pgup/img/pgup.png);\n"
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
"	b"
                        "order-image: url(:/pgdn/img/pgdn.png);\n"
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
"QRadioButton#volumeControlRButton2::indica"
                        "tor:checked\n"
"{\n"
"	border-image: url(:/volume/img/volume.png);\n"
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
"\n"
"/****************************"
                        "******** QSlider ************************************/\n"
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
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid;\n"
"    width: 3px;  /* \u5c06height\u6539\u4e3awidth */\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"  "
                        "  background: #dc82d7;\n"
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
"    background: #5a6375;\n"
"    margin-left: 1px;\n"
"    margin-right: 1px;\n"
"}\n"
"\n"
"/*\u6eda\u52a8\u6761\u9f20\u6807\u60ac\u505c*/\n"
"QScrollBar::handle:hover\n"
"{\n"
"    background: #6f7b91;\n"
"}\n"
"\n"
"/*\u4e0b\u65b9\u7bad\u5934*/\n"
"QScrollBar::add-line\n"
"{\n"
"    height: 0px;\n"
"	width: 0px;\n"
"}\n"
"\n"
"/*\u4e0a\u65b9\u7bad\u5934*/\n"
"QScrollBar::sub-line\n"
"{\n"
"    height: 0px;\n"
"	width: 0px;\n"
"}\n"
"\n"
"/*\u6ed1\u5757\u5df2\u7ecf\u7ecf\u8fc7\u7684\u6ed1\u8f68\u533a\u57df\u7684\u989c\u8272*/\n"
"QScrollBar::add-page:vertical\n"
""
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
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.background = QFrame(Form)
        self.background.setObjectName(u"background")
        self.background.setFrameShape(QFrame.Shape.StyledPanel)
        self.background.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 4, 6, 6)
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setSpacing(0)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.icon = QLabel(self.background)
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

        self.label = QLabel(self.background)
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
        self.winMiniRButton = QRadioButton(self.background)
        self.winBarGroup = QButtonGroup(Form)
        self.winBarGroup.setObjectName(u"winBarGroup")
        self.winBarGroup.setExclusive(False)
        self.winBarGroup.addButton(self.winMiniRButton)
        self.winMiniRButton.setObjectName(u"winMiniRButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.winMiniRButton.sizePolicy().hasHeightForWidth())
        self.winMiniRButton.setSizePolicy(sizePolicy2)
        self.winMiniRButton.setMinimumSize(QSize(26, 26))
        self.winMiniRButton.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_2.addWidget(self.winMiniRButton)

        self.winMaxRButton = QRadioButton(self.background)
        self.winBarGroup.addButton(self.winMaxRButton)
        self.winMaxRButton.setObjectName(u"winMaxRButton")
        sizePolicy2.setHeightForWidth(self.winMaxRButton.sizePolicy().hasHeightForWidth())
        self.winMaxRButton.setSizePolicy(sizePolicy2)
        self.winMaxRButton.setMinimumSize(QSize(26, 26))
        self.winMaxRButton.setMaximumSize(QSize(16777215, 21))
        self.winMaxRButton.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.winMaxRButton)

        self.winCloseRButton = QRadioButton(self.background)
        self.winBarGroup.addButton(self.winCloseRButton)
        self.winCloseRButton.setObjectName(u"winCloseRButton")
        sizePolicy2.setHeightForWidth(self.winCloseRButton.sizePolicy().hasHeightForWidth())
        self.winCloseRButton.setSizePolicy(sizePolicy2)
        self.winCloseRButton.setMinimumSize(QSize(26, 26))
        self.winCloseRButton.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_2.addWidget(self.winCloseRButton)


        self.horizontalLayout_1.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_1)

        self.mainTabWidget = QTabWidget(self.background)
        self.mainTabWidget.setObjectName(u"mainTabWidget")
        self.mainTab = QWidget()
        self.mainTab.setObjectName(u"mainTab")
        self.verticalLayout_5 = QVBoxLayout(self.mainTab)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

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
        self.musicLogoPushButton = QPushButton(self.musicInfoBGFrame)
        self.musicLogoPushButton.setObjectName(u"musicLogoPushButton")
        sizePolicy1.setHeightForWidth(self.musicLogoPushButton.sizePolicy().hasHeightForWidth())
        self.musicLogoPushButton.setSizePolicy(sizePolicy1)
        self.musicLogoPushButton.setMinimumSize(QSize(60, 60))
        self.musicLogoPushButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_7.addWidget(self.musicLogoPushButton)

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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.playSlider1.sizePolicy().hasHeightForWidth())
        self.playSlider1.setSizePolicy(sizePolicy4)
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
        self.winBarGroup.addButton(self.pgupRButton1)
        self.pgupRButton1.setObjectName(u"pgupRButton1")
        sizePolicy1.setHeightForWidth(self.pgupRButton1.sizePolicy().hasHeightForWidth())
        self.pgupRButton1.setSizePolicy(sizePolicy1)
        self.pgupRButton1.setMinimumSize(QSize(26, 26))

        self.horizontalLayout_4.addWidget(self.pgupRButton1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.playRButton1 = QRadioButton(self.musicInfoBGFrame)
        self.winBarGroup.addButton(self.playRButton1)
        self.playRButton1.setObjectName(u"playRButton1")
        sizePolicy1.setHeightForWidth(self.playRButton1.sizePolicy().hasHeightForWidth())
        self.playRButton1.setSizePolicy(sizePolicy1)
        self.playRButton1.setMinimumSize(QSize(26, 26))

        self.horizontalLayout_4.addWidget(self.playRButton1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.pgdnRButton1 = QRadioButton(self.musicInfoBGFrame)
        self.winBarGroup.addButton(self.pgdnRButton1)
        self.pgdnRButton1.setObjectName(u"pgdnRButton1")
        sizePolicy1.setHeightForWidth(self.pgdnRButton1.sizePolicy().hasHeightForWidth())
        self.pgdnRButton1.setSizePolicy(sizePolicy1)
        self.pgdnRButton1.setMinimumSize(QSize(26, 26))

        self.horizontalLayout_4.addWidget(self.pgdnRButton1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_16)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_14)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.playModeRButton1 = QRadioButton(self.musicInfoBGFrame)
        self.winBarGroup.addButton(self.playModeRButton1)
        self.playModeRButton1.setObjectName(u"playModeRButton1")
        sizePolicy1.setHeightForWidth(self.playModeRButton1.sizePolicy().hasHeightForWidth())
        self.playModeRButton1.setSizePolicy(sizePolicy1)
        self.playModeRButton1.setMinimumSize(QSize(26, 26))

        self.horizontalLayout_4.addWidget(self.playModeRButton1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.volumeControlRButton1 = QRadioButton(self.musicInfoBGFrame)
        self.winBarGroup.addButton(self.volumeControlRButton1)
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


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.mainTabWidget.addTab(self.mainTab, "")
        self.playTab = QWidget()
        self.playTab.setObjectName(u"playTab")
        self.mainTabWidget.addTab(self.playTab, "")

        self.verticalLayout_3.addWidget(self.mainTabWidget)


        self.horizontalLayout.addWidget(self.background)


        self.retranslateUi(Form)

        self.subTabWidget.setCurrentIndex(1)


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
        self.subTabWidget.setTabText(self.subTabWidget.indexOf(self.tab_2), "")
        self.subTabWidget.setTabText(self.subTabWidget.indexOf(self.tab_3), "")
        self.musicLogoPushButton.setText("")
        self.playSliderTxt1.setText(QCoreApplication.translate("Form", u"00:00/00:00", None))
        self.musicNameLabel.setText("")
        self.pgupRButton1.setText("")
        self.playRButton1.setText("")
        self.pgdnRButton1.setText("")
        self.playModeRButton1.setText("")
        self.volumeControlRButton1.setText("")
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.mainTab), "")
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.playTab), "")
    # retranslateUi

