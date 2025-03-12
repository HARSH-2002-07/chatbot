import time
import os

file_path = r"D:\ChatBot\Frontend\Files\Mic.data"

with open(file_path, "w", encoding="utf-8") as file:
    file.write("T")
    file.flush()
    os.fsync(file.fileno())

# Wait for changes to apply
time.sleep(1)

# Verify if the file has changed
with open(file_path, "r", encoding="utf-8") as file:
    print("File content:", file.read())
