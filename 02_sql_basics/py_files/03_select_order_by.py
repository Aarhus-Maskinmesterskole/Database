"""
Opgave 3: Hent alle produkter og sorter efter pris (stigende).
"""

import pymysql

conn = pymysql.connect(
    host='localhost',
    user='workshop_user',
    password='din_kode',
    database='workshop_db'
)

try:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM products ORDER BY price ASC;")
        results = cursor.fetchall()
        for row in results:
            print(row)
finally:
    conn.close()
