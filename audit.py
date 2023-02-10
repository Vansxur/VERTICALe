import os
import json

binaries_file = "data.json"

with open(binaries_file, "r") as file:
    binaries = json.load(file)

suid_binaries = []

for binary in os.listdir("/usr/bin"):
    path = os.path.join("/usr/bin", binary)
    if os.stat(path).st_mode & 0o4000:
        suid_binaries.append(binary)

for binary in suid_binaries:
    if binary in binaries and "suid" in binaries[binary]:
        print(f"Binaire '{binary}' existe dans le fichier json avec l'objet 'suid'.")
