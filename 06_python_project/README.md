# 06 Python Project: CRUD-applikation

> **Formål**: Byg et lille Python-projekt, der demonstrerer Create, Read, Update og Delete (CRUD) med MariaDB. Her samles erfaringer fra de forrige moduler.

## 📝 Indhold
1. [Introduktion](#introduktion)
2. [Projektstruktur](#projektstruktur)
3. [Opret hovedfil og databasefunktioner](#opret-hovedfil-og-databasefunktioner)
4. [CRUD-operationer](#crud-operationer)
5. [Menufunktion (CLI)](#menufunktion-cli)
6. [Kør og test](#kør-og-test)
7. [Øvelser og udvidelser](#øvelser-og-udvidelser)
8. [Videre](#videre)

---

## Introduktion
Nu kombinerer vi dine færdigheder i Python og MariaDB til at lave en **enkel CRUD-applikation** (Create, Read, Update, Delete). Den vil køre i terminalen (CLI) og tillade dig at tilføje, se, opdatere og slette data i en tabel.

---

## Projektstruktur
Du kan fx organisere filerne sådan:
```
06_python_project/
├─ README.md            # Dette dokument
├─ main.py              # Indeholder menufunktionalitet og kalder db-funktioner
└─ db.py                # Indeholder databaseforbindelse og CRUD-funktioner
```

---

## Opret hovedfil og databasefunktioner

1. **`db.py`**: Her oprettes en funktion, der laver en forbindelse til MariaDB, samt funktioner til at oprette en tabel, udføre CRUD osv.
2. **`main.py`**: Her har du en simpel menustruktur, der spørger brugeren, hvad de vil gøre (Opret, Se, Opdatér, Slet, Afslut).

### Eksempel på `db.py`
```python
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
```

---

## CRUD-operationer
- **Create**: `create_user(name, email)`
- **Read**: `get_all_users()`
- **Update**: `update_user(user_id, new_name, new_email)`
- **Delete**: `delete_user(user_id)`

I eksemplet ovenfor er `get_all_users()` en simpel "Read"-funktion. Du kan også tilføje en funktion til at hente én bruger ad gangen, hvis du har brug for det.

---

## Menufunktion (CLI)

### Eksempel på `main.py`
```python
# main.py

import db

# Opret først tabellen, hvis den ikke findes
print("Opretter (hvis nødvendigt) tabel...")
db.create_users_table()


def run_menu():
    while True:
        print("\n*** MENUMENU ***")
        print("1) Opret bruger")
        print("2) Se alle brugere")
        print("3) Opdater bruger")
        print("4) Slet bruger")
        print("5) Afslut")

        valg = input("Vælg et nummer: ")
        if valg == "1":
            name = input("Navn: ")
            email = input("Email: ")
            db.create_user(name, email)
            print("Bruger oprettet!")
        elif valg == "2":
            users = db.get_all_users()
            for u in users:
                print(u)
        elif valg == "3":
            user_id = input("Id på den bruger, der skal opdateres: ")
            new_name = input("Nyt navn: ")
            new_email = input("Ny email: ")
            db.update_user(user_id, new_name, new_email)
            print("Bruger opdateret!")
        elif valg == "4":
            user_id = input("Id på den bruger, der skal slettes: ")
            db.delete_user(user_id)
            print("Bruger slettet!")
        elif valg == "5":
            print("Farvel!")
            break
        else:
            print("Ugyldigt valg!")

if __name__ == "__main__":
    run_menu()
```

---

## Kør og test
1. Navigér til mappen `06_python_project`.
2. Sørg for at have installeret `mariadb`-driveren (modul 04).
3. Kør:
   ```bash
   python main.py
   ```
4. Test menupunkterne:
   - Opret 1-2 brugere.
   - Se dem på listen.
   - Opdater evt. en af dem.
   - Slet en af dem.

---

## Øvelser og udvidelser
1. **Brugerinput-fejl**: Sørg for at fange fejl, hvis brugeren indtaster ugyldige data (fx en streng, når der forventes et tal).
2. **Validering**: Tjek om email har korrekt format (kun basalt).
3. **Vis bruger**: Lav en funktion, der henter én bruger ud fra ID, og tilføj den som menupunkt.
4. **Søgning**: Lav et menupunkt, hvor brugeren indtaster et søgeord, og du viser alle brugere, hvis navn matcher.
5. **Logging**: Log fejl til en fil.
6. **Tabeller**: Opret en ekstra tabel (fx `orders`) og lav menupunkter til at håndtere ordrer.

---

## Videre
Nu har du en lille, men fungerende CLI CRUD-applikation i Python, der benytter MariaDB i baggrunden. 

**👉 Videre til (evt.) 07_api** for at udvide projektet til et simpelt REST-API med Python.

