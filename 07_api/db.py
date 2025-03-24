"""db.py

Dette modul indeholder grundlæggende databasefunktioner til at forbinde til MariaDB
og foretage CRUD-operationer på en simpel `users`-tabel. Det er tiltænkt brug i kombination
med et Flask-API (app.py) i 07_api-mappen.
"""

import mariadb

# Ret evt. konfigurationen (host, user, password, database) til dit setup
HOST = "localhost"
USER = "workshop_user"
PASSWORD = "secretpassword"
DATABASE = "workshop_db"


def get_connection():
    """Opretter og returnerer en databaseforbindelse til MariaDB."""
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
    """Opretter en simpel users-tabel, hvis den ikke findes."""
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL
        )
        """
    )

    conn.commit()
    cursor.close()
    conn.close()


def create_user(name, email):
    """Indsætter en ny bruger i users-tabellen."""
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
    except mariadb.Error as e:
        print("Fejl ved INSERT:", e)
    finally:
        cursor.close()
        conn.close()


def get_user_by_id(user_id):
    """Henter en enkelt bruger- række baseret på ID."""
    conn = get_connection()
    if not conn:
        return None
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, name, email FROM users WHERE id=?", (user_id,))
        row = cursor.fetchone()
        return row
    except mariadb.Error as e:
        print("Fejl ved SELECT:", e)
        return None
    finally:
        cursor.close()
        conn.close()


def get_all_users():
    """Henter alle brugere i en liste af tuples (id, name, email)."""
    conn = get_connection()
    if not conn:
        return []
    cursor = conn.cursor()
    rows = []
    try:
        cursor.execute("SELECT id, name, email FROM users")
        rows = cursor.fetchall()
    except mariadb.Error as e:
        print("Fejl ved SELECT:", e)
    finally:
        cursor.close()
        conn.close()
    return rows


def update_user(user_id, new_name, new_email):
    """Opdaterer en bruger baseret på ID."""
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET name=?, email=? WHERE id=?", (new_name, new_email, user_id))
        conn.commit()
    except mariadb.Error as e:
        print("Fejl ved UPDATE:", e)
    finally:
        cursor.close()
        conn.close()


def delete_user(user_id):
    """Sletter en bruger baseret på ID."""
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
    except mariadb.Error as e:
        print("Fejl ved DELETE:", e)
    finally:
        cursor.close()
        conn.close()


def search_users_by_name(search_term):
    """Returnerer alle brugere hvor navnet matcher en delstreng."""
    conn = get_connection()
    if not conn:
        return []
    cursor = conn.cursor()
    results = []
    try:
        query = "SELECT id, name, email FROM users WHERE name LIKE ?"
        cursor.execute(query, (f"%{search_term}%",))
        results = cursor.fetchall()
    except mariadb.Error as e:
        print("Fejl ved SEARCH:", e)
    finally:
        cursor.close()
        conn.close()
    return results
