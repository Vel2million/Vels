import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_tbl_stmt = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_tbl_stmt)

user = (1, 'tj', 'sadas')
inst_stmt = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(inst_stmt, user)

connection.commit()
connection.close()