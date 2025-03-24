"""
Opgave 6 (tilvalg): Søg i produktnavne med LIKE.
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
        søgeord = "%skruetrækker%"
        cursor.execute("SELECT * FROM products WHERE product_name LIKE %s;", (søgeord,))
        results = cursor.fetchall()
        for row in results:
            print(row)
finally:
    conn.close()
