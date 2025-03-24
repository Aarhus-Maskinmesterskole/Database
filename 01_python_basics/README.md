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
9. [Videre](#🚀Videre)

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

## 🧪 Øvelser

Herunder finder du en række små øvelser, som du kan køre direkte i Python. Kopiér koden ind i en `.py`-fil, kør den – og læs kommentarerne. Reflektér over, hvad der sker.

---

### ✅ 1. Hello World

**Opret en fil `hello.py` og skriv:**

```python
# Din første Python-program
print("Hej fra Python!")
```

> 🌟 Kør med `python hello.py` og se resultatet.  
> 🔍 Hvad betyder `print()`? Kan du ændre teksten?

---

### ➕ 2. Regnemaskine

**Spørg brugeren om to tal og udskriv summen**

```python
# Regnemaskine: læg to tal sammen
tal1 = input("Indtast første tal: ")
tal2 = input("Indtast andet tal: ")

# Omform til tal
sum = float(tal1) + float(tal2)

print("Summen er:", sum)
```

> 🔍 Hvad sker der, hvis du skriver tekst i stedet for tal?

---

### 📋 3. Liste-øvelse

**Lav en liste med fem navne og udskriv dem med en for-løkke**

```python
# En liste med navne
navne = ["Alice", "Bob", "Charlie", "Diana", "Emil"]

for navn in navne:
    print("Hej", navn)
```

> 🔍 Hvad sker der, hvis du fjerner én af personerne?  
> ✍️ Prøv selv at tilføje en ny person i listen.

---

### 📖 4. Dictionary-øvelse

**Lav en dictionary med navn og alder og udskriv værdierne**

```python
# En person som dictionary
person = {
    "navn": "Alice",
    "alder": 25
}

print("Navn:", person["navn"])
print("Alder:", person["alder"])
```

> 🔍 Hvad sker der, hvis du prøver at få fat i en nøgle der ikke findes?

---

### 🧠 5. Funktion

**Lav en funktion `gangeTo(x)` der returnerer `x*2`**

```python
# Funktion der ganger med 2
def gangeTo(x):
    return x * 2

print(gangeTo(3))    # 6
print(gangeTo(10))   # 20
print(gangeTo(-5))   # -10
```

> 🔍 Prøv at ændre funktionen, så den ganger med 3 i stedet.

---

### ⭐ 6. Tilvalg: Quiz

**Lav en quiz der stiller et spørgsmål, og tjekker om svaret er korrekt**

```python
# Mini-quiz med ét spørgsmål
rigtige_svar = 0

svar = input("Hvad er hovedstaden i Danmark? ")

if svar.lower() == "københavn":
    print("Korrekt!")
    rigtige_svar += 1
else:
    print("Forkert. Det rigtige svar er København.")

print("Du fik", rigtige_svar, "rigtige.")
```

> ✍️ Udvid quizzen med flere spørgsmål.  
> 🔍 Hvordan tæller du point?

---

## 🚀 Videre
- Når du har løst øvelserne, er du klar til at gå videre til **[02_sql_basics](../02_sql_basics/README.md)**.
- Her lærer du at oprette tabeller og lave grundlæggende SQL-forespørgsler i MariaDB.

