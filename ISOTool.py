from pathlib import Path
import os
import shutil

folder_path = Path(os.getcwd())

def makeFolder(directory,gameName):
    name = (gameName.split('.')[0])
    newFolder = str(folder_path) + '\\'+name
    if name != 'game':
        try:
            print("Creating folder for", name)
            os.makedirs(newFolder)
        except FileExistsError:
            print(name, "folder already exists")
        if Path(newFolder+'\\*.iso').is_file():
            print('Renaming file to game.iso')
            os.rename(newFolder+'\\'+name+'.iso',newFolder+'\\game.iso')
        elif Path(newFolder+'\\game.iso').is_file():
            print(name,"exists as game.iso") 
        else:
            print("Moving file")
            shutil.move(str(folder_path)+'\\'+ gameName,newFolder)
            if Path(newFolder+'\\'+name+'.iso').is_file():
                print('Renaming file to game.iso')
                os.rename(newFolder+'\\'+name+'.iso',newFolder+'\\game.iso')

for i in folder_path.glob('**/*.iso'):  #iterating through paths
    gamename=str(i).split('\\')[-1]       #extracted file name
    directory=i
    makeFolder(directory,gamename)

