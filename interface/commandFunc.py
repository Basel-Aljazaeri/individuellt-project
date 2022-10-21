# this module contains functions that are used in command line interface
import json
from genericpath import exists
from interface import stylingFunc

# configuration json file
with open ('jsonConfig/configDefault.json') as f:
    data = json.load(f)

# functions to check if provided file is valid and has a specified type.  
def fileTypeCheck(filePath):
    '''function to check if the file exists and has a specified type.'''
    splitFileName = filePath.split(".")
    if exists(filePath) == True:
        if splitFileName[len(splitFileName)-1] not in data.get("fileType"):
            print(stylingFunc.colors.red +
                "oops any provided filepath must be of type('bib' or 'tex')" + stylingFunc.colors.white
                    )
        else: return True
    else:
        print(stylingFunc.colors.red +
                "oops file path does't exist" + stylingFunc.colors.white
                    )
        

