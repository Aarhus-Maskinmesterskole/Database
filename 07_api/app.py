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
