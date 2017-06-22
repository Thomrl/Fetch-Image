#! Python3.5
import os, shutil

os.chdir("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Skyrim Special Edition") #Where you want to get the images from
path = os.getcwd()
print(path)

for file in os.listdir():
    if file.endswith(".png"): #The file type                                          #The file type
        shutil.move(file, "C:\\files\\Thomas\\Pictures\\Screenshots\\Skyrim")         #Where you want the images to go

