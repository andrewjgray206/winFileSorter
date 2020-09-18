import os
import shutil

def sortFunction(directory,extension):
            for file in os.listdir(directory):
                if file.endswith(extension):
                    os.system("cls")
                    print("INITIATING COPY.")
                    print("---------------------------------------------------------")
                    shutil.move(file,exeDir)
                    print (file +" Moved to " + exeDir)

                else:
                    print(file + "isn't " + extension +", skipping...")
            
            print("ALL "+ extension+ "'s MOVED SUCCESSFULLY.")


def dirCheck(directory):
        exeDir = input()
        exeDir = directory  + "\\" + exeDir

        if os.path.exists(exeDir):
            print("Exists, continuing")
            return exeDir

        else:
            print("Directory doesn't exist...ERROR")
            return false