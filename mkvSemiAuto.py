from subprocess import run
import os 
from json import loads
import tkinter as tk
import pandas as pd
from _track import Track

### Creating a priority list for subtitles and audios
videoPriority = []
audioCodecPriority = []
subtitleDistroPriority = ["SubStationAlpha", "SRT" , "PGS", "Vort"]


def mkvCheck(file: str): #will be used for checking which case of the mkv file is used
    output = run(args = ['mkvmerge','-J', file], capture_output = True, check = True)
    if output.returncode == 0: #Returns 0 if command was successful
        mkv = loads(output.stdout)
        df = pd.DataFrame(mkv['tracks'])
        #print(pd.DataFrame(mkv['tracks']))
        print(df['properties'][0])
        hold = False
        command = f'mkvpropedit {file} '
        index = 0
        for track in mkv['tracks']:
            ### Key track properties
            try:
                trackName = track['properties']['track_name']
            except KeyError:
                print('Track has no name')
                trackName = ''
            trackStruc = Track(fileName = file, 
                               name = trackName, 
                               category = track['type'], 
                               id = track['id'], 
                               lang = track['properties']['language'], 
                               priority = 0, 
                               default = False, 
                               forced = False, 
                               enabled = True,
                               fileFlag = True)
            print('The name of the track is' + trackStruc.name)        
            #command += f'-e track=:{trackStruc.id + 1} '
            if trackStruc.category == 'subtitles':
                if hold == True:
                    trackLang = 'English'
                hold = not(hold)
            elif trackStruc.category == 'audio':
                #command = audioModify(track1.lang, track1.id, command)
                pass
            else:
                trackLang = 'Japanese'
            #command = ['mkvpropedit', file, ' -e', f'track:={str(trackID+1)}', '-s', f'name=\"{trackName}\"']
            #tempOut = run(args = command, check = True)
            if index == 0:
                cmdPrompt = trackStruc.cmd(skip_file_name = False)
            else:
                cmdPrompt += trackStruc.cmd(skip_file_name = True)
            index += 1
        #run(args=command)
        print(cmdPrompt)
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
        mkvCheck(input)
    else:
        raise Exception(f'ERROR: {input} IS NOT A VALID FILE NAME.')
    return 'dir'

def audioModify(trackLang: str, trackID: int, command: str):
    if trackLang == 'jpn':
        return 
    elif trackLang == 'eng':
        return #command+= f'-s name="English" '
    elif trackLang =='':
        #This needs to add another check
        pass
    else: 
        return #command+= f'-s flag-enabled=0 '

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

