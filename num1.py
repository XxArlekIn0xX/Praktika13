import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

##cursor.execute('''
##CREATE TABLE IF NOT EXISTS Users (
##id INTEGER PRIMARY KEY,
##username TEXT NOT NULL,
##email TEXT NOT NULL,
##age INTEGER
##)
##''')

##cursor.execute('CREATE INDEX idx_email ON Users (email)')

##cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'neuser@example.com', 28))
##cursor.execute('UPDATE Users SET age = ? WHERE username = ? ', (29, 'newuser'))
##cursor.execute('DELETE FROM Users WHERE username = ? ', ('newuser',))
##cursor.execute('SELECT * FROM Users')
##users = cursor.fetchall()
##for user in users:
##    print(user)
##cursor.execute('SELECT Username, age FROM Users WHERE age > ?', (25,))
##cursor.execute('SELECT AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
##cursor.execute('SELECT Username, age FROM Users GROUP BY age HAVING AVG(age) > ? ORDER BY age DESC', (30,))
##results = cursor.fetchall()
##for row in results:
##    print(row)

##cursor.execute('SELECT COUNT(*) FROM Users')
##total_users = cursor.fetchone()[0]
##print('Общее количество пользователей:', total_users)

##cursor.execute('SELECT SUM(age) FROM Users')
##total_age = cursor.fetchone()[0]
##print('Общая сумма возрастов пользователей: ', total_age)

##cursor.execute('SELECT AVG(age) FROM Users')
##average_age = cursor.fetchone()[0]
##print('Средний возраст пользователей:', average_age)

##cursor.execute('SELECT MIN(age)  FROM Users')
##min_age = cursor.fetchone()[0]
##print('Минимальный возраст среди пользователей:',min_age)

##cursor.execute('SELECT MAX(age)  FROM Users')
##max_age = cursor.fetchone()[0]
##print('Максимальный возраст среди пользователей:',max_age)

##cursor.execute('SELECT * FROM Users')
##users = cursor.fetchall()
##for user in users:
##    print(user)

##cursor.execute('SELECT * FROM Users')
##first_user = cursor.fetchone()
##print(first_user)
##
##print("=" * 30)
##
##
##cursor.execute('SELECT * FROM Users')
##first_five_users = cursor.fetchmany(5)
##print(first_five_users)
##
##print("=" * 30)
##
##cursor.execute('SELECT * FROM Users')
##all_users = cursor.fetchall()
##print(all_users)

##cursor.execute('SELECT * FROM Users')
##users = cursor.fetchall()
##
##users_list = []
##for user in users:
##    user_dict = {
##        'id': user[0],
##        'username': user[1],
##        'email': user[2],
##        'age': user[3]
##    }
##    users_list.append(user_dict)
##
##for user in users_list:
##    print(user)

##cursor.execute('SELECT * FROM Users WHERE age IS NULL')
##unknown_age_users = cursor.fetchall()
##
##for user in unknown_age_users:
##    print(user)

try:
    # Начинаем транзакцию
    cursor.execute('BEGIN')

    # Выполняем операции
    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user1', 'user1@example.com'))
    cursor.execute('INSERT INTO Users (username, email) VALUES (?, ?)', ('user2', 'user2@example.com'))

    # Подтверждаем изменения
    cursor.execute('COMMIT')

except:
    # Отменяем транзакцию в случае ошибки
    cursor.execute('ROLLBACK')

connection.commit()
connection.close()
