import os
import shutil

def sortFunction(directory,destination,extension):
            print("++++++++++++++++++++++++INITIATING COPY+++++++++++++++++++++++++++")
            print ("")
            for file in os.listdir(directory):

                if file.endswith(extension):
                    os.system("cls")
                    print("---------------------------------------------------------")
                    shutil.move(file,destination)
                    print (file +" Moved to " + destination)
                else:
                    print(file + "isn't " + extension +", skipping...")

            print ("----------------------------------------")
            print ("----------------------------------------")
            print("ALL "+ extension+ "'s MOVED SUCCESSFULLY.")


def dirCheck(directory):
        exeDir = input()
        exeDir = directory  + "\\" + exeDir
        print ("The directory to send to should be" + exeDir)

        if os.path.exists(exeDir):
            print("Exists, continuing")
            return exeDir

        else:
            print("Directory doesn't exist...ERROR")
            return false