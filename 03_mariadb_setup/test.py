import pymysql

connection = pymysql.connect(
    host='localhost',
    user='nybruger',
    password='kode123',
    database='workshop_db'
)

try:
    with connection.cursor() as cursor:
        try:
            cursor.execute("DROP TABLE IF EXISTS test_table;")
            print("DROP TABLE lykkedes.")
        except Exception as e:
            print(f"DROP TABLE fejlede: {e}")

        try:
            cursor.execute("DELETE FROM test_table;")
            print("DELETE lykkedes.")
        except Exception as e:
            print(f"DELETE fejlede: {e}")
finally:
    connection.close()
