
import re
from fileAnalyzingFunc import handlingFiles
from interface import commandFunc


def gitSupport(text):

        
    textSplit = re.findall('.*?[.,?,!,,]', text)

    counter = 0
    for i in range (0,len(textSplit)):
    
        if len (textSplit[i-counter]) == 1: # and textSplit[i-counter][0] == ".":
            
            textSplit[i-counter-1] = textSplit[i-counter-1] +  textSplit[i-counter] 
            textSplit.remove(textSplit[i-counter])
            counter += 1
    return textSplit




def stripper(textFilepath):
    textStripped = []
    textNewline = handlingFiles.readFileLines(textFilepath)
    
    for i in textNewline:
        
        if(i == "\n"):
            continue
        else:
            textStripped.append(i.strip())

    return textStripped




def commentFormat (line):
    
    return line[:1]+"\t" + line[1:]


def blankLines(BlankLinesList,tabIdent,tabCounter,i):
       
    numNewLines = int(BlankLinesList[len(BlankLinesList)-1])

    commandToBlankLines = BlankLinesList[0:len(BlankLinesList)-1]

    if re.split(' |{|,|}|,',i)[0] in commandToBlankLines:

        i = commandFunc.data.get("newline") * numNewLines + tabIdent * tabCounter + i

    return i

def beginHandling(tabCounter,linesValidated,tabIdent,i):
    tabCounter += 1
    linesValidated.append(tabIdent * tabCounter + i )
    tabCounter = tabCounter + 1
    return tabCounter


def endHandling(tabCounter,linesValidated,tabIdent,i):
    tabCounter -= 1
    linesValidated.append(tabIdent * tabCounter + i )
    tabCounter -= 1
    return tabCounter