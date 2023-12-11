import sys
from PySide6.QtWidgets import QApplication
from view import View
from life_processing import Country_Life


def main():
    core = Country_Life('Россия', 'Владимир Путин')
    app = QApplication(sys.argv)
    window = View(core)
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
