# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'desktop_lyrics.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGraphicsView,
    QHBoxLayout, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1200, 250)
        Form.setStyleSheet(u"\n"
"/************************************ QFrame  ************************************/\n"
"\n"
"\n"
"QFrame#background\n"
"{\n"
"	background-color: #1F2430;\n"
"}\n"
"\n"
"\n"
"\n"
"/************************************ QGraphicsView  ************************************/\n"
"\n"
"QGraphicsView\n"
"{\n"
"	background-color: transparent;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"\n"
"/************************************ QRadioButton  ************************************/\n"
"\n"
"\n"
"/************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QRadioButton#transparentRButton::indicator:checked\n"
"{\n"
"	border-image: url(:/transparent/img/transparents.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"QRadioButton#transparentRButton::indicator:unchecked\n"
"{\n"
"	border-image: url(:/transparent/img/transparent.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"/*\u60ac\u505c*/\n"
"QRadioButton#transparentRButton::indicator:checked:hover\n"
"{\n"
"	border-image: url(:/transparent/img/transparents.png);\n"
"	widt"
                        "h: 22px;\n"
"	height: 22px;\n"
"}\n"
"QRadioButton#transparentRButton::indicator:unchecked:hover\n"
"{\n"
"	border-image: url(:/transparent/img/transparent.png);\n"
"	width: 22px;\n"
"	height: 22px;\n"
"}\n"
"\n"
"QRadioButton#transparentRButton:pressed\n"
"{\n"
"	padding-bottom: -2px;\n"
"	padding-left: 1px\n"
"}\n"
"\n"
"\n"
"/************/\n"
"\n"
"/*\u539f\u59cb*/\n"
"QRadioButton#lockRButton::indicator:checked\n"
"{\n"
"	border-image: url(:/lock/img/locks.png);\n"
"	width: 21px;\n"
"	height: 21px;\n"
"}\n"
"\n"
"QRadioButton#lockRButton::indicator:unchecked\n"
"{\n"
"	border-image: url(:/lock/img/lock.png);\n"
"	width: 21px;\n"
"	height: 21px;\n"
"}\n"
"\n"
"/*\u60ac\u505c*/\n"
"QRadioButton#lockRButton::indicator:checked:hover\n"
"{\n"
"	border-image: url(:/lock/img/locks.png);\n"
"	width: 21px;\n"
"	height: 21px;\n"
"}\n"
"QRadioButton#lockRButton::indicator:unchecked:hover\n"
"{\n"
"	border-image: url(:/lock/img/lock.png);\n"
"	width: 21px;\n"
"	height: 21px;\n"
"}\n"
"\n"
"QRadioButton#lockRButton:pre"
                        "ssed\n"
"{\n"
"	padding-bottom: -2px;\n"
"	padding-left: 1px\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.background = QFrame(Form)
        self.background.setObjectName(u"background")
        self.background.setFrameShape(QFrame.Shape.StyledPanel)
        self.background.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.background)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.transparentRButton = QRadioButton(self.background)
        self.RButtonGroup = QButtonGroup(Form)
        self.RButtonGroup.setObjectName(u"RButtonGroup")
        self.RButtonGroup.setExclusive(False)
        self.RButtonGroup.addButton(self.transparentRButton)
        self.transparentRButton.setObjectName(u"transparentRButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transparentRButton.sizePolicy().hasHeightForWidth())
        self.transparentRButton.setSizePolicy(sizePolicy)
        self.transparentRButton.setMinimumSize(QSize(26, 26))

        self.horizontalLayout_2.addWidget(self.transparentRButton)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.lockRButton = QRadioButton(self.background)
        self.RButtonGroup.addButton(self.lockRButton)
        self.lockRButton.setObjectName(u"lockRButton")
        sizePolicy.setHeightForWidth(self.lockRButton.sizePolicy().hasHeightForWidth())
        self.lockRButton.setSizePolicy(sizePolicy)
        self.lockRButton.setMinimumSize(QSize(26, 26))

        self.horizontalLayout_2.addWidget(self.lockRButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.graphicsView = QGraphicsView(self.background)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)


        self.horizontalLayout.addWidget(self.background)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Desktop Lyrics", None))
        self.transparentRButton.setText("")
        self.lockRButton.setText("")
    # retranslateUi

