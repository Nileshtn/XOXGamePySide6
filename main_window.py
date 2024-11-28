# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window2.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLCDNumber, QFormLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget, QDialog)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(480, 540))
        MainWindow.setMaximumSize(QSize(480, 540))
        
        self.actionRestart = QAction(MainWindow)
        self.actionRestart.setObjectName(u"actionRestart")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionboard = QAction(MainWindow)
        self.actionboard.setObjectName(u"actionboard")
        self.actionplayer_name = QAction(MainWindow)
        self.actionplayer_name.setObjectName(u"actionplayer_name")
        self.actionstart = QAction(MainWindow)
        self.actionstart.setObjectName(u"actionstart")
        self.actionscore = QAction(MainWindow)
        self.actionscore.setObjectName(u"actionscore")
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.place00 = QPushButton(self.centralwidget)
        self.place00.setObjectName(u"place00")
        self.place00.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.place00.sizePolicy().hasHeightForWidth())
        self.place00.setSizePolicy(sizePolicy1)
        self.place00.setMaximumSize(QSize(128, 128))
        self.place00.setAutoRepeat(False)
        self.place00.setAutoExclusive(False)
        self.place00.setAutoDefault(False)
        self.place00.setFlat(False)
        self.gridLayout_2.addWidget(self.place00, 0, 0, 1, 1)

        self.place02 = QPushButton(self.centralwidget)
        self.place02.setObjectName(u"place02")
        self.place02.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.place02.sizePolicy().hasHeightForWidth())
        self.place02.setSizePolicy(sizePolicy1)
        self.place02.setMaximumSize(QSize(128, 128))
        self.place02.setAutoRepeat(False)
        self.place02.setAutoExclusive(False)
        self.place02.setAutoDefault(False)
        self.place02.setFlat(False)

        self.gridLayout_2.addWidget(self.place02, 0, 2, 1, 1)

        self.place20 = QPushButton(self.centralwidget)
        self.place20.setObjectName(u"place20")
        self.place20.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.place20.sizePolicy().hasHeightForWidth())
        self.place20.setSizePolicy(sizePolicy1)
        self.place20.setMaximumSize(QSize(128, 128))
        self.place20.setAutoRepeat(False)
        self.place20.setAutoExclusive(False)
        self.place20.setAutoDefault(False)
        self.place20.setFlat(False)

        self.gridLayout_2.addWidget(self.place20, 2, 0, 1, 1)

        self.place10 = QPushButton(self.centralwidget)
        self.place10.setObjectName(u"place10")
        self.place10.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.place10.sizePolicy().hasHeightForWidth())
        self.place10.setSizePolicy(sizePolicy1)
        self.place10.setMaximumSize(QSize(128, 128))
        self.place10.setAutoRepeat(False)
        self.place10.setAutoExclusive(False)
        self.place10.setAutoDefault(False)
        self.place10.setFlat(False)

        self.gridLayout_2.addWidget(self.place10, 1, 0, 1, 1)

        self.place22 = QPushButton(self.centralwidget)
        self.place22.setObjectName(u"place22")
        self.place22.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.place22.sizePolicy().hasHeightForWidth())
        self.place22.setSizePolicy(sizePolicy1)
        self.place22.setMaximumSize(QSize(128, 128))
        self.place22.setAutoRepeat(False)
        self.place22.setAutoExclusive(False)
        self.place22.setAutoDefault(False)
        self.place22.setFlat(False)

        self.gridLayout_2.addWidget(self.place22, 2, 2, 1, 1)

        self.place01 = QPushButton(self.centralwidget)
        self.place01.setObjectName(u"place01")
        self.place01.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.place01.sizePolicy().hasHeightForWidth())
        self.place01.setSizePolicy(sizePolicy1)
        self.place01.setMaximumSize(QSize(128, 128))
        self.place01.setAutoRepeat(False)
        self.place01.setAutoExclusive(False)
        self.place01.setAutoDefault(False)
        self.place01.setFlat(False)

        self.gridLayout_2.addWidget(self.place01, 0, 1, 1, 1)

        self.place12 = QPushButton(self.centralwidget)
        self.place12.setObjectName(u"place12")
        self.place12.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.place12.sizePolicy().hasHeightForWidth())
        self.place12.setSizePolicy(sizePolicy1)
        self.place12.setMaximumSize(QSize(128, 128))
        self.place12.setAutoRepeat(False)
        self.place12.setAutoExclusive(False)
        self.place12.setAutoDefault(False)
        self.place12.setFlat(False)

        self.gridLayout_2.addWidget(self.place12, 1, 2, 1, 1)

        self.place11 = QPushButton(self.centralwidget)
        self.place11.setObjectName(u"place11")
        self.place11.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.place11.sizePolicy().hasHeightForWidth())
        self.place11.setSizePolicy(sizePolicy1)
        self.place11.setMaximumSize(QSize(128, 128))
        self.place11.setAutoRepeat(False)
        self.place11.setAutoExclusive(False)
        self.place11.setAutoDefault(False)
        self.place11.setFlat(False)

        self.gridLayout_2.addWidget(self.place11, 1, 1, 1, 1)

        self.place21 = QPushButton(self.centralwidget)
        self.place21.setObjectName(u"place21")
        self.place21.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.place21.sizePolicy().hasHeightForWidth())
        self.place21.setSizePolicy(sizePolicy1)
        self.place21.setMaximumSize(QSize(128, 128))
        self.place21.setAutoRepeat(False)
        self.place21.setAutoExclusive(False)
        self.place21.setAutoDefault(False)
        self.place21.setFlat(False)

        self.gridLayout_2.addWidget(self.place21, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")

        self.horizontalLayout.addWidget(self.start_button)

        self.resetButton = QPushButton(self.centralwidget)
        self.resetButton.setObjectName(u"resetButton")

        self.horizontalLayout.addWidget(self.resetButton)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.player_x_nameLineEdit = QLineEdit(self.centralwidget)
        self.player_x_nameLineEdit.setObjectName(u"player_x_nameLineEdit")

        self.gridLayout.addWidget(self.player_x_nameLineEdit, 0, 1, 1, 1)

        self.player_y_nameLineEdit = QLineEdit(self.centralwidget)
        self.player_y_nameLineEdit.setObjectName(u"player_y_nameLineEdit")

        self.gridLayout.addWidget(self.player_y_nameLineEdit, 1, 1, 1, 1)

        self.player_y_nameLabel = QLabel(self.centralwidget)
        self.player_y_nameLabel.setObjectName(u"player_y_nameLabel")

        self.gridLayout.addWidget(self.player_y_nameLabel, 1, 0, 1, 1)

        self.player_x_nameLabel = QLabel(self.centralwidget)
        self.player_x_nameLabel.setObjectName(u"player_x_nameLabel")

        self.gridLayout.addWidget(self.player_x_nameLabel, 0, 0, 1, 1)

        self.player_x_score = QLCDNumber(self.centralwidget)
        self.player_x_score.setObjectName(u"player_x_score")
        self.player_x_score.setSmallDecimalPoint(False)
        self.player_x_score.setDigitCount(1)

        self.gridLayout.addWidget(self.player_x_score, 0, 2, 1, 1)

        self.player_y_score = QLCDNumber(self.centralwidget)
        self.player_y_score.setObjectName(u"player_y_score")
        self.player_y_score.setDigitCount(1)
        self.player_y_score.setProperty(u"intValue", 0)

        self.gridLayout.addWidget(self.player_y_score, 1, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 24))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        self.menutools = QMenu(self.menubar)
        self.menutools.setObjectName(u"menutools")
        self.menureset = QMenu(self.menutools)
        self.menureset.setObjectName(u"menureset")
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.player_y_nameLabel.setBuddy(self.player_y_nameLineEdit)
        self.player_x_nameLabel.setBuddy(self.player_x_nameLineEdit)
#endif // QT_CONFIG(shortcut)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menutools.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menufile.addAction(self.actionRestart)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionQuit)
        self.menutools.addAction(self.menureset.menuAction())
        self.menutools.addAction(self.actionstart)
        self.menureset.addAction(self.actionboard)
        self.menureset.addAction(self.actionplayer_name)
        self.menureset.addAction(self.actionscore)
        self.menuhelp.addAction(self.actionabout)
        self.menuhelp.addAction(self.actionhelp)

        self.retranslateUi(MainWindow)

        self.place00.setDefault(False)
        self.place02.setDefault(False)
        self.place20.setDefault(False)
        self.place10.setDefault(False)
        self.place22.setDefault(False)
        self.place01.setDefault(False)
        self.place12.setDefault(False)
        self.place11.setDefault(False)
        self.place21.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"XOX Game", None))
        self.actionRestart.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionboard.setText(QCoreApplication.translate("MainWindow", u"board", None))
        self.actionplayer_name.setText(QCoreApplication.translate("MainWindow", u"player name", None))
        self.actionstart.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.actionscore.setText(QCoreApplication.translate("MainWindow", u"score", None))
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.actionhelp.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.place00.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.place02.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.place20.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.place10.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.place22.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.place01.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.place12.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.place11.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.place21.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"reset", None))
        self.player_y_nameLabel.setText(QCoreApplication.translate("MainWindow", u"player_y_name", None))
        self.player_x_nameLabel.setText(QCoreApplication.translate("MainWindow", u"Player_x_name", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
        self.menutools.setTitle(QCoreApplication.translate("MainWindow", u"tools", None))
        self.menureset.setTitle(QCoreApplication.translate("MainWindow", u"reset", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"help", None))
    # retranslateUi


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("set player name")
        self.setMinimumHeight(125)
        self.setMinimumWidth(340)
        self.setMaximumHeight(125)
        self.setMaximumWidth(345)
        
        # Vertical layout for the dialog
        layout = QVBoxLayout(self)
        self.formlo = QFormLayout()
        layout.addLayout(self.formlo)

        # First input field
        
        
        self.player_x_name_tb = QLineEdit(self)
        self.formlo.addRow("Enter player_x_name:", self.player_x_name_tb)

        # Second input field
        self.player_o_name_tb = QLineEdit(self)
        self.formlo.addRow("Enter player_o_name:", self.player_o_name_tb)

        # Horizontal layout for buttons
        button_layout = QHBoxLayout()

        # OK button
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)  # Close dialog and return accepted status
        button_layout.addWidget(self.ok_button)

        # Cancel button
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)  # Close dialog and return rejected status
        button_layout.addWidget(self.cancel_button)

        # Add buttons to the main layout
        layout.addLayout(button_layout)

    def get_inputs(self):
        """Return the text from the two textboxes."""
        return self.player_x_name_tb.text(), self.player_o_name_tb.text()