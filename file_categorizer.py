import os, shutil

selectFolder = input('Enter the path of folder to categorize(leave empty to categorize Downloads folder): ')
selectFolder = selectFolder.replace('\\', '\\\\')
if not selectFolder:
    # -------------os.path.expandvars('%username%') = nope
    # ------------os.path.expanduser('~') = C:\\Users\\nope
    selectFolder = os.path.join(os.path.expanduser('~'), 'Downloads')

# selectFolder = os.getcwd()

groupExt = {
            'Pictures': ('png', 'jpg', 'jpeg', 'webp', 'bmp'),
            'Documents': ('pdf', 'txt', 'docx', 'html', 'srt', 'csv', 'xlsx', 'htm', 'pptx', 'epub'),
            'Videos': ('mp4', 'ts', 'mkv', 'gif'),
            'Programs': ('exe', 'msi', 'img'),
            'Music': ('mp3', 'm4a', 'flac', 'aac'),
            'Apk': ('apk', 'jar'),
            'Compressed': ('zip', 'rar', '7z')
}

def makeDirIfNoDir(mapDirs):
    for folder in mapDirs.keys():
        os.makedirs(os.path.join(selectFolder, folder), exist_ok=True)
    return 'All required folder are available.'

def categorizeFiles(currFile, mapDirs):
    for dirr in mapDirs.keys():
        try:
            if currFile.endswith(groupExt[dirr]):
                # shutil.move(sourceFile, destinationFolder/destinationFile to rename)
                shutil.move(os.path.join(selectFolder, currFile), os.path.join(selectFolder, dirr))
                print(f'Sucessfully moved {currFile}')
                return True
        except shutil.Error as e:
            print(f'Couldnt move cuz {e}')
            return None
    else:
        print(f'Couldnt categorize {currFile} because its extension is not configured yet.')
        return None

moved = 0
notMoved = 0

print(makeDirIfNoDir(groupExt))

with os.scandir(selectFolder) as rootDir:
    for eachFile in rootDir:
        if eachFile.is_file():
            # if move is success, return True which adds (moved+1); otherwise if returned None, add (notmoved+1)
            if categorizeFiles(eachFile.name, groupExt):
                moved += 1
            else:
                notMoved += 1

print('Number of files moved were: ' + str(moved))
print('Numer of files not moved were: ' + str(notMoved))
input()


"""
def categorizeFiles(aFile):
    try:
        if aFile.endswith(groupExt.get('Pictures')):
            shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, 'Pictures'))

        elif aFile.endswith(groupExt.get('Music')):
            shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, 'Music'))

        elif aFile.endswith(groupExt.get('Videos')):
            shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, 'Videos'))

        elif aFile.endswith(groupExt.get('Documents')):
            shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, 'Documents'))

        elif aFile.endswith(groupExt.get('Programs')):
            shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, 'Programs'))

        elif aFile.endswith(groupExt.get('Apk')):
            shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, 'Apk'))

        elif aFile.endswith(groupExt.get('Compressed')):
            shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, 'Compressed'))

        # if aFile.endswith(('')):
        #     shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, ''))

        else:
            print(f'Couldnt categorize {aFile} because its extension is not configured yet.')
            return None
    except shutil.Error as e:
        print(f'Couldnt move cuz {e}')
        return None

    print(f'Sucessfully Moved {aFile}')
    return True
"""
