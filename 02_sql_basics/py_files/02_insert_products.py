"""
Opgave 2: Indsæt mindst 3 produkter i 'products'-tabellen.
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
        cursor.executemany("""
            INSERT INTO products (product_name, price)
            VALUES (%s, %s);
        """, [
            ("Skruetrækker", 49.95),
            ("Hammer", 79.50),
            ("Boremaskine", 499.00)
        ])
        print("3 produkter er indsat.")
    conn.commit()
finally:
    conn.close()
