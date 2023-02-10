#!/bin/bash

binaries_file="gtfobins.json"

# Charger les binaires à partir du fichier json
binaries=$(cat $binaries_file)

touch suid_binaries.txt 2> /dev/null

# Boucle sur tous les binaires dans /usr/bin pour trouver ceux avec le bit SUID
for binary in $(ls /bin); do
  path=$(realpath "/bin/$binary")

# TODO : CHERCHER SUR TOUT LE SYSTEME

  if [ -u $path ]; then
    # Vérifier s'ils existent dans le fichier json avec l'objet "suid"
    if echo "$binaries" | grep -q "\"$binary\": \[.*suid.*\]"; then
      echo "Binaire '$binary' existe dans le fichier json avec l'objet 'suid'."; >> suid_binaries.txt;
    fi
  fi
done

if [ -s suid_binaries.txt; ]; then
	exit 0
else
	echo "nosuid" > suid_binaries.txt;
fi
