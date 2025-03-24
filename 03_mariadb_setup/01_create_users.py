import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='dit_root_kodeord'
)

try:
    with connection.cursor() as cursor:
        cursor.execute("CREATE USER 'nybruger'@'localhost' IDENTIFIED BY 'kode123';")
        cursor.execute("GRANT SELECT, INSERT ON workshop_db.* TO 'nybruger'@'localhost';")
        cursor.execute("FLUSH PRIVILEGES;")
        print("Bruger oprettet og rettigheder tildelt.")
    connection.commit()
finally:
    connection.close()
