from subprocess import run
import os 
from json import loads
import tkinter as tk
from pandas import DataFrame

###This object is not needed, just going to use variables
'''
class Track:
    def __init__(self, name:str, category:str, id:int, lang:str):
        self.name = name
        self.category = category
        self.id = id
        self.lang = lang
'''

trackProp = {
    "trackName": "",
    "trackType": "",
    "trackID": None,
    "trackLang": ""
}

def bashCall(file: str): #runs the bash script
    
    pass

def mkvCheck(file: str): #will be used for checking which case of the mkv file is used
    output = run(args = ["mkvmerge","-J", file], capture_output = True, check = True)
    if output.returncode == 0: #Returns 0 if command was successful
        mkv = loads(output.stdout)
        testDF = DataFrame(mkv["tracks"])
        print(testDF)
        hold = False
        for track in mkv["tracks"]:
            ### Key track properties
            try:
                trackName = track["properties"]["track_name"]
            except KeyError:
                print("Error has no track name")
                trackName = ""
            trackType = track["type"]
            trackID = track["id"]
            trackLang = track["properties"]["language"]
            #track1 = Track(name = trackName, category = trackType, id = trackID, lang = trackLang)
            print("The name of the track is" + track1.name)
            
            ### Testing output (void when finalized)
            print(trackType)
            print(trackID)
            print(trackLang)
            if trackType == "subtitles":
                if hold == True:
                    trackLang = "English"
                hold = not(hold)
            elif trackType == "audio":
                trackLanguage = "Undefined"
            else:
                trackLang = "Japanese"
            command = ["mkvpropedit", file, "-e", f"track:={str(trackID+1)}", "-s", f"name=\"{trackName}\""]
            tempOut = run(args = command, check = True)
    else:
        print("ERROR: json file could not be created. Ensure file is correct mkv format.")

def mkvDir(dir: str):
    mkvFiles = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f))]
    for file in mkvFiles:
        mkvCheck(os.path.join(dir,file))
    print(mkvFiles)

def fileCheck(input: str): #check if file or dir exists
    if os.path.isfile(input):
        print("PASSING. IS A FILE")
        mkvCheck(input)
    elif os.path.isdir(input):
        print("PASSING. IS A DIRECTORY")
        mkvCheck(input,)
    else:
        print("ERR: File does not exist")
    return

def audioModify(trackName: str, trackID: int):
    pass
def subtitleModify(trackName: str, trackID: int):
    pass

if __name__ == "__main__":
    ## NOTE:  This will be replaced by file selector ###
    dirIn = "/home/duck/Desktop/mkvProgramTest/Input"
    fileIn = "[SubsPlease] Dragon Ball Daima - 10 (1080p) [9D357C09].mkv"
    fileLoc = os.path.join(dirIn, fileIn)
    ##########

    fileCheck(fileLoc)
    #mkvDir(dirIn)

