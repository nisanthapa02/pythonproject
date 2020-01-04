import os, shutil

selectFolder = input('Enter the path of folder to categorize: ')
selectFolder = selectFolder.replace('\\', '\\\\')
if not selectFolder:
    # os.path.expanduser('~') = C:\\Users\\nope
    # os.path.expandvars('%username%') = nope
    selectFolder = os.path.join(os.path.expanduser('~'), 'Downloads')

# selectFolder = os.getcwd()

def createIfNoFolder():
    neededFolders = ('Pictures', 'Documents', 'Videos', 'Programs', 'Music', 'Apk', 'Compressed')
    for folder in neededFolders:
        os.makedirs(os.path.join(selectFolder, folder), exist_ok=True)
    return 'All folder available.'

def categorizeFiles(aFile):
    try:
        if aFile.endswith(('png', 'jpg', 'jpeg', 'webp', 'bmp')):
            shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, 'Pictures'))

        elif aFile.endswith(('mp3', 'm4a', 'flac', 'aac')):
            shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, 'Music'))

        elif aFile.endswith(('mp4', 'ts', 'mkv', 'gif')):
            shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, 'Videos'))

        elif aFile.endswith(('pdf', 'txt', 'docx', 'html', 'srt', 'csv', 'xlsx', 'htm', 'pptx', 'epub')):
            shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, 'Documents'))

        elif aFile.endswith(('exe', 'msi', 'img')):
            shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, 'Programs'))

        elif aFile.endswith(('apk', 'jar')):
            shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, 'Apk'))

        elif aFile.endswith(('zip', 'rar', '7z')):
            shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, 'Compressed'))

        # if aFile.endswith(('')):
        #     shutil.move(os.path.join(selectFolder, aFile), os.path.join(selectFolder, ''))

        else:
            print(f'Couldnt categorize {aFile}')
            return None
    except shutil.Error as e:
        print(f'Couldnt move cuz {e}')
        return None

    print('Moved')
    return True

moved = 0
notMoved = 0

print(createIfNoFolder())

with os.scandir(selectFolder) as rootDir:
    for eachFile in rootDir:
        if eachFile.is_file():
            #
            if categorizeFiles(eachFile.name):
                moved += 1
            else:
                notMoved += 1

print('Number of files moved were: ' + str(moved))
print('Numer of files not moved were: ' + str(notMoved))
input()
