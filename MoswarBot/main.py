# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from main_window import MainWindow

if __name__ == '__main__':
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    # window = loader.load("mainwindow.ui", None)
    window = MainWindow('https://www.moswar.ru/')
    window.show()
    #window.run()
    sys.exit(app.exec())

    # mw = MainWindow()
    # mw.set_screen()
    # mw.resize(1300, 800)
    # mw.read_settings()
    # mw.show()

    # mw.ui.view.setHtml(open('[02 58 54] Задержан за бои - Милиция.htm', encoding='utf-8').read())

    # Загрузка страницы мосвара и авторизация
    # mw.auth()

    # from PySide.QtWebKit import *
    # view = QWebView()
    # view.setHtml(open('[02 58 54] Задержан за бои - Милиция.htm', encoding='utf-8').read())
    # # view.setHtml("""        <div class="fighter2">
    # #       <span class="user ">
    # #            <i class="npc" title="Горожанин"></i>
    # #            <a onclick="return AngryAjax.goToUrl(this, event);" href="http://www.moswar.ru/player/38325/"> savteam</a>
    # #            <span class="level">[7]</span>
    # #        </span>
    # #      </div>""")
    # from PySide.QtCore import *
    # timer = QTimer()
    # timer.setSingleShot(True)
    # timer.start(3000)
    # loop = QEventLoop()
    # timer.timeout.connect(loop.quit)
    # loop.exec_()
    #
    # doc = view.page().mainFrame().documentElement()
    # print(doc.findFirst('head title').toPlainText())
