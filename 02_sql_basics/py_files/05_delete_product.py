"""
Opgave 5: Slet ét produkt fra tabellen.
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
        cursor.execute("""
            DELETE FROM products
            WHERE product_name = 'Hammer';
        """)
        print("Produkt slettet.")
    conn.commit()
finally:
    conn.close()
