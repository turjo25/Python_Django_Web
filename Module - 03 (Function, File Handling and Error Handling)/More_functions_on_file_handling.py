import os
import pathlib
if os.path.exists('test.txt'):
    print("File exist")
else:
    print("Doesn't exist")

#pathlib
file_path = pathlib.Path('file.txt')
if file_path.exists():
    print("Exists")

#for printing path
print(os.path.abspath('file.txt'))

#for the size of the file
print(os.path.getsize('info.txt'))