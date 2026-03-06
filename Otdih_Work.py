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

    def read_turistputevki(self):
        # функция для обновления данных таблицы на главном экране
        self.ui.tableWidget.setRowCount(0)  # убрали старые строки из таблицы
        
        # Получаем все данные из таблицы turistputevki
        cursor.execute('SELECT * FROM turistputevki ORDER BY idTuristPutevki')
        self.turistputevki_data = cursor.fetchall()
        
        # Устанавливаем количество строк в таблице
        self.ui.tableWidget.setRowCount(len(self.turistputevki_data))
        
        # Заполняем таблицу данными
        for row in range(len(self.turistputevki_data)):
            data = self.turistputevki_data[row]
            
            # Формируем текст для отображения
            text = (f"{data[1]} | Страна: {data[1]}\n"  # Strana
                    f"Даты: {data[2]} - {data[3]}\n"     # DataFirstDayOtdiha - DataLastDayOtdiha
                    f"Комнат: {data[4]}\n"                # KolichestvoKomnat
                    f"Питание: {'Да' if data[5] == 1 else 'Нет'}\n"  # Pitanie
                    f"Культ. программа: {'Да' if data[6] == 1 else 'Нет'}\n"  # KulturnayaProgramma
                    f"Стоимость за сутки: {data[7]} руб.")
            
            # Создаем элемент и устанавливаем текст
            item = QTableWidgetItem()
            item.setText(text)
            self.ui.tableWidget.setItem(row, 0, item)
            
            # Добавляем информацию о стоимости в отдельную колонку
            price_item = QTableWidgetItem()
            price_item.setText(f"{data[7]} руб/сутки")
            self.ui.tableWidget.setItem(row, 1, price_item)
            
            # Добавляем информацию о количестве дней
            # Вычисляем количество дней между датами
            from datetime import datetime
            date_start = datetime.strptime(data[2], '%Y-%m-%d')
            date_end = datetime.strptime(data[3], '%Y-%m-%d')
            days_count = (date_end - date_start).days + 1
            
            days_item = QTableWidgetItem()
            days_item.setText(f"{days_count} дней")
            self.ui.tableWidget.setItem(row, 2, days_item)
            
            # Общая стоимость тура
            total_price = days_count * data[7]
            total_item = QTableWidgetItem()
            total_item.setText(f"Итого: {total_price} руб.")
            self.ui.tableWidget.setItem(row, 3, total_item)

if __name__ == "__main__":  # Хорошая практика
    app = QApplication(sys.argv)

    # Выбор стиля
    QApplication.setStyle(QStyleFactory.create("Fusion"))

    # Создание и настройка палитры
    pal = QApplication.palette()

    # Цвет основного фона
    pal.setColor(QPalette.Window, QColor('#FFFFFF'))
    # Цвет дополнительного фона (кнопки)
    pal.setColor(QPalette.Button, QColor('#67BA80'))
    # Цвет акцентирования внимания (поля ввода)
    pal.setColor(QPalette.Base, QColor('#F4E8D3'))

    # Установка созданной палитры
    QApplication.setPalette(pal)

    # Создание и установка нужного шрифта
    font = QFont('Segoe UI', 12)
    QApplication.setFont(font)
    
    conn = sqlite3.connect('otdih_savinih.db')
    cursor = conn.cursor()
    
    main_form = main_window()
    main_form.show()
    
    sys.exit(app.exec_())
    
    cursor.close()
    conn.close()

