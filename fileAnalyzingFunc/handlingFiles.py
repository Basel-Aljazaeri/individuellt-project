# functions that are used in reading and writing to files


def readFile(filePath):
    '''function readFile to read file.'''
    with open(filePath, "r") as f:
        lines = f.read()
    return lines


def writeToFile(filePath, listLines=[]):
    '''function writeFile to write to file.'''
    writing = open(filePath, "w")
    for i in listLines:

        writing.write(str(i) + "\n")

    writing.close()


def readFileLines(filePath):
    '''function to write to file.'''
    with open(filePath, "r") as f:
        lines = f.readlines()

    return lines
