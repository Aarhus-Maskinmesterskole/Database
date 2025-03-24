# db.py

import mariadb

HOST = "localhost"
USER = "workshop_user"
PASSWORD = "secretpassword"
DATABASE = "workshop_db"


def get_connection():
    """Opretter og returnerer en databaseforbindelse"""
    try:
        conn = mariadb.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        return conn
    except mariadb.Error as e:
        print(f"DB Forbindelses-fejl: {e}")
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
        email VARCHAR(50)
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()


def create_user(name, email):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()

    cursor.close()
    conn.close()


def get_all_users():
    conn = get_connection()
    if not conn:
        return []
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email FROM users")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


def update_user(user_id, new_name, new_email):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET name=?, email=? WHERE id=?", (new_name, new_email, user_id))
    conn.commit()

    cursor.close()
    conn.close()


def delete_user(user_id):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()

    cursor.close()
    conn.close()
