from subprocess import run
import os 
from json import loads
import tkinter as tk
import pandas as pd

### Creating a priority list for subtitles and audios
videoPriority = []
audioCodecPriority = []
subtitleDistroPriority = ["SubStationAlpha", "SRT" , "PGS", "Vort"]



###This object is not needed, just going to use variables

class Track:
    def __init__(self, name:str, category:str, id:int, lang:str, priority:int, default:bool, forced:bool):
        self.name = name
        self.category = category
        self.id = id
        self.lang = lang
        self.priority = priority
        self.default = default
        self.forced = forced

def mkvCheck(file: str): #will be used for checking which case of the mkv file is used
    output = run(args = ['mkvmerge','-J', file], capture_output = True, check = True)
    if output.returncode == 0: #Returns 0 if command was successful
        mkv = loads(output.stdout)
        df = pd.DataFrame(mkv['tracks'])
        #print(pd.DataFrame(mkv['tracks']))
        print(df['properties'][0])
        hold = False
        command = f'mkvpropedit {file} '
        for track in mkv['tracks']:
            ### Key track properties
            try:
                trackName = track['properties']['track_name']
            except KeyError:
                print('Error has no track name')
                trackName = ''
            trackType = track['type']
            trackID = track['id']
            trackLang = track['properties']['language']
            trackStruc = Track(name = trackName, 
                           category = trackType, 
                           id = trackID, 
                           lang = trackLang,
                           priority = 0,
                           default = False,
                           forced = False)
            print('The name of the track is' + trackStruc.name)
            
            ### Testing output (void when finalized)
            # print(trackType)
            # print(trackID)
            # print(trackLang)
            command = f'-e track=:{trackID + 1} '
            if trackType == 'subtitles':
                if hold == True:
                    trackLang = 'English'
                hold = not(hold)
            elif trackType == 'audio':
                command = audioModify(track1.lang, track1.id, command)
            else:
                trackLang = 'Japanese'
            command = ['mkvpropedit', file, ' -e', f'track:={str(trackID+1)}', '-s', f'name=\"{trackName}\"']
            tempOut = run(args = command, check = True)
        #run(args=command)
    else:
        print('ERROR: json file could not be created. Ensure file is correct mkv format.')

def mkvDir(dir: str):
    mkvFiles = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f))]
    for file in mkvFiles:
        mkvCheck(os.path.join(dir,file))
    print(mkvFiles)

def fileCheck(input: str): #check if file or dir exists
    if os.path.isfile(input):
        print('PASSING. IS A FILE')
        mkvCheck(input)
    elif os.path.isdir(input):
        print('PASSING. IS A DIRECTORY')
        mkvCheck(input,)
    else:
        print('ERR: File does not exist')
    return 'dir'

def audioModify(trackLang: str, trackID: int, command: str):
    if trackLang == 'jpn':
        return command+= f'-s name="Japanese" '
    elif trackLang == 'eng':
        return command+= f'-s name="English" '
    elif trackLang =='':
        #This needs to add another check
        pass
    else: 
        return command+= f'-s flag-enabled=0 '

def subtitleModify(trackName: str, trackID: int):
    
    pass

if __name__ == "__main__":
    ## NOTE:  This will be replaced by file selector ###
    dirIn = '/home/duck/Desktop/mkvProgramTest/Input'
    fileIn = '[SubsPlease] Dragon Ball Daima - 10 (1080p) [9D357C09].mkv'
    fileLoc = os.path.join(dirIn, fileIn)
    ##########

    fileCheck(fileLoc)
    #mkvDir(dirIn)

