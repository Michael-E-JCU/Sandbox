import os

print(f"The files and folders in {os} are")
items = os.listdir('.')
for item in items:
    print(item)
