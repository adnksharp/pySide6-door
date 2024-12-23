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
            if event.text() == '\b':
                widget.delCode()
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
        
        self.ui.b.clicked.connect(lambda x: self.addCode(0))
        self.ui.b_1.clicked.connect(lambda x: self.addCode(1))
        self.ui.b_2.clicked.connect(lambda x: self.addCode(2))
        self.ui.b_3.clicked.connect(lambda x: self.addCode(3))
        self.ui.b_4.clicked.connect(lambda x: self.addCode(4))
        self.ui.b_5.clicked.connect(lambda x: self.addCode(5))
        self.ui.b_6.clicked.connect(lambda x: self.addCode(6))
        self.ui.b_7.clicked.connect(lambda x: self.addCode(7))
        self.ui.b_8.clicked.connect(lambda x: self.addCode(8))
        self.ui.b_9.clicked.connect(lambda x: self.addCode(9))
        
    def addCode(self, k):
        self.code += str(k)
        
    def delCode(self):
        self.code = self.code[:-1]
        
    def updates(self):
        self.ui.lcdNumber.display(self.code)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
