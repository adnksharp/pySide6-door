# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(406, 463)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.open = QPushButton(Widget)
        self.open.setObjectName(u"open")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open.sizePolicy().hasHeightForWidth())
        self.open.setSizePolicy(sizePolicy)
        self.open.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.open)

        self.lcdNumber = QLCDNumber(Widget)
        self.lcdNumber.setObjectName(u"lcdNumber")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy1)
        self.lcdNumber.setMinimumSize(QSize(0, 38))
        self.lcdNumber.setFrameShape(QFrame.Shape.NoFrame)
        self.lcdNumber.setFrameShadow(QFrame.Shadow.Plain)
        self.lcdNumber.setLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(18)
        self.lcdNumber.setMode(QLCDNumber.Mode.Dec)
        self.lcdNumber.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.verticalLayout_3.addWidget(self.lcdNumber)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.b_5 = QPushButton(Widget)
        self.b_5.setObjectName(u"b_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.b_5.sizePolicy().hasHeightForWidth())
        self.b_5.setSizePolicy(sizePolicy2)
        self.b_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.b_5, 1, 1, 1, 1)

        self.b_4 = QPushButton(Widget)
        self.b_4.setObjectName(u"b_4")
        sizePolicy2.setHeightForWidth(self.b_4.sizePolicy().hasHeightForWidth())
        self.b_4.setSizePolicy(sizePolicy2)
        self.b_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.b_4, 1, 0, 1, 1)

        self.b_2 = QPushButton(Widget)
        self.b_2.setObjectName(u"b_2")
        sizePolicy2.setHeightForWidth(self.b_2.sizePolicy().hasHeightForWidth())
        self.b_2.setSizePolicy(sizePolicy2)
        self.b_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.b_2, 2, 1, 1, 1)

        self.b_8 = QPushButton(Widget)
        self.b_8.setObjectName(u"b_8")
        sizePolicy2.setHeightForWidth(self.b_8.sizePolicy().hasHeightForWidth())
        self.b_8.setSizePolicy(sizePolicy2)
        self.b_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.b_8, 0, 1, 1, 1)

        self.b_7 = QPushButton(Widget)
        self.b_7.setObjectName(u"b_7")
        sizePolicy2.setHeightForWidth(self.b_7.sizePolicy().hasHeightForWidth())
        self.b_7.setSizePolicy(sizePolicy2)
        self.b_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.b_7, 0, 0, 1, 1)

        self.b = QPushButton(Widget)
        self.b.setObjectName(u"b")
        sizePolicy2.setHeightForWidth(self.b.sizePolicy().hasHeightForWidth())
        self.b.setSizePolicy(sizePolicy2)
        self.b.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.b, 3, 1, 1, 1)

        self.b_9 = QPushButton(Widget)
        self.b_9.setObjectName(u"b_9")
        sizePolicy2.setHeightForWidth(self.b_9.sizePolicy().hasHeightForWidth())
        self.b_9.setSizePolicy(sizePolicy2)
        self.b_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.b_9, 0, 2, 1, 1)

        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)

        self.b_6 = QPushButton(Widget)
        self.b_6.setObjectName(u"b_6")
        sizePolicy2.setHeightForWidth(self.b_6.sizePolicy().hasHeightForWidth())
        self.b_6.setSizePolicy(sizePolicy2)
        self.b_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.b_6, 1, 2, 1, 1)

        self.b_1 = QPushButton(Widget)
        self.b_1.setObjectName(u"b_1")
        sizePolicy2.setHeightForWidth(self.b_1.sizePolicy().hasHeightForWidth())
        self.b_1.setSizePolicy(sizePolicy2)
        self.b_1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.b_1, 2, 0, 1, 1)

        self.b_3 = QPushButton(Widget)
        self.b_3.setObjectName(u"b_3")
        sizePolicy2.setHeightForWidth(self.b_3.sizePolicy().hasHeightForWidth())
        self.b_3.setSizePolicy(sizePolicy2)
        self.b_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.b_3, 2, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.label)

        self.log = QPushButton(Widget)
        self.log.setObjectName(u"log")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.log.sizePolicy().hasHeightForWidth())
        self.log.setSizePolicy(sizePolicy3)
        self.log.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpenRecent))
        self.log.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.log)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Puerta", None))
        self.open.setText(QCoreApplication.translate("Widget", u"Solicitar acceso", None))
        self.b_5.setText(QCoreApplication.translate("Widget", u"5", None))
        self.b_4.setText(QCoreApplication.translate("Widget", u"4", None))
        self.b_2.setText(QCoreApplication.translate("Widget", u"2", None))
        self.b_8.setText(QCoreApplication.translate("Widget", u"8", None))
        self.b_7.setText(QCoreApplication.translate("Widget", u"7", None))
        self.b.setText(QCoreApplication.translate("Widget", u"0", None))
        self.b_9.setText(QCoreApplication.translate("Widget", u"9", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"<", None))
        self.b_6.setText(QCoreApplication.translate("Widget", u"6", None))
        self.b_1.setText(QCoreApplication.translate("Widget", u"1", None))
        self.b_3.setText(QCoreApplication.translate("Widget", u"3", None))
        self.label.setText("")
        self.log.setText("")
    # retranslateUi

