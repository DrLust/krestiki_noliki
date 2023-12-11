# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowhPMCtq.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QDockWidget, QHBoxLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QToolBar, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1037, 736)
        self.actionStartTimer = QAction(MainWindow)
        self.actionStartTimer.setObjectName(u"actionStartTimer")
        self.actionStopTimer = QAction(MainWindow)
        self.actionStopTimer.setObjectName(u"actionStopTimer")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonBackWebPage = QPushButton(self.centralwidget)
        self.pushButtonBackWebPage.setObjectName(u"pushButtonBackWebPage")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBackWebPage.sizePolicy().hasHeightForWidth())
        self.pushButtonBackWebPage.setSizePolicy(sizePolicy)
        self.pushButtonBackWebPage.setMaximumSize(QSize(25, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButtonBackWebPage)

        self.url_le = QLineEdit(self.centralwidget)
        self.url_le.setObjectName(u"url_le")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.url_le.sizePolicy().hasHeightForWidth())
        self.url_le.setSizePolicy(sizePolicy1)
        self.url_le.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.url_le)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.commands_cb = QComboBox(self.centralwidget)
        self.commands_cb.setObjectName(u"commands_cb")
        sizePolicy1.setHeightForWidth(self.commands_cb.sizePolicy().hasHeightForWidth())
        self.commands_cb.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.commands_cb)

        self.run_pb = QPushButton(self.centralwidget)
        self.run_pb.setObjectName(u"run_pb")
        self.run_pb.setMaximumSize(QSize(35, 16777215))

        self.horizontalLayout.addWidget(self.run_pb)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.view = QWebEngineView(self.centralwidget)
        self.view.setObjectName(u"view")
        self.view.setUrl(QUrl(u"about:blank"))

        self.verticalLayout.addWidget(self.view)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1037, 22))
        self.menuDockWindow = QMenu(self.menubar)
        self.menuDockWindow.setObjectName(u"menuDockWindow")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dock_widget_exec = QDockWidget(MainWindow)
        self.dock_widget_exec.setObjectName(u"dock_widget_exec")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_exec = QPushButton(self.dockWidgetContents_2)
        self.button_exec.setObjectName(u"button_exec")

        self.verticalLayout_2.addWidget(self.button_exec)

        self.code = QComboBox(self.dockWidgetContents_2)
        self.code.setObjectName(u"code")

        self.verticalLayout_2.addWidget(self.code)

        self.dock_widget_exec.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dock_widget_exec)
        self.dock_widget_simple_log = QDockWidget(MainWindow)
        self.dock_widget_simple_log.setObjectName(u"dock_widget_simple_log")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 3, -1, -1)
        self.clear_slog = QToolButton(self.dockWidgetContents)
        self.clear_slog.setObjectName(u"clear_slog")

        self.verticalLayout_3.addWidget(self.clear_slog)

        self.simple_log = QPlainTextEdit(self.dockWidgetContents)
        self.simple_log.setObjectName(u"simple_log")

        self.verticalLayout_3.addWidget(self.simple_log)

        self.dock_widget_simple_log.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dock_widget_simple_log)
        self.toolBarGeneral = QToolBar(MainWindow)
        self.toolBarGeneral.setObjectName(u"toolBarGeneral")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBarGeneral)

        self.menubar.addAction(self.menuDockWindow.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.toolBarGeneral.addAction(self.actionStartTimer)
        self.toolBarGeneral.addAction(self.actionStopTimer)

        self.retranslateUi(MainWindow)
        self.clear_slog.clicked.connect(self.simple_log.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u0442 moswar", None))
        self.actionStartTimer.setText(QCoreApplication.translate("MainWindow", u"Start Timer", None))
#if QT_CONFIG(tooltip)
        self.actionStartTimer.setToolTip(QCoreApplication.translate("MainWindow", u"Start Timer", None))
#endif // QT_CONFIG(tooltip)
        self.actionStopTimer.setText(QCoreApplication.translate("MainWindow", u"Stop Timer", None))
#if QT_CONFIG(tooltip)
        self.actionStopTimer.setToolTip(QCoreApplication.translate("MainWindow", u"Stop Timer", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButtonBackWebPage.setToolTip(QCoreApplication.translate("MainWindow", u"Back", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButtonBackWebPage.setStatusTip(QCoreApplication.translate("MainWindow", u"Back", None))
#endif // QT_CONFIG(statustip)
        self.pushButtonBackWebPage.setText(QCoreApplication.translate("MainWindow", u"<-", None))
        self.run_pb.setText(QCoreApplication.translate("MainWindow", u"run", None))
        self.menuDockWindow.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043d\u0430", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.dock_widget_exec.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0441\u043a\u0440\u0438\u043f\u0442\u0430", None))
        self.button_exec.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c!", None))
        self.dock_widget_simple_log.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u0442\u043e\u0439 \u043b\u043e\u0433", None))
#if QT_CONFIG(tooltip)
        self.clear_slog.setToolTip(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043b\u043e\u0433", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.clear_slog.setStatusTip(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043b\u043e\u0433", None))
#endif // QT_CONFIG(statustip)
        self.clear_slog.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043b\u043e\u0433", None))
        self.toolBarGeneral.setWindowTitle(QCoreApplication.translate("MainWindow", u"General", None))
    # retranslateUi

