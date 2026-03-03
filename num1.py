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

cursor.execute('SELECT SUM(age) FROM Users')
total_age = cursor.fetchone()[0]
print('Общая сумма возрастов пользователей: ', total_age)

connection.commit()
connection.close()
