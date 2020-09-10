import os
import shutil


print ("--------------------")
directory = input("Enter Directory to sort.")


if os.path.exists(directory):
    print ("Directory Exists, continuing.")
else:
    print ("Directory doesnt exist.")
    quit()

print("Continuing.")


os.chdir(directory)


print("Script entered: ",directory)
dirType = input("Are you using folders already created or would you like to sort into new folders? (1,2)")
print(dirType)

if dirType == "1":
    print ("Folder system of your choosing! sweet. :)")
    print("Now you need to designate what files go into what folder.")
    print("Printing folders and files in the directory listed....")
    print("---------------------------------------------------------")
    dirs = os.listdir(directory)
    for file in dirs:
        print(file)
    print("----------------------------------------------------------")

    print("So, where do you want executables and installers/ect to go?")
    exeDir = input()
    exeDir = directory +  exeDir
    print (exeDir)
    if os.path.exists(exeDir):
        print("Exists, continuing")
        for file in os.listdir(directory):
            if file.endswith(".exe"):
                shutil.move(file,exeDir)
                print (file+" Moved to " + exeDir)

if dirType == 2:
    print ("placeholder 2")
