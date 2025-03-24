# 07 API (valgfri)

> **Formål**: Byg et simpelt REST-API i Python, der gør CRUD-funktioner i MariaDB tilgængelige over HTTP.

## 📝 Indhold
1. [Introduktion](#introduktion)
2. [Installation og opsætning](#installation-og-opsætning)
3. [Projektstruktur](#projektstruktur)
4. [Eksempel på Flask-API](#eksempel-på-flask-api)
5. [Kørsel og test](#kørsel-og-test)
6. [Øvelser](#øvelser)
7. [Videre](#videre)

---

## Introduktion
Dette modul viser, hvordan du kan bygge et **REST-API** oven på din eksisterende database og Python-kode, så du kan tilgå og manipulere dine data via HTTP. Du kan bruge **Flask** eller **FastAPI** – her vises Flask som eksempel.

---

## Installation og opsætning

1. **Forudsætninger**: Du bør have gennemgået modulerne om Python, SQL, MariaDB og gerne have en simpel CRUD-funktionalitet klar (jf. `db.py`).
2. **Installer Flask**:
   ```bash
   pip install flask
   ```
3. **Valgfrit**: Installer en REST-klient som Postman eller brug `curl`/`httpie` til at teste.

---

## Projektstruktur
Du kan vælge at udvide din eksisterende mappestruktur:

```
07_api/
├─ README.md              # Dette dokument
├─ app.py                 # Flask API (eller FastAPI)
└─ db.py                  # Evt. genbrug fra modul 06 (crud-funktioner)
```

Du kan også placere `app.py` ved siden af dine andre filer, men for overskuelighedens skyld er det fint at have en dedikeret mappe.

---

## Eksempel på Flask-API

Nedenfor er et helt simpelt eksempel, der giver en CRUD-API for "users".

```python
# app.py

from flask import Flask, request, jsonify
import mariadb
import db  # Antag, at du har en db.py med get_connection() osv.

app = Flask(__name__)

# Hent alle brugere
@app.route("/users", methods=["GET"])
def get_users():
    conn = db.get_connection()
    if not conn:
        return jsonify({"error": "DB connection error"}), 500
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    # Omform til en liste af dicts for JSON
    users = []
    for (user_id, name, email) in rows:
        users.append({"id": user_id, "name": name, "email": email})

    return jsonify(users), 200

# Opret ny bruger
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "name and email are required"}), 400

    conn = db.get_connection()
    if not conn:
        return jsonify({"error": "DB connection error"}), 500
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        new_id = cursor.lastrowid
    except mariadb.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify({"id": new_id, "name": name, "email": email}), 201

# Hent én bruger
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    conn = db.get_connection()
    if not conn:
        return jsonify({"error": "DB connection error"}), 500
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users WHERE id=?", (user_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row:
        (u_id, name, email) = row
        return jsonify({"id": u_id, "name": name, "email": email}), 200
    else:
        return jsonify({"error": "User not found"}), 404

# Opdater bruger
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    name = data.get("name")
    email = data.get("email")

    conn = db.get_connection()
    if not conn:
        return jsonify({"error": "DB connection error"}), 500

    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET name=?, email=? WHERE id=?", (name, email, user_id))
        conn.commit()
    except mariadb.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify({"id": user_id, "name": name, "email": email}), 200

# Slet bruger
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = db.get_connection()
    if not conn:
        return jsonify({"error": "DB connection error"}), 500

    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
    except mariadb.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify({"message": "User deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
```

> **Bemærk**: I en rigtig applikation håndterer du nok konfiguration (host, port, debug-mode osv.) med en separat konfig.

---

## Kørsel og test
1. Sørg for at MariaDB-serveren kører, og at du har en `users`-tabel. Kør evt. `db.create_users_table()`.
2. Start Flask:
   ```bash
   python app.py
   ```
3. Flask burde køre på `http://127.0.0.1:5000` (standard).
4. Test i Postman eller med `curl`:
   ```bash
   # Hent brugere
   curl -X GET http://127.0.0.1:5000/users

   # Opret ny bruger
   curl -X POST -H "Content-Type: application/json" \
        -d '{"name":"Kurt","email":"kurt@example.com"}' \
        http://127.0.0.1:5000/users
   ```

---

## Øvelser
1. **Udvid**: Lav en rute `GET /users/search/<navn>` der søger på brugernavn.
2. **Fejlhåndtering**: Hvad sker der, hvis du prøver at opdatere eller slette en bruger, der ikke findes?
3. **Validering**: Tjek, at en mailadresse følger et grundlæggende format.
4. **Tilføj relationer**: Hvis du har tabellen `orders`, kan du lave et `/orders`-endpoint.

---

## Videre
Du har nu et grundlæggende web-API i Flask, der forbinder til MariaDB. Du kan bygge en frontend, en mobilapp eller lade et script/andet system kalde dine endpoints. Overvej at kigge på **FastAPI**, hvis du vil have automatisk dokumentation, async-støtte og andet praktisk.
