"""
Opgave 1: Opret en tabel 'products' med felter:
- id (INT, AUTO_INCREMENT, PRIMARY KEY)
- product_name (VARCHAR)
- price (DECIMAL)
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
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_name VARCHAR(100),
                price DECIMAL(10,2)
            );
        """)
        print("Tabel 'products' er oprettet.")
    conn.commit()
finally:
    conn.close()
