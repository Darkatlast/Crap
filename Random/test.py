import os

filename = "example.txt"

# --- CREATE ---
# Create a new file (or overwrite if it already exists) and write to it
with open(filename, "w") as f:
    f.write("Hello, this is the first line.\n")

print("File created and data written.")

# --- READ ---
# Open the file and read its contents
with open(filename, "r") as f:
    content = f.read()

print("File contents after READ:")
print(content)

# --- UPDATE ---
# Append new data to the file
with open(filename, "a") as f:
    f.write("This is an appended line.\n")

# Overwrite the file (if needed)
with open(filename, "r+") as f:
    lines = f.readlines()
    lines[0] = "Hello, this line has been UPDATED.\n"
    f.seek(0)
    f.writelines(lines)

print("File updated.")

# Check updated content
with open(filename, "r") as f:
    print("File contents after UPDATE:")
    print(f.read())

# --- DELETE ---
# Remove the file from the system
os.remove(filename)
print("File deleted.")