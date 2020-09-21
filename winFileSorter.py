import os
import shutil
import moveFunction

while True:
    os.system("cls")
    print ("--------------------------------------------------------------------")
    directory = input("Enter Directory to sort. ( 'xx' to exit) ")

    if directory == "xx":
        break;

    if os.path.exists(directory):
        print ("Directory Exists, continuing.")
    else:
        print ("Directory doesnt exist.")
        quit()

    print("Continuing...")

    os.chdir(directory)

    print("Script entered: ",directory)
    dirType = input("Are you using folders already created or would you like to sort into new folders? (1 , 2)")
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
        check = moveFunction.dirCheck(directory)
        if check != False:
            moveFunction.sortFunction(directory,check,".exe")
            moveFunction.sortFunction(directory,check,".zip")
            moveFunction.sortFunction(directory,check,".msi")
        print("Cool, how about images and media content?")
        check = moveFunction.dirCheck(directory)
        if check != False:
            moveFunction.sortFunction(directory,check,".jpg")
            moveFunction.sortFunction(directory,check,".png")
        print("What about documents?")
        check = moveFunction.dirCheck(directory)
        if check != False:
            moveFunction.sortFunction(directory,check,".doc")
            moveFunction.sortFunction(directory,check,".docx")
            moveFunction.sortFunction(directory,check,".xlsx")
            moveFunction.sortFunction(directory,check,".pdf")
            moveFunction.sortFunction(directory,check,".pptx")

    if dirType == 2:
        print ("placeholder 2")

    print("finished")