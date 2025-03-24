# 05 Advanced SQL

> **Formål**: Dykke dybere ned i SQL, herunder JOINs, aggregering (GROUP BY), og underforespørgsler. Få en bedre forståelse af mere avancerede dataforespørgsler i MariaDB.

## 📝 Indhold
1. [Introduktion](#introduktion)
2. [JOIN-typer](#join-typer)
3. [GROUP BY og aggregering](#group-by-og-aggregering)
4. [HAVING-klausul](#having-klausul)
5. [Subqueries (underforespørgsler)](#subqueries-underforespørgsler)
6. [Øvelser](#øvelser)
7. [Videre](#videre)

---

## Introduktion
Nu har du set, hvordan man opretter tabeller, indsætter data og udfører basale forespørgsler (SELECT, UPDATE, DELETE). I dette modul ser vi på **JOIN** (hvordan du kobler data fra flere tabeller), **GROUP BY** (aggregering) og **underforespørgsler** (subqueries). Det giver dig mulighed for at opbygge mere komplekse og kraftfulde SQL-forespørgsler.

---

## JOIN-typer

En **JOIN** kombinerer rækker fra to (eller flere) tabeller baseret på en fælles kolonne.

### Eksempel-tabeller

- Tabel `users` (id, name, email)
- Tabel `orders` (id, user_id, order_date, amount)

> `orders.user_id` refererer til `users.id`.

### INNER JOIN

Henter kun de rækker, der har match i **begge** tabeller.
```sql
SELECT u.name, o.order_date, o.amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;
```

### LEFT JOIN

Henter **alle** rækker fra venstre tabel (users), men kun matchende rækker fra højre tabel (orders). Hvor der ikke er match, bliver feltet fra den højre tabel `NULL`.
```sql
SELECT u.name, o.order_date, o.amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

### RIGHT JOIN

Ligesom LEFT JOIN, men tager udgangspunkt i den højre tabel.
```sql
SELECT u.name, o.order_date, o.amount
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```
> Bemærk, at RIGHT JOIN er mindre brugt end LEFT JOIN.

### CROSS JOIN / SELF JOIN

- **CROSS JOIN** kombinerer hver række i første tabel med alle rækker i anden tabel.
- **SELF JOIN** er, når en tabel joines med sig selv (sjældnere anvendt i praksis, men kan være nyttigt fx i hierarkiske data).

---

## GROUP BY og aggregering

Når du vil opsummere data (f.eks. summen af ordrer pr. bruger), bruger du **GROUP BY** + aggregeringsfunktioner.

### COUNT, SUM, AVG, MIN, MAX

Eksempler:
```sql
-- Antal ordrer pr. bruger:
SELECT user_id, COUNT(*) AS antal_ordrer
FROM orders
GROUP BY user_id;
```

```sql
-- Samlet beløb pr. bruger:
SELECT user_id, SUM(amount) AS total_spent
FROM orders
GROUP BY user_id;
```

```sql
-- Gennemsnitligt ordresum pr. bruger:
SELECT user_id, AVG(amount) AS avg_order
FROM orders
GROUP BY user_id;
```

> Du kan lave et JOIN for at vise brugerens navn i stedet for `user_id`:
```sql
SELECT u.name, SUM(o.amount) as total_spent
FROM users u
INNER JOIN orders o ON u.id = o.user_id
GROUP BY u.name;
```

---

## HAVING-klausul

**HAVING** bruges ligesom WHERE, men på de aggregerede resultater efter GROUP BY.

Eksempel:
```sql
SELECT user_id, SUM(amount) AS total_spent
FROM orders
GROUP BY user_id
HAVING SUM(amount) > 100;
```

Her filtreres der på den aggregerede kolonne `SUM(amount)`. `WHERE` fungerer nemlig ikke på resultater af GROUP BY, derfor HAVING.

---

## Subqueries (underforespørgsler)

En **subquery** er en forespørgsel inde i en anden. Det kan være i:
1. **SELECT-listen** (fx hent en beregnet værdi).
2. **FROM**-klausulen (som et virtuelt tabel).
3. **WHERE**-klausulen (oftest).

### Eksempel i WHERE

```sql
SELECT name, email
FROM users
WHERE id IN (
  SELECT user_id
  FROM orders
  WHERE amount > 100
);
```

Her hentes alle brugere, der har mindst én ordre over 100.

### Eksempel i SELECT

```sql
SELECT
  id,
  name,
  (SELECT COUNT(*) FROM orders WHERE orders.user_id = users.id) AS ordre_antal
FROM users;
```

Underforespørgsler kan gøre koden mindre læsbar, men er meget nyttigt i komplekse scenarier.

---

## Øvelser
1. **JOIN**
   - Opret en tabel `orders` (id, user_id, order_date, amount) og lav relation til `users.id`.
   - Indsæt fx 3-5 rækker i `orders`.
   - Lav en forespørgsel med INNER JOIN, der returnerer `users.name`, `orders.order_date` og `orders.amount`.
2. **GROUP BY**
   - Vis summen af `orders.amount` pr. bruger.
   - Filtrér med HAVING (fx kun dem med en total over et vist beløb).
3. **Subquery**
   - Lav en forespørgsel, der viser alle brugere, som har en ordre over 100.
   - (Valgfrit) Lav en SELECT, der viser antallet af ordrer for hver bruger.

---

## Videre
Nu har du set, hvordan man kan udtrække mere komplekse data fra flere tabeller. Disse teknikker gør dig i stand til at lave ret avancerede dataanalyser og rapporter direkte via SQL.

**👉 Videre til [06_python_project](../06_python_project/README.md)**, hvor du bygger en lille CRUD-applikation i Python, der bruger MariaDB.


