import os
import sys

if (len(sys.argv) != 2):
    print("Error: need to input the folder you want to rename")
    exit()

targetDirectory = sys.argv[1]

# Protect against trailing slashes
if targetDirectory.endswith('/'):
    targetDirectory = targetDirectory[:-1]
    
fileNames = os.listdir(targetDirectory)

directoryName = os.path.split(targetDirectory)[-1]

for i in range(len(fileNames)):
    fileName = fileNames[i]
    print('Renaming', fileName, 'to', directoryName + "." + str(i) + ".jpg")
    os.rename(targetDirectory + "/" + fileName, targetDirectory + "/" + directoryName + "." + str(i) + ".jpg")