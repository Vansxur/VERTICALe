import json

# Load the JSON file
with open('data.json') as f:
    data = json.load(f)

# Load the list of suid binary files
with open('suid_binaries.txt') as f:
    suid_binaries = [line.strip() for line in f]

# Iterate over each binary file in the list
for suid_binary in suid_binaries:
    # Extract the file name from the file path
    binary_name = suid_binary.split("/")[-1]

    # Check if the file name is present in the dictionary
    if binary_name in data:
        # If the file name is present, check if the "suid" tag is present in the associated list
        if "suid" in data[binary_name]:
            print(f"The 'suid' tag is present for the binary file '{binary_name}'.")
        else:
            print(f"The 'suid' tag is not present for the binary file '{binary_name}'.")
    else:
        print(f"The binary file '{binary_name}' was not found in the JSON file.")
