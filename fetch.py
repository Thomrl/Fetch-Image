#! Python3.5
import os, shutil

os.chdir("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Skyrim Special Edition")
path = os.getcwd()
print(path)

for file in os.listdir():
    if file.endswith(".png"):
        shutil.move(file, "C:\\files\\Thomas\\Pictures\\Screenshots\\Skyrim")

