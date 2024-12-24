# This Python file uses the following encoding: utf-8
import sys
from random import randint as random
import smtplib as smtp
from time import strftime as time
# import notifypy as noty
from dotenv import load_dotenv as env
from os import getenv
from email.mime.multipart import MIMEMultipart as multipart
from email.mime.text import MIMEText as text
from ssl import create_default_context as myssl
from pymata4.pymata4 import Pymata4 as arduino
from pymongo import MongoClient as mongose

from PySide6.QtWidgets import QApplication, QWidget, QListWidget
from PySide6.QtCore import QObject, QEvent, QTimer

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from ui_log import Ui_Widget as Ui_History

class DB():
    def __init__(self, host = 'mongodb://localhost:27017/', server = 'Arduino', db = 'door'):
        srv = mongose(host)
        mydb = srv[server]
        self.collections = mydb[db]
        
    def add(self, done):
        data = {
            'data': time("%Y-%m-%d, %A, %H:%M:%S"),
            'done': done
        }
        self.collections.insert_one(data)
        
    def get(self):
        return [i for i in self.collections.find()]

class Board():
    def __init__(self, *pin):
        self.ino = arduino()
        self.door = pin[0]
        self.led = [pin[1], pin[2]]
        for i in pin:
            self.ino.set_pin_mode_digital_output(i)
        self.b = False
    
    def on(self, state):
        self.ino.digital_pin_write(self.door, state)
        self.ino.digital_pin_write(self.led[0], not state)
        self.ino.digital_pin_write(self.led[1], state)
        
    def blink(self):
        self.ino.digital_pin_write(self.led[1], self.b)
        self.b = not self.b

class Email():
    def __init__(self, parent = None):
        self.widget = parent
        pass
        
    def send(self):
        if self.widget.paswd == 'X':
            self.widget.paswd = None
            env()
            email = getenv('FROM')
            to = getenv('TO')
            host = getenv('SSL_HOST')
            port = getenv('SSL_PORT')
        
            parts = multipart()
            pasw = random(1*10**5, 1*10**6)
        
            body = f'''
            <html>
                <body>
                    <h3>Hemos recibido una solicitud para acceder a tu puerta</h3>
                    <p>Para acceder ingresa el siguiente código:</p>
                    <span style="font-weight:bold">
                        {pasw}
                    </span>
                    <p>Si no fuiste tú quien realizó esta acción, ignora este correo</p>

                    <h5>Este correo electrónico fue generado automáticamente.</h5>
                </body>
            </html>
            '''
        
            parts['From'] = email
            parts['To'] = to
            parts['Subject'] = 'Tu clave de acceso'
        
            parts.attach(text(body, 'html'))
        
            context = myssl()
        
            with smtp.SMTP_SSL(host, port, context=context) as service:
                service.login(email, getenv('PASSWORD'))
                service.sendmail(email, to, parts.as_string())
            
            self.widget.paswd = pasw

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
        # selenoid, lock, unlock leds
        self.board = Board(13, 2, 3)
        self.board.on(False)
        
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        self.h = History()
        
        self.code = ''
        self.paswd = 'X'
        self.toclose = 5
        
        self.eventFilter = Keyboard(parent = self)
        self.installEventFilter(self.eventFilter)
        
        self.email = Email(self)
        
        self.db = DB()
        
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
        self.ui.pushButton.clicked.connect(self.delCode)
        self.ui.open.clicked.connect(self.email.send)
        self.ui.log.clicked.connect(self.showH)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.closing)
        
    def addCode(self, k):
        if len(self.code) < 6:
            self.code += str(k)
        self.updates()
        
    def delCode(self):
        self.code = self.code[:-1]
        self.updates()
        
    def updates(self):
        self.ui.lcdNumber.display(self.code)
        if len(self.code) == 6:
            self.db.add(str(self.paswd) == self.code)
            if  str(self.paswd) == self.code:
                print('pass')
                self.ui.label.setText('Acceso concedido')
                self.timer.start(1000)
                self.paswd = 'X'
                self.board.on(True)
            else:
                self.ui.label.setText('Acceso denegado')
                self.board.on(False)
            self.code = ''
            self.ui.lcdNumber.display('')
            self.updateList()

    def  closing(self):
        if self.toclose > 0:
            self.ui.label.setText(f'Acceso concedido ({self.toclose}s)')
            self.toclose -= 1
            self.board.blink()
        else:
            self.toclose = 5
            self.ui.label.setText('')
            self.timer.stop()
            self.board.on(False)
            
    def closeEvent(self, event):
        self.board.ino.shutdown()
        self.h.close()
        return super().closeEvent(event)
    
    def updateList(self):
        data = self.db.get()
        self.h.ui.listWidget.clear()
        for d in data:
            self.h.ui.listWidget.addItem(f'Fecha: {d['data']}\tAcceso: {'concedido' if d['done'] else 'denegado'}')
    
    def showH(self):
        self.updateList()
        self.h.show()        

class History(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_History()
        self.ui.setupUi(self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
