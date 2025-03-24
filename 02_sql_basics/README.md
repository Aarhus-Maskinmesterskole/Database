# 02 SQL Basics

> **Formål**: Lære at oprette og håndtere tabeller i MariaDB, samt forstå basale SQL-forespørgsler (SELECT, INSERT, UPDATE, DELETE, WHERE, ORDER BY).

## 📝 Indhold
1. [Introduktion](#introduktion)
2. [Opsætning og forbindelse](#opsætning-og-forbindelse)
3. [Oprettelse af tabel](#oprettelse-af-tabel)
4. [Indsæt data (INSERT)](#indsæt-data-insert)
5. [Forespørgsler (SELECT, WHERE, ORDER BY)](#forespørgsler-select-where-order-by)
6. [Opdatering og sletning (UPDATE, DELETE)](#opdatering-og-sletning-update-delete)
7. [Øvelser](#øvelser)
8. [Videre](#videre)

---

## Introduktion
I dette modul kommer du i gang med **grundlæggende SQL** ved brug af MariaDB. Du lærer at oprette tabeller, indsætte data og udtrække data ved hjælp af SELECT-sætninger. Derudover gennemgår vi, hvordan man opdaterer og sletter rækker.

---

## Opsætning og forbindelse

1. **Start MariaDB-server** (hvis den ikke allerede kører).
2. **Åbn en terminal** og log ind:
   ```bash
   mysql -u workshop_user -p
   USE workshop_db;
   ```
   (Indtast din adgangskode, hvis du har sat en.)

> **Tip**: Kør `SHOW DATABASES;` for at se alle databaser, og `SHOW TABLES;` for at se tabellerne i den aktuelle database.

---

## Oprettelse af tabel

Først opretter vi en simpel tabel til at gemme brugere:
```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50)
);
```
Forklaring:
- **id**: Et unikt id (INT) med AUTO_INCREMENT.
- **name**: Navn på brugeren (op til 50 tegn).
- **email**: Emailadresse (op til 50 tegn).

Tjek, om tabellen nu eksisterer:
```sql
SHOW TABLES;
```

---

## Indsæt data (INSERT)

For at tilføje data til `users`:
```sql
INSERT INTO users (name, email)
VALUES ("Alice", "alice@example.com");
```

Tilføj flere rækker:
```sql
INSERT INTO users (name, email)
VALUES
("Bob", "bob@example.com"),
("Charlie", "charlie@example.com");
```

---

## Forespørgsler (SELECT, WHERE, ORDER BY)

### SELECT

For at hente alle data:
```sql
SELECT * FROM users;
```

### WHERE

Filtrér resultaterne:
```sql
SELECT * FROM users
WHERE name = "Alice";
```

Eller fx på id:
```sql
SELECT * FROM users
WHERE id = 2;
```

### ORDER BY

Sortér data efter et felt:
```sql
SELECT * FROM users
ORDER BY name ASC;

-- Eller omvendt:
SELECT * FROM users
ORDER BY name DESC;
```

---

## Opdatering og sletning (UPDATE, DELETE)

### UPDATE

Ændr data i eksisterende rækker:
```sql
UPDATE users
SET email = "newalice@example.com"
WHERE name = "Alice";
```

> **Tip**: Brug en WHERE-klausul, så du ikke kommer til at opdatere ALLE rækker!

### DELETE

Sletning af specifikke rækker:
```sql
DELETE FROM users
WHERE id = 2;
```

> **Tip**: Hvis du udelader WHERE, slettes alle rækker i tabellen. Vær forsigtig!

---

## Øvelser
1. **Opret tabel**: Lav en ny tabel `products` med felter for `id` (AUTO_INCREMENT, PK), `product_name` (VARCHAR), `price` (DECIMAL(10,2)) eller INT efter eget valg.
2. **Indsæt data**: Tilføj mindst 3 produkter.
3. **SELECT**: Hent alle produkter og vis dem i stigende rækkefølge efter pris (ORDER BY).
4. **UPDATE**: Skift navnet på et af dine produkter.
5. **DELETE**: Slet et produkt.
6. **Tilvalg**: Lav en søgeforespørgsel, fx `WHERE product_name LIKE "%navn%"`.

---

## Videre
Med disse grundlæggende SQL-kommandoer kan du nu **oprette**, **hente**, **opdatere** og **slette** data i en tabel.

**👉 Videre til [03_mariadb_setup](../03_mariadb_setup/README.md)** for mere om opsætning, brugerkonti, rettigheder og konfiguration af MariaDB.

