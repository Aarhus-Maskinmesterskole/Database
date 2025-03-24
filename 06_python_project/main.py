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
