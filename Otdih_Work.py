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

        self.read_turistputevki()

    def read_turistputevki(self):
        # Очищаем таблицу
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(2)  # Убедимся, что есть 2 колонки
        
        # Устанавливаем заголовки
        self.ui.tableWidget.setHorizontalHeaderLabels(["Информация о путевке", "Скидка"])
        
        # Получаем данные
        try:
            cursor.execute('SELECT * FROM turistputevki')
            self.tur_data = cursor.fetchall()
            print(f"Получено записей: {len(self.tur_data)}")
            
            if not self.tur_data:
                print("Нет данных для отображения!")
                return
                
            self.ui.tableWidget.setRowCount(len(self.tur_data))
            
            for row, record in enumerate(self.tur_data):
                # Проверяем структуру записи
                print(f"Запись {row}: {record}")
                
                # Формируем текст с проверкой индексов
                try:
                    strana = record[1] if len(record) > 1 else "Н/Д"
                    data_start = record[2] if len(record) > 2 else "Н/Д"
                    data_end = record[3] if len(record) > 3 else "Н/Д"
                    komnat = record[4] if len(record) > 4 else 0
                    pitanie = record[5] if len(record) > 5 else 0
                    kult = record[6] if len(record) > 6 else 0
                    price = record[7] if len(record) > 7 else 0
                    
                    pitanie_text = "с питанием" if pitanie == 1 else "без питания"
                    kult_text = "с культурной программой" if kult == 1 else "без культурной программы"
                    
                    text = (f"{strana} | {data_start} - {data_end}\n"
                           f"Комнат: {komnat}, {pitanie_text}, {kult_text}\n"
                           f"Стоимость за сутки: {price} руб.")
                    
                    # Первая колонка - информация
                    item1 = QTableWidgetItem(text)
                    self.ui.tableWidget.setItem(row, 0, item1)
                    
                    # Вторая колонка - скидка
                    item2 = QTableWidgetItem()
                    if price < 2000:
                        item2.setText('0%')
                    elif price < 3000:
                        item2.setText('3%')
                    elif price < 4000:
                        item2.setText('5%')
                    elif price < 5000:
                        item2.setText('8%')
                    else:
                        item2.setText('10%')
                    
                    self.ui.tableWidget.setItem(row, 1, item2)
                    
                except IndexError as e:
                    print(f"Ошибка индекса в записи {row}: {e}")
                    continue
            
            # Автоматически подгоняем размер колонок
            self.ui.tableWidget.resizeColumnsToContents()
            self.ui.tableWidget.resizeRowsToContents()
            
        except Exception as e:
            print(f"Общая ошибка: {e}")

if __name__ == "__main__": 
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

