import os

if os.path.exists("Text.txt.txt"):
    os.remove("Text.txt.txt")
else:
    print("File not Found")