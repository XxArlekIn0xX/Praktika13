from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import sqlite3
from GlavMenu import Ui_MainWindow as main_interface

class main_window(QMainWindow):        # ИЗМЕНЕНО: QMainWindow вместо QWidget
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)  # ИЗМЕНЕНО: QMainWindow.__init__
        self.ui = main_interface()
        self.ui.setupUi(self)

if __name__ == "__main__":  # Хорошая практика
    app = QApplication(sys.argv)
    
    conn = sqlite3.connect('otdih_savinih.db')
    cursor = conn.cursor()
    
    main_form = main_window()
    main_form.show()
    
    sys.exit(app.exec_())
    
    cursor.close()
    conn.close()

