import os

def displayFiles(pathname):
    if os.path.isfile(pathname):
        print('File Name:', pathname)
        openFiles(pathname)
    elif os.path.isdir(pathname):
        print('Directory Name:', pathname)
        openDirectory(pathname)

def openFiles(pathname):
    file = open(pathname, 'r')
    for line in file:
        print(line)
    file.close()
    return

def openDirectory(pathname):
    listFiles = os.listdir(pathname)
    for (file) in listFiles:
        openPath = pathname + str(file)
        if not file.startswith('.DS'):
            if os.path.isfile(openPath):
                openPath = pathname + str(file)
                contents = open(openPath, 'r')
                print('File Name:', str(pathname) + str(file), contents.read())
                contents.close()
            else:
                openPath = pathname + str(file) + "/"
                openDirectory(openPath)
            
           
