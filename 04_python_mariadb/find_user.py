name_input = input("Indtast navn, du vil søge efter: ")
conn = get_connection()
cursor = conn.cursor()

query = "SELECT * FROM users WHERE name = ?"
cursor.execute(query, (name_input,))
result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
conn.close()
