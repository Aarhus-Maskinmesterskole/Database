try:
    cursor.execute("SELEKT * FROM users")  # Bevidst fejl i 'SELECT'
except mariadb.Error as e:
    print("Databasefejl fanget:", e)
