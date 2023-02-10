import os
import json
import requests
import sys
import re

print("""
                 _   _           _
 /\   /\___ _ __| |_(_) ___ __ _| |
 \ \ / / _ \ '__| __| |/ __/ _` | |
  \ V /  __/ |  | |_| | (_| (_| | |
   \_/ \___|_|   \__|_|\___\__,_|_|
""")

print("- Get the list of Binaries")
url = 'https://api.github.com/repos/GTFOBins/GTFOBins.github.io/contents/_gtfobins?ref=master'
response = requests.get(url)
print("Status = " + str(response))
data = response.json()
filenames = []

for file in data:
    if file['type'] == 'file':
        filename = file['name']
        if os.path.splitext(filename)[1] == '.md':
            filenames.append(os.path.splitext(file['name'])[0])

with open('gtfobins_binaries.txt', 'w') as file:
    for name in filenames:
        file.write(name + '\n')

if os.path.exists("gtfobins_binaries.txt"):
    with open("gtfobins_binaries.txt", "r") as f:
        content = f.readlines()
        if not os.path.exists("binaries"):
            os.mkdir("binaries")
        for binary in content:
            binary = binary.strip()
            res = requests.get(f"https://raw.githubusercontent.com/GTFOBins/GTFOBins.github.io/master/_gtfobins/{binary}.md")
            data = res.text
            with open(f"binaries/{binary}.md", "w") as md_file:
                md_file.write(data)
            print(f"{binary}.md created.")

directory = 'binaries'
data = {}

for filename in os.listdir(directory):
    if filename.endswith(".md"):
        # Extraction du nom de fichier sans l'extension
        name = filename[:-3]

        # Lecture du fichier .md
        with open(os.path.join(directory, filename), 'r') as file:
            lines = file.readlines()

        # Boucle sur les lignes du fichier
        for line in lines:
            # Si la ligne contient "functions", c'est le début des méthodes
            if "functions:" in line:
                # Initialisation de la liste des méthodes pour ce fichier
                functions = []
                # Boucle sur les lignes suivantes pour extraire les méthodes
                for line in lines[lines.index(line)+1:]:
                    # Si la ligne est vide, c'est la fin des méthodes
                    if line.strip() == '':
                        break
                    # Vérification de la longueur de la ligne et que la deuxième position est un espace
                    if len(line) >= 2 and line[0] == ' ' and line[1] == ' ' and line[2] != ' ':
                        # Extraction du nom de la méthode
                        function = line.split(':')[0].strip()
                        # Ajout de la méthode à la liste
                        functions.append(function)
                # Enregistrement de la liste de méthodes pour ce fichier
                data[name] = functions

# Écriture du fichier JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
