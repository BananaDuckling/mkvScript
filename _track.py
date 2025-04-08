from subprocess import run
import os 


###Stores the track properties as a data frame

class Track:
    def __init__(self, name:str, category:str, id:int, lang:str, priority:int, default:bool, forced:bool, enabled:bool, fileFlag:bool = False, fileName:str = ''):
        self.fileName = fileName
        self.fileFlag = fileFlag
        self.name = name
        self.id = id
        self.category = category
        self.priority = priority
        self.language = lang
        self.default = int(default)
        self.forced = int(forced)
        self.enabled = int(enabled)
        
    def cmd(self, skip_file_name: bool = False): #Prints the mkvpropedit executable command
        if skip_file_name == True:
            start = 1
        else:
            start = 0
        if self.fileFlag == True: #Checks if the command should include the file name
            if os.path.isfile(self.fileName) == False:
                raise Exception (f'ERROR. File name : "{self.fileName}" could not be found.')
            elif not(self.fileName.endswith('.mkv'))    :
                raise Exception (f'ERROR. File "{self.fileName}" is not a Matroska video file')
            _cmd = f'mkvmerge "{self.fileName}" -e track=:{self.id + 1}'
        else:
            _cmd = f' -e track=:{self.id + 1}'
        for i, (attr, val) in enumerate(self.__dict__.items()): #Converts properties into an executable string
            if (i > 6):
                _cmd += f" -s flag-{attr}={val}" 
            elif (i = 6):
                _cmd += f" -s {attr}={val}"          
        return _cmd
    
    def execute(self):
        _cmd = self.cmd()
        output = run(args = _cmd, capture_output = True, check = True)
        if output.returncode == 0:
            print(f'MKV file, {self.name}, has beed successfully edited.')
        else:
            raise Exception(f'{self.name} could not be edited.')
