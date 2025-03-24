#Advarsel: Brug kun dette på testmaskiner. På produktionssystemer bør adgangskoder ændres manuelt og logges korrekt.
import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="gammelKode"  # ← Skift denne
)

try:
    with connection.cursor() as cursor:
        cursor.execute("ALTER USER 'root'@'localhost' IDENTIFIED BY 'nyKode123';")
        print("Adgangskode ændret.")
    connection.commit()
finally:
    connection.close()
