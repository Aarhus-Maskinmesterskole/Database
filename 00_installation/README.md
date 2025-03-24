# 00 Installation og Opsætning

> **Formål**: Få sat både Python og MariaDB korrekt op lokalt, så du er klar til at arbejde med resten af workshops.

## 📝 Indhold
1. [Forudsætninger](#forudsætninger)
2. [Installation af Python 3](#installation-af-python-3)
3. [Installation af MariaDB](#installation-af-mariadb)
4. [Oprettelse af database og bruger](#oprettelse-af-database-og-bruger)
5. [Test af installation](#test-af-installation)
6. [Evt. opsætning af Virtual Environment](#evt-opsætning-af-virtual-environment)
7. [Fejlfinding](#fejlfinding)

---

## Forudsætninger
- Du har adgang til at installere programmer på din computer (Windows/macOS/Linux).
- Du er i stand til at downloade og køre eksekverbare filer.
- Hvis du allerede har Python 3 installeret, bør du sikre, at det er en forholdsvis ny version (fx 3.8 eller nyere).

---

## Installation af Python 3
### Windows
1. Gå til [python.org/downloads](https://www.python.org/downloads/)
2. Vælg den nyeste stabile version (3.x.x).
3. Kør installationsprogrammet, **husk** at markere “Add Python to PATH” (hvis den mulighed findes).
4. Tjek installationen ved at åbne en PowerShell eller Command Prompt og køre:
   ```bash
   python --version
   ```

### macOS
1. Installer enten via [python.org/downloads](https://www.python.org/downloads/) eller via Homebrew (`brew install python3`).
2. Tjek installationen i Terminal:
   ```bash
   python3 --version
   ```

### Linux
1. De fleste distributioner har en nyere Python-version i deres pakkesystem, fx:
   ```bash
   sudo apt-get update && sudo apt-get install python3 python3-pip
   ```
2. Tjek installationen:
   ```bash
   python3 --version
   ```

---

## Installation af MariaDB
### Windows
1. Download installationsfilen fra [mariadb.org](https://mariadb.org/).
2. Kør installationsprogrammet og følg guiden.
3. Notér brugernavn og adgangskode, hvis du bliver bedt om at oprette det undervejs.
4. For at teste, kør `mysql --version` i en Command Prompt eller se om "MariaDB" er tilgængelig under programmer.

### macOS & Linux
1. Via Homebrew (macOS): `brew install mariadb`.
2. På Linux (Debian/Ubuntu):
   ```bash
   sudo apt-get update
   sudo apt-get install mariadb-server mariadb-client
   ```
3. Tjek installation med:
   ```bash
   mysql --version
   ```

---

## Oprettelse af database og bruger
Efter installation kan du oprette en ny database og en separat bruger til workshoppen. Det kan du gøre via kommandolinjen:

1. Åbn Terminal/Command Prompt:
   ```bash
   mysql -u root -p
   ```
   (Indtast "root"-adgangskode, hvis du har sat en.)

2. Opret databasen:
   ```sql
   CREATE DATABASE workshop_db;
   ```

3. Opret en ny bruger (valgfrit hvis du vil holde alt på root, men anbefales):
   ```sql
   CREATE USER 'workshop_user'@'localhost' IDENTIFIED BY 'secretpassword';
   GRANT ALL PRIVILEGES ON workshop_db.* TO 'workshop_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

4. Afslut med `exit;`.

---

## Test af installation
**Test MariaDB**:
1. Log ind med din nye bruger:
   ```bash
   mysql -u workshop_user -p
   ```
2. Tjek at `workshop_db` eksisterer:
   ```sql
   SHOW DATABASES;
   USE workshop_db;
   ```

**Test Python**:
1. Åbn en terminal eller prompt og kør:
   ```bash
   python --version
   ```
   eller (hvis det kræves)
   ```bash
   python3 --version
   ```
2. Lav en simpel testfil `test.py`:
   ```python
   print("Hej fra Python!")
   ```
   Kør med `python test.py`.

---

## Evt. opsætning af Virtual Environment
For at holde dine Python-pakker isolerede og undgå konflikter, kan du bruge et virtuelt miljø:
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
.\venv\Scripts\activate  # Windows
```

Installer derefter Python-pakker lokalt i dette miljø, fx:
```bash
pip install mariadb
```

Husk altid at aktivere miljøet, før du kører dine scripts.

---

## Fejlfinding
- **Kan ikke køre `mysql`-kommando**: Sørg for, at MariaDB er tilføjet til PATH, eller prøv at navigere til installationsmappen.
- **Får en fejl ved `pip install mariadb`**: Tjek at du har nyeste `pip` ved `python -m pip install --upgrade pip`.
- **Rettigheder**: Hvis du ikke kan oprette databaser/tabeller, så tjek om brugeren har de rigtige GRANTs.

---

**Så er du klar til næste modul!**

**👉 Videre til [01_python_basics](../01_python_basics/README.md)**
