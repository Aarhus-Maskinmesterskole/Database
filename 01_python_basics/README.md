# 01 Python Basics

> **Formål**: Få en introduktion til grundlæggende Python-syntaks, datastrukturer og kontrolstrukturer.

## 📝 Indhold
1. [Introduktion](#introduktion)
2. [Kørsel af Python-kode](#kørsel-af-python-kode)
3. [Grundlæggende syntaks](#grundlæggende-syntaks)
4. [Datatyper og variabler](#datatyper-og-variabler)
5. [Lister, Tupler og Dictionaries](#lister-tupler-og-dictionaries)
6. [Kontrolstrukturer](#kontrolstrukturer)
7. [Funktioner](#funktioner)
8. [Øvelser](#øvelser)
9. [Videre](#videre)

---

## Introduktion
I dette modul får du en hurtig gennemgang af, hvordan du skriver og kører Python-kode. Du lærer om variabler, datatyper, lister/tupler/dictionaries, if-sætninger og løkker. Du kommer også til at lave et par små øvelser for at få praktisk erfaring.

---

## Kørsel af Python-kode
### Direkte i terminal
- Åbn en terminal og skriv `python` (eller `python3`) for at åbne en interaktiv Python-fortolker.
- Test ved at skrive `print("Hej fra Python!")` og se, om det virker.
- Afslut med `exit()` eller Ctrl+D.

### Fra en .py-fil
1. Opret en fil, fx `hello.py`, og skriv:
   ```python
   print("Hej fra Python!")
   ```
2. Kør filen i terminalen:
   ```bash
   python hello.py
   ```

### IDE eller editor
- Du kan også bruge en editor som VSCode, PyCharm, Sublime etc.
- Fordel: syntaksfremhævning, autocompletion, debugging, osv.

---

## Grundlæggende syntaks
- Python er indrykningsbaseret: blokke defineres ved indryk (typisk 4 mellemrum).
- Kommentarer: `# Dette er en kommentar`
- Et simpelt eksempel:
  ```python
  # Variabel tildeling
  navn = "Alice"
  alder = 25

  if alder > 18:
      print(navn, "er myndig")
  ```

---

## Datatyper og variabler

1. **Strenge** (strings):
   ```python
   tekst = "Hello world"
   print(tekst)
   ```
2. **Heltal** (integers) og **Kommatal** (floats):
   ```python
   heltal = 42
   kommatal = 3.14
   ```
3. **Boolean** (True/False):
   ```python
   er_sand = True
   ```
4. **Typecasting**:
   ```python
   tal = "123"
   tal_som_int = int(tal)  # 123 som int
   ```
5. **Lidt om variable scope** (grundlæggende i Python):
   - Variabler i funktioner er lokale.
   - Global scope kan tilgås, men sjældent anbefalet.

---

## Lister, Tupler og Dictionaries

### Lister
- En liste er en sekvens af elementer, der kan ændres.
  ```python
  navne = ["Alice", "Bob", "Charlie"]
  print(navne[0])   # "Alice"
  navne.append("Diana")
  ```

### Tupler
- En tuple er ligesom en liste, men kan **ikke** ændres (immutable).
  ```python
  farver = ("rød", "grøn", "blå")
  ```

### Dictionaries
- En dictionary er et nøgle-værdi-par.
  ```python
  person = {
      "navn": "Alice",
      "alder": 25
  }
  print(person["navn"])  # Alice
  ```

---

## Kontrolstrukturer

### If-sætninger
```python
if betingelse:
    # kode
elif anden_betingelse:
    # kode
else:
    # kode
```

### For-løkke
```python
for x in range(5):
    print(x)

for navn in ["Alice", "Bob"]:
    print(navn)
```

### While-løkke
```python
tal = 0
while tal < 5:
    print(tal)
    tal += 1
```

---

## Funktioner
```python
def hils(navn):
    print(f"Hej, {navn}!")

hils("Alice")
```python
- En funktion defineres med `def`.
- Parametre og evt. returværdi:
  ```python
def kvadrat(x):
    return x * x
```

---

## Øvelser
1. **Hello World**: Opret en `hello.py` og print "Hej fra Python!".
2. **Regnemaskine**: Skriv et script, der spørger om to tal og printer summen.
3. **Liste-øvelse**: Lav en liste med 5 navne og loop over dem med en `for`-løkke.
4. **Dictionary-øvelse**: Lav en dictionary med nøglerne `navn`, `alder` og print dem.
5. **Funktion**: Skriv en funktion `gangeTo(x)`, der returnerer x*2. Kald den med flere værdier.
6. **Tilvalg**: Lav en lille quiz, der beder brugeren om input, sammenligner med rigtige svar, og tæller point.

---

## Videre
- Når du har løst øvelserne, er du klar til at gå videre til **[02_sql_basics](../02_sql_basics/README.md)**.
- Her lærer du at oprette tabeller og lave grundlæggende SQL-forespørgsler i MariaDB.

