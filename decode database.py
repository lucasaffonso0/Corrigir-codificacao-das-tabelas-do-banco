import mysql.connector

banco = {
    'host' : 'localhost', # Database Hostname
    'user' : 'root',      # Database Username
    'password' : 'root'   # Database Password
}

banco = mysql.connector.connect(**banco)

cursor = banco.cursor()

db_name = 'my_database_name' # Database Name

cursor.execute(f"use {db_name}")
cursor.execute(f"SELECT DISTINCT TABLE_NAME FROM information_schema.`COLUMNS` WHERE TABLE_SCHEMA = '{db_name}';")
for table in cursor.fetchall():
    table = table[0]
    cursor.execute(f"SELECT COLUMN_NAME FROM information_schema.`COLUMNS` WHERE TABLE_NAME = '{table}';")
    for coluna in cursor.fetchall():
        coluna = coluna[0]
        try:
            cursor.execute(f'UPDATE {table} SET {coluna} = CONVERT(CAST({coluna} AS BINARY) USING UTF8);')
            banco.commit()
        except Exception:
            pass
