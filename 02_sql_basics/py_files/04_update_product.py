"""
Opgave 4: Skift navnet på ét produkt.
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
            UPDATE products
            SET product_name = 'Elektrisk Skruetrækker'
            WHERE product_name = 'Skruetrækker';
        """)
        print("Produktnavn opdateret.")
    conn.commit()
finally:
    conn.close()
