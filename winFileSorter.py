import os
import shutil
import moveFunction

while True:
    os.system("cls")
    print ("--------------------------------------------------------------------")
    directory = input("Enter Directory to sort. ( '0' to exit) ")

    if directory == "0":
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
        dirs = os.listdir(directory) #array of files
        for file in dirs:
            print(file) #prints file/folder name
        print("----------------------------------------------------------")

        print("So, where do you want executables and installers/ect to go?")
        check = moveFunction.dirCheck(directory)
        if check != False:
            moveFunction.sortFunction(directory,check,".exe") #need to reformat and have list of all file extensions and just run through.
            moveFunction.sortFunction(directory,check,".zip")
            moveFunction.sortFunction(directory,check,".msi")
            moveFunction.sortFunction(directory,check,".rar")
            moveFunction.sortFunction(directory,check,".7z")
        else:
            print("------------------------------------------------------")
            newDirCheck = input("So you didn't enter an existing directory, did you want to create one under that name?")
            if newDirCheck == True:
                os.mkdir(directory)
            
        print("Cool, how about images and media content?")
        check = moveFunction.dirCheck(directory)
        if check != False:
            moveFunction.sortFunction(directory,check,".jpg") #need to reformat and have list of all file extensions and just run through.
            moveFunction.sortFunction(directory,check,".png")
            moveFunction.sortFunction(directory,check,".jpeg")
            moveFunction.sortFunction(directory,check,".bmp")
        print("What about documents?")
        check = moveFunction.dirCheck(directory)
        if check != False:
            moveFunction.sortFunction(directory,check,".doc") #need to reformat and have list of all file extensions and just run through.
            moveFunction.sortFunction(directory,check,".docx")
            moveFunction.sortFunction(directory,check,".xlsx")
            moveFunction.sortFunction(directory,check,".pdf")
            moveFunction.sortFunction(directory,check,".pptx")
            moveFunction.sortFunction(directory,check,".html")
            moveFunction.sortFunction(directory,check,".odt")

    if dirType == 2:
        print ("Alright - These are going to sort them for you into a directory.")
        autoSortDir = "C:/PythonSorter"

        

    print("finished!!")