# 04 Python ↔ MariaDB

> **Formål**: Lære at forbinde fra Python til MariaDB ved hjælp af `mariadb`-biblioteket, udføre grundlæggende SQL-queries og håndtere resultater.

## 📝 Indhold
1. [Introduktion](#introduktion)
2. [Installation af mariadb-biblioteket](#installation-af-mariadb-biblioteket)
3. [Opret forbindelse i Python](#opret-forbindelse-i-python)
4. [Eksekver SQL-kommandoer](#eksekver-sql-kommandoer)
5. [Håndtering af resultater](#håndtering-af-resultater)
6. [Parameteriserede queries](#parameteriserede-queries)
7. [Fejlhåndtering (try-except)](#fejlhåndtering-try-except)
8. [Øvelser](#øvelser)
9. [Videre](#videre)

---

## Introduktion
I dette modul kommer du til at skrive Python-kode, der forbinder til MariaDB og udfører SQL-queries programmatisk. Ved at kombinere Python og SQL kan du automatisere opgaver, bygge CLI- eller webapplikationer m.m.

---

## Installation af mariadb-biblioteket

1. Sørg for at du kører i dit virtuelle miljø (hvis du benytter sådan et).
2. Installer `mariadb`-driveren:
   ```bash
   pip install mariadb
   ```
3. Tjek, at installationen lykkedes:
   ```bash
   pip show mariadb
   ```

---

## Opret forbindelse i Python

Opret en fil `db_test.py`:
```python
import mariadb

try:
    conn = mariadb.connect(
        user="workshop_user",
        password="secretpassword",
        host="localhost",
        port=3306,
        database="workshop_db"
    )
    print("Forbindelse oprettet")

except mariadb.Error as e:
    print(f"Fejl ved forbindelse: {e}")

finally:
    if conn:
        conn.close()
        print("Forbindelse lukket")
```

- **`mariadb.connect()`** tager dine loginoplysninger + database.
- I en rigtig applikation vil du ofte gemme disse oplysninger i en konfigurationsfil eller miljøvariabler.
- **`try-except-finally`** sikrer, at vi håndterer fejl og lukker forbindelsen.

Kør scriptet:
```bash
python db_test.py
```
Se, om du får en besked om "Forbindelse oprettet".

---

## Eksekver SQL-kommandoer

For at udføre queries, skal du bruge et **cursor**-objekt:
```python
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data VARCHAR(100)
)")
conn.commit()  # Husk at committe ved DDL/INSERT/UPDATE/DELETE
```

> Bemærk: Hvis du får en fejl, kan det skyldes manglende rettigheder.

---

## Håndtering af resultater

Når du laver en SELECT, kan du hente rækkerne:
```python
cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()  # henter alle resultater
for row in rows:
    print(row)
```

Du kan også bruge `cursor.fetchone()` til én række ad gangen.

- `rows` vil typisk være en liste af tuples.
- Hvis `users`-tabellen har kolonnerne (id, name, email), så kan en row fx se ud som `(1, "Alice", "alice@example.com")`.

---

## Parameteriserede queries

For at undgå SQL-injection og gøre queries fleksible, brug placeholders:
```python
data = ("Alice", "alice@example.com")
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", data)
conn.commit()
```

> `?`-placeholderen erstattes af værdier i `data`.

Du kan også bruge named placeholders med `%s` afhængigt af driver, men `?` er standard i `mariadb`.

---

## Fejlhåndtering (try-except)

```python
try:
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
except mariadb.Error as e:
    print("Databasefejl:", e)
```

- Hvis der sker en fejl (fx syntax error i SQL), fanges den af `mariadb.Error`.
- Håndtér det på en hensigtsmæssig måde (evt. log det, eller giv brugeren besked).

---

## Øvelser
1. **Opret script**: Lav et script `create_users.py`, der:
   - Forbinder til databasen.
   - Opretter en tabel `users` (hvis den ikke findes).
   - Indsætter 2-3 rækker.
   - Læser (SELECT) og printer dem i terminalen.
2. **Eksperimentér**: Tilføj en parameteriseret query, hvor du spørger brugeren om et navn og bruger det i et SELECT-spørgsmål.
3. **Afprøv fejl**: Prøv bevidst at lave en syntaxfejl i en query og se, hvordan `mariadb.Error` håndteres.

---

## Videre
Tillykke! Du har nu lært at forbinde Python og MariaDB med en driver.

**👉 Videre til [05_advanced_sql](../05_advanced_sql/README.md)**, hvor du lærer om JOIN, GROUP BY, underforespørgsler og mere avanceret SQL.
