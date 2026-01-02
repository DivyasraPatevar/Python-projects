import os

files = os.listdir()

for i, file in enumerate(files):
    if file.endswith(".txt"):
        os.rename(file, f"file_{i}.txt")
