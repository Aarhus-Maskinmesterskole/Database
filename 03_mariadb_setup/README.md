# 03 MariaDB Setup

> **Formål**: Få et bedre indblik i, hvordan man opsætter og konfigurerer MariaDB, herunder brugerkonti, rettigheder og generel drift.

## 📝 Indhold
1. [Introduktion](#introduktion)
2. [Start og stop af MariaDB](#start-og-stop-af-mariadb)
3. [Brugerkonti og rettigheder](#brugerkonti-og-rettigheder)
4. [Konfiguration (my.cnf)](#konfiguration-mycnf)
5. [Yderligere sikkerhed](#yderligere-sikkerhed)
6. [Øvelser](#øvelser)
7. [Videre](#videre)

---

## Introduktion
Nu hvor du har prøvet de mest grundlæggende SQL-kommandoer, er det tid til at se lidt på, hvordan du sætter MariaDB op i praksis og håndterer brugere samt rettigheder. Hvis du allerede har kørt nogle af kommandoerne fra de tidligere moduler, er noget af dette måske en gentagelse, men her får du et samlet overblik.

---

## Start og stop af MariaDB

Hvordan du starter/stopper MariaDB afhænger af dit styresystem.

### Linux (Debian/Ubuntu)
```bash
sudo service mariadb start   # Start
sudo service mariadb stop    # Stop
sudo service mariadb restart # Genstart
```

### macOS (Homebrew)
```bash
brew services start mariadb
brew services stop mariadb
brew services restart mariadb
```

### Windows
- MariDB kan køre som en tjeneste. For at styre den, kan du åbne **Services** (tjenester) i Windows og finde "MariaDB".
- Alternativt kan du køre den via en batchfil eller i en "bin"-mappe, fx:
  ```bash
  net start MariaDB
  net stop MariaDB
  ```

> **Tip**: Sørg for at MariaDB kører, inden du prøver at logge på via `mysql -u ... -p`.

---

## Brugerkonti og rettigheder
MariaDB/MySQL har et system til brugerkonti og rettigheder (privileges), der afgør, hvem der må gøre hvad.

### Opret brugerkonto

```sql
CREATE USER 'brugernavn'@'localhost' IDENTIFIED BY 'hemmeligtKodeord';
```

- `'localhost'` betyder, at brugeren kun kan logge på fra samme maskine.
- Ønsker du ekstern adgang, kan du bruge `'%'` eller en specifik IP.

### Tildel rettigheder

```sql
GRANT ALL PRIVILEGES ON workshop_db.* TO 'brugernavn'@'localhost';
FLUSH PRIVILEGES;
```

- `ALL PRIVILEGES` kan erstattes af specifikke rettigheder, fx `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `DROP`, osv.
- `workshop_db.*` giver rettigheder på alle tabeller i databasen `workshop_db`.
- `FLUSH PRIVILEGES;` skal kaldes for at opdatere ændringer i rettighedstabellerne.

### Vis rettigheder

```sql
SHOW GRANTS FOR 'brugernavn'@'localhost';
```

### Ændr adgangskode

```sql
ALTER USER 'brugernavn'@'localhost' IDENTIFIED BY 'nytKodeord';
```

### Slet brugerkonto

```sql
DROP USER 'brugernavn'@'localhost';
```

---

## Konfiguration (my.cnf)

MariaDBs hovedkonfigurationsfil hedder ofte `my.cnf` (eller `mysqld.cnf`), og kan ligge forskellige steder alt efter styresystem. Eksempler:
- `/etc/mysql/my.cnf` (Debian/Ubuntu)
- `/usr/local/etc/my.cnf` (macOS Homebrew)
- `C:\Program Files\MariaDB XX\data\my.ini` (Windows, sti varierer)

Nogle ofte konfigurerede felter:
- **`bind-address`**: Hvis du vil tillade ekstern adgang, skal denne måske ændres fra `127.0.0.1` til `0.0.0.0` (eller en bestemt IP).
- **`port`**: Standardport er 3306.
- **`max_connections`**: Styrer, hvor mange samtidige forbindelser der kan være.
- **`query_cache_size`** (i ældre versioner) eller `innodb_buffer_pool_size` (InnoDB performance).

Ændrer du i `my.cnf`, skal du ofte genstarte serveren:
```bash
sudo service mariadb restart
```

---

## Yderligere sikkerhed
- **Root-brugeren**: På produktionsservere bør du sikre, at root-brugeren kun kan logge på lokalt, og at du har et stærkt kodeord.
- **Firewall**: Hvis du eksponerer port 3306 eksternt, så sæt firewallregler for kun at tillade relevante IP-adresser.
- **Brug `sudo mysql_secure_installation`** (på nogle Linux-systemer) for at sætte root-kodeord, fjerne anonyme brugere osv.

---

## Øvelser
1. **Opret ny bruger**: Lav en bruger, der kun har SELECT- og INSERT-rettigheder på `workshop_db.*`.
2. **Test**: Log ind med den nye bruger og forsøg at køre en `DROP TABLE` eller `DELETE`. Hvad sker der?
3. **Bind-address**: Tjek (om muligt) din `my.cnf` for at se, hvad `bind-address` er sat til.
4. **Skift root-adgangskode** (på en testserver), hvis du ikke allerede har gjort det.
   OBS! Opgave 4 bør kun anvendes på testserver som den du arbejder på og ikke server som allerede er oppe at køre i produktionen.

---

## Videre
Nu har du en forståelse for, hvordan MariaDB håndterer brugerkonti, rettigheder og konfiguration. Dette kan være nyttigt, når du fx skal opsætte en database til en Python-applikation.

**👉 Videre til [04_python_mariadb](../04_python_mariadb/README.md)**, hvor du lærer at forbinde Python direkte til MariaDB og udføre queries programmatisk.


