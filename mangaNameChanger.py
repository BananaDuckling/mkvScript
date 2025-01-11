import os 
from tkinter import filedialog, messagebox
import re 

def fileParser(dir):
    print(os.listdir(dir))
    books = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f))]
    manga = True #It will check if its manga first, then comic books
    i=0
    for file in books:
        print(file)
        fileExt = file.split(".")
        file = file.replace("#","")
        #file = file.replace(".","")
        #print(f" hello ")
        if manga == True:
            test = re.split(" v\.?\s?| Vol\.?\s?|\(|.txt|.cbz|.cbr", file)
            print(test)
            try:
                num = int(test[1])
                newName = os.path.join(dir, f"{test[0]} Vol. {num}.{fileExt[-1]}")
                if i == 0:
                    foo = messagebox.askyesno("ATTENTION", f"The folder will be formatted as follows: \n\n{test[0]} Vol. {num}.{fileExt[-1]}\n\nDo you wish to proceed?")
                    if foo == False:
                        return "Aborted"
                os.rename(os.path.join(dir, file), newName)
                print(f"SUCCESS! File renamed to: {newName}")
            except Exception as e:
                print("ERROR: File names could not be renamed.")
                print(e)
                print("Testing for comic books")
                manga = False
        if manga == False:
            test = re.split(" chp\.? ?| Chp\.? ?|\(|\.?|.cbz|.cbr", file)
            try:
                num = test[1].zfill(3)
                newName = os.path.join(dir, f"{test[0]} Chp. {num}.{fileExt[-1]}")
                os.rename(os.path.join(dir, file), newName)
                print(f"SUCCESS! File renamed to: {newName}")
            except:
                print("ERROR: File name could not be renamed.")
                print("Could not rename the file")
                #print("Comic")
                messagebox.showerror("ERROR", "The file names could not be successfully changed.")
                return "Error"
        i+=1
    return "Success"


if __name__ == "__main__":
    fileDir = ""
    fileCheck = "" 
    dir = filedialog.askdirectory()
    
    #dir = "/home/duck/Documents/ParsingTest"
    #print(dir)
    
    exitState = fileParser(dir)
    if exitState == "Success":
        messagebox.showinfo("SUCCESS", "The file names have been successfully changed.")
    