from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import sqlite3
from GlavMenu import Ui_MainWindow as main_interface
from DiaKli import Ui_Dialog_Kli as klient_interface
from DiaPut import Ui_Dialog_Put as putevka_interface
from DiaZak import Ui_Dialog_Zak as zakaz_interface

class klient_window(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = klient_interface()
        self.ui.setupUi(self)



class putevka_window(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = putevka_interface()
        self.ui.setupUi(self)



class zakaz_window(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = zakaz_interface()
        self.ui.setupUi(self)

class main_window(QMainWindow):        # ИЗМЕНЕНО: QMainWindow вместо QWidget
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)  # ИЗМЕНЕНО: QMainWindow.__init__
        self.ui = main_interface()
        self.ui.setupUi(self)

        self.read_turistputevki()
        self.ui.comboBox.currentIndexChanged.connect(self.Vibor)
        self.ui.pushButton.clicked.connect(self.open_add_form)
        self.ui.tableWidget.itemClicked.connect(self.open_update_form)

    def open_add_form(self):  
        selected_text = self.ui.comboBox.currentText()
        if selected_text == "Путевки":
            self.add_form = putevka_window(self)
            self.add_form.exec()
            
        elif selected_text == "Туристы":
            self.add_form = klient_window(self)
            self.add_form.exec()
            
        elif selected_text == "Заказы":
            self.add_form = zakaz_window(self)
            self.add_form.exec()


    def open_update_form(self):  
        selected_text = self.ui.comboBox.currentText()
        if selected_text == "Путевки":
            self.update_form = putevka_window(self)
            self.update_form.exec()

            
        elif selected_text == "Туристы":
            self.update_form = klient_window(self)
            self.update_form.exec()

            
        elif selected_text == "Заказы":
            self.update_form = zakaz_window(self)
            self.update_form.exec()


    def Vibor(self, index):
        selected_text = self.ui.comboBox.currentText()
        
        # Очищаем таблицу
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(0)
        
        # Вызываем соответствующую функцию в зависимости от выбора
        if selected_text == "Путевки":
            self.read_turistputevki()
        elif selected_text == "Туристы":
            self.read_klienti()
        elif selected_text == "Заказы":
            self.read_zakaz()

    def read_klienti(self):
        # Получаем данные из таблицы klienti
        cursor.execute('SELECT * FROM klienti')
        klienti_data = cursor.fetchall()
        
        if not klienti_data:
            print("Нет данных в таблице клиентов")
            return
        
        # Устанавливаем количество строк и столбцов
        self.ui.tableWidget.setRowCount(len(klienti_data))
        self.ui.tableWidget.setColumnCount(6)  # 6 столбцов в таблице
        
        # Устанавливаем заголовки столбцов
        headers = ["Код туриста", "Фамилия", "Имя", "Отчество", "Адрес", "Город"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        
        # Заполняем таблицу данными
        for row, record in enumerate(klienti_data):
            for col in range(6):
                item = QTableWidgetItem(str(record[col]))
                self.ui.tableWidget.setItem(row, col, item)
        
        # Автоматически подгоняем размер колонок
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()

    def read_turistputevki(self):
        # Очищаем таблицу
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(3)  # Убедимся, что есть 3 колонки
        
        # Устанавливаем заголовки
        self.ui.tableWidget.setHorizontalHeaderLabels(["Информация о путевке", "Скидка", "Фото"])
        try:
            cursor.execute('SELECT * FROM turistputevki')
            self.tur_data = cursor.fetchall()
            
            if not self.tur_data:
                print("Нет данных для отображения!")
                return
                
            self.ui.tableWidget.setRowCount(len(self.tur_data))
            self.ui.tableWidget.setColumnCount(3)  # Добавляем 3-й столбец для фото
            
            for row, record in enumerate(self.tur_data):
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

                    pixmap = QPixmap('Putevka.png')
                    if pixmap.isNull():
                        print("Ошибка загрузки изображения Putevka.png")
                        # Создаем пустое изображение с текстом
                        pixmap = QPixmap(100, 100)
                        pixmap.fill(Qt.gray)

                    pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)

                    # Добавляем фото в 3-й столбец
                    photo_item = QTableWidgetItem()
                    photo_item.setFlags(photo_item.flags() & ~Qt.ItemIsEditable)  # Запрещаем редактирование
                    
                    # Создаем label с изображением
                    photo_label = QLabel()
                    photo_label.setPixmap(pixmap)
                    photo_label.setAlignment(Qt.AlignCenter)
                    
                    # Устанавливаем label в ячейку
                    self.ui.tableWidget.setCellWidget(row, 2, photo_label)
                    
                except IndexError as e:
                    print(f"Ошибка индекса в записи {row}: {e}")
                    continue
            
            # Автоматически подгоняем размер колонок
            self.ui.tableWidget.resizeColumnsToContents()
            self.ui.tableWidget.resizeRowsToContents()
            
        except Exception as e:
            print(f"Общая ошибка: {e}")
    def read_zakaz(self):
        # Получаем данные из таблицы zakaz с JOIN для отображения названий вместо ID
        cursor.execute('SELECT * FROM zakaz')
        zakaz_data = cursor.fetchall()
        
        if not zakaz_data:
            print("Нет данных в таблице заказов")
            return
        
        # Устанавливаем количество строк и столбцов
        self.ui.tableWidget.setRowCount(len(zakaz_data))
        self.ui.tableWidget.setColumnCount(5)  # 5 столбцов
        
        # Устанавливаем заголовки столбцов
        headers = ["ID заказа", "Турист", "Путевка (страна)", "Кол-во людей", "Дата прибытия"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        
        # Заполняем таблицу данными
        for row, record in enumerate(zakaz_data):
            for col in range(5):
                item = QTableWidgetItem(str(record[col]))
                self.ui.tableWidget.setItem(row, col, item)
        
        # Автоматически подгоняем размер колонок
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()

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

