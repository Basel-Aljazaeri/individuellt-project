'''
    importing argprse to handle the command line arguments
'''
import argparse
from fileAnalyzingFunc import handlingFiles
from fileAnalyzingFunc import analyzingFunc
from interface import commandFunc


parser = argparse.ArgumentParser()

# the parser
parser = argparse.ArgumentParser(
    prog='laLinter',

    description="welcome to TrustLinter. ")

# the input file arg
parser.add_argument('fileName',
                    type=str,
                    help="Enter the path of the inputFile")


# the new line for better git support arg (optional)
parser.add_argument('--gitSupport', '--g',
                    action="store_true",
                    dest="git",
                    help="Enter either (--git) or (--g) to better git support.")


# blank lines after (optional, adjustable)
parser.add_argument('--newline', '--n',
                    nargs="+",
                    dest="newline",
                    help='''
                            Enter either (--newline) or (--n) followed by the
                            commands you want to add separated by the number of blank lines.
                            Example: --n /section /subsection 2 
                            ''')
# Executing the parser args
args = parser.parse_args()


# checking if the input file has a specified type.

if args.git is not False:
    commandFunc.data["gitSupport"] = args.git

if args.newline is not None:
    commandFunc.data["blankLines"] = args.newline


tabIdent = commandFunc.data.get("indent")
newLine = commandFunc.data.get("newline")
# setting a newList variable to contain the split of gitSupport function


'''

    the function to reformat the tex,bib files
'''
def main():
    if commandFunc.fileTypeCheck(args.fileName) is True:
        inputFilePath = args.fileName
    else:
         return False 
    LinesModifiedSplit = analyzingFunc.stripper(inputFilePath)
    linesValidated = []
    tabCounter = 0
    BlankLinesList = commandFunc.data.get("blankLines")
    
    for i in LinesModifiedSplit:
        if commandFunc.data.get("gitSupport") == True:

            if len(i) != 0 and i[0] != "\\" and i[0] != "%":
                newList = []
                stringGit = ""
                if len(analyzingFunc.gitSupport(i)) > 1:

                    newList.append(analyzingFunc.gitSupport(i)[0])
                    for j in range(1, len(analyzingFunc.gitSupport(i))):
                        subString = tabIdent * tabCounter + \
                            ((analyzingFunc.gitSupport(i))[j]).strip()
                        newList.append(subString)
                    for k in range(len(newList)):
                        # if statement to make sure that no new lines added at the end of the list
                        if k < len(newList)-1:
                            stringGit += newList[k] + "\n"
                        else:
                            stringGit += newList[k]
                    i = stringGit

        if len(i) != 0:

            
            if len(BlankLinesList) != 0:
                i = analyzingFunc.blankLines(
                    BlankLinesList, tabIdent, tabCounter, i)

        if i[1:6] == "begin" and "begin{document}" not in i:
        
            tabCounter = analyzingFunc.beginHandling(
                tabCounter, linesValidated, tabIdent, i)
    
            continue

        if i[1:4] == "end" and "end{document}" not in i:
            tabCounter = analyzingFunc.endHandling(
                tabCounter, linesValidated, tabIdent, i)
      
            continue

        if len(i) != 0 and i[0] == "%":
            i = analyzingFunc.commentFormat(i)

        linesValidated.append(tabIdent * tabCounter + i)

    handlingFiles.writeToFile("TrustLinter.tex", linesValidated)
    return True

if __name__ == "__main__":
    main()

