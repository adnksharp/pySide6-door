# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, QEvent, QTimer

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from log_ui import Ui_Widget as Ui_History

class Keyboard(QObject):
    def eventFilter(self, widget, event):
        if event.type() == QEvent.KeyRelease:
            if event.text().isdigit():
                widget.addCode(event.text())
        return False                

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        self.code = ''
        
        self.eventFilter = Keyboard(parent = self)
        self.installEventFilter(self.eventFilter)
        
    def addCode(self, k):
        self.code += str(k)
        print(self.code)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
