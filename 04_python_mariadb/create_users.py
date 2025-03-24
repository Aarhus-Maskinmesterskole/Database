"""
create_users.py

Formål: Forbinder til databasen, opretter en users-tabel, indsætter data og henter dem.
"""

import mariadb

HOST = "localhost"
USER = "workshop_user"
PASSWORD = "secretpassword"
DATABASE = "workshop_db"

def get_connection():
    try:
        return mariadb.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
    except mariadb.Error as e:
        print(f"Forbindelsesfejl: {e}")
        return None

def create_users_table():
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        email VARCHAR(100)
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()

def insert_users():
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Charlie', 'charlie@example.com')
    """)

    conn.commit()
    cursor.close()
    conn.close()

def select_users():
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_users_table()
    insert_users()
    select_users()
