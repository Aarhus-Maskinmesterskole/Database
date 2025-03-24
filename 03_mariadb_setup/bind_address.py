# Denne version tjekker automatisk om systemet er Linux eller Windows og forsøger at finde filen.
import os
import platform

def find_bind_address():
    system = platform.system()

    if system == "Linux":
        paths = [
            "/etc/mysql/my.cnf",
            "/etc/mysql/mariadb.conf.d/50-server.cnf"
        ]
    elif system == "Windows":
        paths = [
            r"C:\Program Files\MariaDB 10.11\data\my.ini",  # Tilpas evt. version
            r"C:\Program Files\MariaDB 10.5\data\my.ini"
        ]
    else:
        print("Ukendt system")
        return

    for path in paths:
        if os.path.exists(path):
            print(f"Tjekker: {path}")
            with open(path, "r") as f:
                for line in f:
                    if "bind-address" in line and not line.strip().startswith("#"):
                        print("Fundet:", line.strip())
                        return
            print("Ingen aktiv bind-address fundet.")
            return
    print("Ingen konfigurationsfil fundet.")

find_bind_address()
