import os
import requests

try:
    curDir = input("Enter path: ")
    newDir = input("Enter new path: ")

    items = os.listdir(curDir)

    for item in items:
        stringLength = len(item)
        fileExtension = item[stringLength-4:]

        if fileExtension == '.pdf':
            currentPath = f'{curDir}/{item}'
            newPath = f'{newDir}/{item}'

            os.renames(currentPath, newPath)

    print('Moving Files Done...')

except FileNotFoundError:
    print("File/Directory doesn't Exist")










