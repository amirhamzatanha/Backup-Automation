# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainSZhTGA.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import ( QCursor,
    QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget, QRadioButton, QButtonGroup, QFormLayout)
#from .resource import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1191, 720)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy1)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font1)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"../images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon1)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"../images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon2)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.content)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(340, 29, 771, 511))
        self.stackedWidget.setStyleSheet(u"background-color: black;")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.button_preReq = QPushButton(self.page_4)
        self.button_preReq.setObjectName(u"button_preReq")
        self.button_preReq.setGeometry(QRect(100, 90, 91, 24))
        self.button_preReq.setCheckable(True)
        self.plainTextEdit_3 = QPlainTextEdit(self.page_4)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(90, 130, 501, 241))
        self.plainTextEdit_3.setReadOnly(True)
        self.stackedWidget.addWidget(self.page_4)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_14 = QLabel(self.page_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(130, 80, 261, 41))
        self.label_14.setFrameShape(QFrame.NoFrame)
        self.label_14.setLineWidth(4)
        self.label_14.setMidLineWidth(1)
        self.label_14.setTextFormat(Qt.PlainText)
        self.label_14.setWordWrap(True)
        self.label_16 = QLabel(self.page_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(50, 200, 171, 21))
        self.label_16.setFrameShape(QFrame.NoFrame)
        self.label_16.setLineWidth(4)
        self.label_16.setMidLineWidth(1)
        self.label_16.setTextFormat(Qt.PlainText)
        self.label_16.setWordWrap(True)
        self.inputIRecoverymedia = QLineEdit(self.page_7)
        self.inputIRecoverymedia.setObjectName(u"inputIRecoverymedia")
        self.inputIRecoverymedia.setGeometry(QRect(250, 200, 249, 23))
        self.buttonStartRestore = QPushButton(self.page_7)
        self.buttonStartRestore.setObjectName(u"buttonStartRestore")
        self.buttonStartRestore.setGeometry(QRect(50, 410, 111, 31))
        self.label_17 = QLabel(self.page_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 240, 171, 21))
        self.label_17.setFrameShape(QFrame.NoFrame)
        self.label_17.setLineWidth(4)
        self.label_17.setMidLineWidth(1)
        self.label_17.setTextFormat(Qt.PlainText)
        self.label_17.setWordWrap(True)
        self.inputIVmName = QLineEdit(self.page_7)
        self.inputIVmName.setObjectName(u"inputIVmName")
        self.inputIVmName.setGeometry(QRect(250, 240, 249, 23))
        self.inputIRamSize = QLineEdit(self.page_7)
        self.inputIRamSize.setObjectName(u"inputIRamSize")
        self.inputIRamSize.setGeometry(QRect(250, 280, 249, 23))
        self.label_18 = QLabel(self.page_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 280, 171, 21))
        self.label_18.setFrameShape(QFrame.NoFrame)
        self.label_18.setLineWidth(4)
        self.label_18.setMidLineWidth(1)
        self.label_18.setTextFormat(Qt.PlainText)
        self.label_18.setWordWrap(True)
        self.inputIDiskSize = QLineEdit(self.page_7)
        self.inputIDiskSize.setObjectName(u"inputIDiskSize")
        self.inputIDiskSize.setGeometry(QRect(250, 320, 249, 23))
        self.label_19 = QLabel(self.page_7)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(50, 320, 171, 21))
        self.label_19.setFrameShape(QFrame.NoFrame)
        self.label_19.setLineWidth(4)
        self.label_19.setMidLineWidth(1)
        self.label_19.setTextFormat(Qt.PlainText)
        self.label_19.setWordWrap(True)
        self.label_24 = QLabel(self.page_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(50, 360, 171, 21))
        self.label_24.setFrameShape(QFrame.NoFrame)
        self.label_24.setLineWidth(4)
        self.label_24.setMidLineWidth(1)
        self.label_24.setTextFormat(Qt.PlainText)
        self.label_24.setWordWrap(True)
        self.bootloaderUEFI = QRadioButton(self.page_7)
        self.buttonGroupbootloader = QButtonGroup(MainWindow)
        self.buttonGroupbootloader.setObjectName(u"buttonGroupbootloader")
        self.buttonGroupbootloader.addButton(self.bootloaderUEFI)
        self.bootloaderUEFI.setObjectName(u"bootloaderUEFI")
        self.bootloaderUEFI.setGeometry(QRect(270, 370, 89, 20))
        self.bootloaderUEFI.setChecked(True)
        self.bootloaderLagacy = QRadioButton(self.page_7)
        self.buttonGroupbootloader.addButton(self.bootloaderLagacy)
        self.bootloaderLagacy.setObjectName(u"bootloaderLagacy")
        self.bootloaderLagacy.setGeometry(QRect(370, 370, 101, 20))
        self.stackedWidget.addWidget(self.page_7)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(80, 70, 261, 41))
        self.label_11.setFrameShape(QFrame.NoFrame)
        self.label_11.setLineWidth(4)
        self.label_11.setMidLineWidth(1)
        self.label_11.setTextFormat(Qt.PlainText)
        self.label_11.setWordWrap(True)
        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 170, 121, 39))
        self.radioFullBackup = QRadioButton(self.page_2)
        self.buttonGroupBackupType = QButtonGroup(MainWindow)
        self.buttonGroupBackupType.setObjectName(u"buttonGroupBackupType")
        self.buttonGroupBackupType.addButton(self.radioFullBackup)
        self.radioFullBackup.setObjectName(u"radioFullBackup")
        self.radioFullBackup.setGeometry(QRect(230, 160, 231, 20))
        self.radioFullBackup.setChecked(True)
        self.radioRecoveryMediaOnly = QRadioButton(self.page_2)
        self.buttonGroupBackupType.addButton(self.radioRecoveryMediaOnly)
        self.radioRecoveryMediaOnly.setObjectName(u"radioRecoveryMediaOnly")
        self.radioRecoveryMediaOnly.setGeometry(QRect(230, 190, 161, 20))
        self.buttonSetBackupOptions = QPushButton(self.page_2)
        self.buttonSetBackupOptions.setObjectName(u"buttonSetBackupOptions")
        self.buttonSetBackupOptions.setGeometry(QRect(60, 390, 131, 31))
        self.label_15 = QLabel(self.page_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(70, 288, 141, 21))
        self.radioManualReocvery = QRadioButton(self.page_2)
        self.buttonGroupRecoveryType = QButtonGroup(MainWindow)
        self.buttonGroupRecoveryType.setObjectName(u"buttonGroupRecoveryType")
        self.buttonGroupRecoveryType.addButton(self.radioManualReocvery)
        self.radioManualReocvery.setObjectName(u"radioManualReocvery")
        self.radioManualReocvery.setGeometry(QRect(230, 300, 161, 20))
        self.radioFullRecovery = QRadioButton(self.page_2)
        self.buttonGroupRecoveryType.addButton(self.radioFullRecovery)
        self.radioFullRecovery.setObjectName(u"radioFullRecovery")
        self.radioFullRecovery.setGeometry(QRect(230, 270, 231, 20))
        self.radioFullRecovery.setChecked(True)
        self.label_21 = QLabel(self.page_2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(70, 220, 141, 21))
        self.inputBackupPath = QLineEdit(self.page_2)
        self.inputBackupPath.setObjectName(u"inputBackupPath")
        self.inputBackupPath.setGeometry(QRect(230, 220, 249, 23))
        self.plainTextBackupOptions = QPlainTextEdit(self.page_2)
        self.plainTextBackupOptions.setObjectName(u"plainTextBackupOptions")
        self.plainTextBackupOptions.setGeometry(QRect(230, 360, 431, 81))
        self.plainTextBackupOptions.setReadOnly(True)
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_13 = QLabel(self.page_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(90, 50, 261, 41))
        self.label_13.setFrameShape(QFrame.NoFrame)
        self.label_13.setLineWidth(4)
        self.label_13.setMidLineWidth(1)
        self.label_13.setTextFormat(Qt.PlainText)
        self.label_13.setWordWrap(True)
        self.textOutputBackupLogs = QPlainTextEdit(self.page_5)
        self.textOutputBackupLogs.setObjectName(u"textOutputBackupLogs")
        self.textOutputBackupLogs.setGeometry(QRect(90, 100, 581, 271))
        self.textOutputBackupLogs.setReadOnly(True)
        self.button_StartBackup = QPushButton(self.page_5)
        self.button_StartBackup.setObjectName(u"button_StartBackup")
        self.button_StartBackup.setGeometry(QRect(90, 440, 91, 24))
        self.button_StartBackup.setCheckable(True)
        self.stackedWidget.addWidget(self.page_5)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_20 = QLabel(self.page_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(90, 60, 261, 41))
        self.label_20.setFrameShape(QFrame.NoFrame)
        self.label_20.setLineWidth(4)
        self.label_20.setMidLineWidth(1)
        self.label_20.setTextFormat(Qt.PlainText)
        self.label_20.setWordWrap(True)
        self.textOutputRestoreLogs = QPlainTextEdit(self.page_8)
        self.textOutputRestoreLogs.setObjectName(u"textOutputRestoreLogs")
        self.textOutputRestoreLogs.setGeometry(QRect(90, 140, 581, 271))
        self.textOutputRestoreLogs.setReadOnly(True)
        self.stackedWidget.addWidget(self.page_8)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_7 = QLabel(self.page_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 70, 261, 41))
        self.label_7.setFrameShape(QFrame.NoFrame)
        self.label_7.setLineWidth(4)
        self.label_7.setMidLineWidth(1)
        self.label_7.setTextFormat(Qt.PlainText)
        self.label_7.setWordWrap(True)
        self.buttonTestConnectionHyp = QPushButton(self.page_6)
        self.buttonGroupBackupType.addButton(self.buttonTestConnectionHyp)
        self.buttonTestConnectionHyp.setObjectName(u"buttonTestConnectionHyp")
        self.buttonTestConnectionHyp.setGeometry(QRect(150, 300, 111, 31))
        self.textOutputTestSSHHvp = QPlainTextEdit(self.page_6)
        self.textOutputTestSSHHvp.setObjectName(u"textOutputTestSSHHvp")
        self.textOutputTestSSHHvp.setGeometry(QRect(260, 300, 211, 81))
        self.textOutputTestSSHHvp.setReadOnly(True)
        self.layoutWidget = QWidget(self.page_6)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(150, 141, 271, 151))
        self.formLayout_2 = QFormLayout(self.layoutWidget)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.inputIPAddressHyp = QLineEdit(self.layoutWidget)
        self.inputIPAddressHyp.setObjectName(u"inputIPAddressHyp")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.inputIPAddressHyp)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.inputIUsernameHyp = QLineEdit(self.layoutWidget)
        self.inputIUsernameHyp.setObjectName(u"inputIUsernameHyp")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.inputIUsernameHyp)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.inputPasswordHyp = QLineEdit(self.layoutWidget)
        self.inputPasswordHyp.setObjectName(u"inputPasswordHyp")
        self.inputPasswordHyp.setEchoMode(QLineEdit.Password)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.inputPasswordHyp)

        self.label_23 = QLabel(self.layoutWidget)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_23)

        self.inputPort2 = QLineEdit(self.layoutWidget)
        self.inputPort2.setObjectName(u"inputPort2")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.inputPort2)

        self.stackedWidget.addWidget(self.page_6)
        self.page_last = QWidget()
        self.page_last.setObjectName(u"page_last")
        self.buttonRunCommand = QPushButton(self.page_last)
        self.buttonRunCommand.setObjectName(u"buttonRunCommand")
        self.buttonRunCommand.setGeometry(QRect(170, 410, 101, 24))
        self.inputCommand = QLineEdit(self.page_last)
        self.inputCommand.setObjectName(u"inputCommand")
        self.inputCommand.setGeometry(QRect(170, 370, 521, 23))
        self.textOutputTestSSH_2 = QPlainTextEdit(self.page_last)
        self.textOutputTestSSH_2.setObjectName(u"textOutputTestSSH_2")
        self.textOutputTestSSH_2.setGeometry(QRect(170, 70, 511, 271))
        self.textOutputTestSSH_2.setReadOnly(True)
        self.stackedWidget.addWidget(self.page_last)
        self.mainpage = QWidget()
        self.mainpage.setObjectName(u"mainpage")
        self.textEdit = QTextEdit(self.mainpage)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(43, 60, 651, 401))
        self.stackedWidget.addWidget(self.mainpage)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.textOutputTestSSH = QPlainTextEdit(self.page_1)
        self.textOutputTestSSH.setObjectName(u"textOutputTestSSH")
        self.textOutputTestSSH.setGeometry(QRect(300, 330, 211, 81))
        self.textOutputTestSSH.setReadOnly(True)
        self.buttonTestConnection = QPushButton(self.page_1)
        self.buttonTestConnection.setObjectName(u"buttonTestConnection")
        self.buttonTestConnection.setGeometry(QRect(170, 330, 111, 31))
        self.label_6 = QLabel(self.page_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(170, 60, 261, 41))
        self.label_6.setFrameShape(QFrame.NoFrame)
        self.label_6.setLineWidth(4)
        self.label_6.setMidLineWidth(1)
        self.label_6.setTextFormat(Qt.PlainText)
        self.label_6.setWordWrap(True)
        self.layoutWidget1 = QWidget(self.page_1)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(170, 150, 190, 112))
        self.formLayout = QFormLayout(self.layoutWidget1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.inputIPAddress = QLineEdit(self.layoutWidget1)
        self.inputIPAddress.setObjectName(u"inputIPAddress")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.inputIPAddress)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.inputIUsername = QLineEdit(self.layoutWidget1)
        self.inputIUsername.setObjectName(u"inputIUsername")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inputIUsername)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.inputPassword = QLineEdit(self.layoutWidget1)
        self.inputPassword.setObjectName(u"inputPassword")
        self.inputPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.inputPassword)

        self.label_22 = QLabel(self.layoutWidget1)
        self.label_22.setObjectName(u"label_22")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_22)

        self.inputPort = QLineEdit(self.layoutWidget1)
        self.inputPort.setObjectName(u"inputPort")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.inputPort)

        self.stackedWidget.addWidget(self.page_1)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 29, 311, 511))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(u"background-image: url(:/imagefielpath/backup.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-30, 190, 381, 341))
        self.label_4.setPixmap(QPixmap(u":/newPrefix/backup.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 0, 281, 181))
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.label_5.setLineWidth(4)
        self.label_5.setMidLineWidth(1)
        self.label_5.setTextFormat(Qt.PlainText)
        self.label_5.setWordWrap(True)
        self.layoutWidget2 = QWidget(self.frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(870, 580, 239, 28))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.buttonBack = QPushButton(self.layoutWidget2)
        self.buttonBack.setObjectName(u"buttonBack")
        self.buttonBack.setEnabled(False)
        self.buttonBack.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_7.addWidget(self.buttonBack)

        self.buttonNext = QPushButton(self.layoutWidget2)
        self.buttonNext.setObjectName(u"buttonNext")
        self.buttonNext.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_7.addWidget(self.buttonNext)

        self.buttonCancel = QPushButton(self.layoutWidget2)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_7.addWidget(self.buttonCancel)


        self.horizontalLayout_4.addWidget(self.frame)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(False)
        font2.setItalic(False)
        self.creditsLabel.setFont(font2)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.horizontalLayout_6.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.buttonStartRestore.setDefault(False)
        self.buttonSetBackupOptions.setDefault(False)
        self.buttonTestConnectionHyp.setDefault(False)
        self.buttonTestConnection.setDefault(False)
        self.buttonBack.setDefault(False)
        self.buttonNext.setDefault(False)
        self.buttonCancel.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Test Backup Application", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.button_preReq.setText(QCoreApplication.translate("MainWindow", u"Check Pre. Req", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Select VM options", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Recovery Media path on NFS", None))
        self.inputIRecoverymedia.setText(QCoreApplication.translate("MainWindow", u"/nfsshare/localhost/rear-localhost.iso", None))
        self.inputIRecoverymedia.setPlaceholderText(QCoreApplication.translate("MainWindow", u"/nfsshare/localhost/rear-localhost.iso", None))
        self.buttonStartRestore.setText(QCoreApplication.translate("MainWindow", u"Start Restore", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Enter new VM Name", None))
        self.inputIVmName.setText(QCoreApplication.translate("MainWindow", u"myvm_restored", None))
        self.inputIVmName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"myvm_restored", None))
        self.inputIRamSize.setText(QCoreApplication.translate("MainWindow", u"2048", None))
        self.inputIRamSize.setPlaceholderText(QCoreApplication.translate("MainWindow", u"2048", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Enter RAM Size", None))
        self.inputIDiskSize.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.inputIDiskSize.setPlaceholderText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Enter Disk Size", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Boot Loader", None))
        self.bootloaderUEFI.setText(QCoreApplication.translate("MainWindow", u"UEFI BIOS", None))
        self.bootloaderLagacy.setText(QCoreApplication.translate("MainWindow", u"Lagacy BIOS", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Select Backup Options", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Select Backup Type: ", None))
        self.radioFullBackup.setText(QCoreApplication.translate("MainWindow", u"Full Backup with Recovery Media", None))
        self.radioRecoveryMediaOnly.setText(QCoreApplication.translate("MainWindow", u"Recovery Media Only", None))
        self.buttonSetBackupOptions.setText(QCoreApplication.translate("MainWindow", u"Set Backup Options", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Select Recovery Option", None))
        self.radioManualReocvery.setText(QCoreApplication.translate("MainWindow", u"Manual Recovery", None))
        self.radioFullRecovery.setText(QCoreApplication.translate("MainWindow", u"Fully Automated Recovery", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Backup Path", None))
        self.inputBackupPath.setInputMask("")
        self.inputBackupPath.setText("")
        self.inputBackupPath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"10.0.0.26/nfsshare", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Backup Logs", None))
        self.button_StartBackup.setText(QCoreApplication.translate("MainWindow", u"Start Backup", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Backup Logs", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Connect to Hypervisor to test the Backup on a new VM.", None))
        self.buttonTestConnectionHyp.setText(QCoreApplication.translate("MainWindow", u"Test Connection", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.inputIPAddressHyp.setInputMask(QCoreApplication.translate("MainWindow", u"000.000.000.000;_", None))
        self.inputIPAddressHyp.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.inputIUsernameHyp.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.inputPasswordHyp.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.inputPort2.setText("")
        self.buttonRunCommand.setText(QCoreApplication.translate("MainWindow", u"Run Command", None))
        self.inputCommand.setText("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to the Backup Testing Wizard. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in this wizard we will walk you through connecting to a Linux machine, con"
                        "necting to a file server. and creating backup to the file server. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in second step we will help you restore the backup to a Virtual Environment. </p></body></html>", None))
        self.buttonTestConnection.setText(QCoreApplication.translate("MainWindow", u"Test Connection", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Connect to Backup Source Computer", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.inputIPAddress.setInputMask(QCoreApplication.translate("MainWindow", u"000.000.000.000;_", None))
        self.inputIPAddress.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.inputIUsername.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.inputPassword.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.inputPort.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Test Backup Application: More Description will come here to provide some information to the user while restoring / testing a backup. ", None))
        self.buttonBack.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.buttonNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.buttonCancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Mir Hamza Nasiri", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

