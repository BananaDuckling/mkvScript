import os 
from tkinter import filedialog
import re 

def fileParser(dir):
    print(os.listdir(dir))
    books = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f))]
    manga = True #It will check if its manga first, then comic books
    for file in books:
        print(file)
        fileExt = file.split(".")
        file = file.replace("#","")
        #file = file.replace(".","")
        if manga == True:
            test = re.split(" v\.?\s?| Vol\.?\s?|\(|.txt|.cbz|.cbr", file)
            print(test)
            try:
                num = test[1].zfill(2)
                newName = os.path.join(dir, test[0] + " Vol. " + num + "." + fileExt[-1])
                os.rename(os.path.join(dir, file), newName)
                print(f"SUCCESS! File renamed to: {newName}")
            except:
                print("ERROR: File names could not be renamed.")
                print("Testing for comic books")
                manga = False
        if manga == False:
            test = re.split(" chp\.? ?| Chp\.? ?|\(|\.?|.cbz|.cbr", file)
            try:
                num = test[1].zfill(3)
                newName = os.path.join(dir, test[0] + " Chp. " + num + "." + fileExt[-1])
                os.rename(os.path.join(dir, file), newName)
                print(f"SUCCESS! File renamed to: {newName}")
            except:
                print("ERROR: File name could not be renamed.")
                print("Could not rename the file")
                #print("Comic")


if __name__ == "__main__":
    fileDir = ""
    fileCheck = "" 
    dir = filedialog.askdirectory()
    '''
    dir = "/home/duck/Documents/ParsingTest"
    print(dir)
    '''
    fileParser(dir)
    