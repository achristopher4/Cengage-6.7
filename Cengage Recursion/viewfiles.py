import os

def displayFiles(pathname):
    orginal = pathname
    pathname = makeReadable(pathname)
    
    if os.path.isfile(pathname):
        print('File Name:', orginal)
        openFiles(pathname)
    elif os.path.isdir(pathname):
        print('Directory Name:', orginal)
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
                contents = open(openPath, 'r')
                print('File Name:', finalPrint(pathname) + '.' + str(file))
                print(contents.read())
                contents.close()
            else:
                openDir = openPath + '/'
                openDirectory(openDir)

def makeReadable(pathname):
    seperate = pathname.split('/')
    removePeriod = []
    for i in range(len(seperate)):
        find = seperate[i]
        if find.startswith('.'):
            new = find.replace('.','',1)
            removePeriod.append(new)
        elif find != '':
            new = find
            removePeriod.append(new)
    lastValue = removePeriod[-1]
    reconstructionList = []
    for i in range(len(removePeriod)):
        determine = removePeriod[i]
        if determine == lastValue:
            if os.path.isfile(determine):
                reconstructionList.append('/'+ determine)
            elif os.path.isfile(removePeriod[i-1] + '/' + determine):
                reconstructionList.append('/'+ determine)
            else:
                reconstructionList.append('/'+ determine + '/')
        else:
            reconstructionList.append('/'+determine)
    final = ''
    final = final.join(reconstructionList)
    return final

def finalPrint(pathname):
    seperate = pathname.split('/')
    removePeriod = []
    for i in range(len(seperate)):
        find = seperate[i]
        if find.startswith('.'):
            new = find.replace('.','',1)
            removePeriod.append(new)
        elif find != '':
            new = find
            removePeriod.append(new)
    lastValue = removePeriod[-1]
    reconstructionList = []
    for i in range(len(removePeriod)):
        determine = removePeriod[i]
        if determine == lastValue:
            if os.path.isfile(determine):
                reconstructionList.append('/'+ determine)
            elif os.path.isfile(removePeriod[i-1] + '/' + determine):
                reconstructionList.append('/'+ determine)
            else:
                reconstructionList.append('/'+ '.' + determine + '/')
        else:
            reconstructionList.append('/'+determine)
    final = ''
    final = final.join(reconstructionList)
    return final
