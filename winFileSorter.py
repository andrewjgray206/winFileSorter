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
            moveFunction.sortFunction(check,".exe")
            moveFunction.sortFunction(check,".zip")
            moveFunction.sortFunction(check,".msi")
        print("Cool, how about images and media content?")
        check = moveFunction.dirCheck(directory)
        if check != False:
            moveFunction.sortFunction(check,".jpg")
            moveFunction.sortFunction(check,".png")
        print("What about documents?")
        check = moveFunction.dirCheck(directory)
        if check != False:
            moveFunction.sortFunction(check,".doc")
            moveFunction.sortFunction(check,".docx")
            moveFunction.sortFunction(check,".xlsx")
            moveFunction.sortFunction(check,".pdf")
            moveFunction.sortFunction(check,".pptx")

    if dirType == 2:
        print ("placeholder 2")