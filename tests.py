'''unit testing my functions'''

from fileAnalyzingFunc import analyzingFunc


def gitSupport():
    '''testing git support'''

    string = '''Your text with scientific results or something...
 Your text with scientific results,,,,,,,,,,,,,,,,
 or something... Your text with scientific results or something...
 Your text with scientific results!? or something...
'''


    output = ["Your text with scientific results or something...",
                " Your text with scientific results,,,,,,,,,,,,,,,,",
                " or something...", " Your text with scientific results or something...",
                " Your text with scientific results!?", " or something..."]

    for i in range(len(analyzingFunc.gitSupport(string))-1):
        if analyzingFunc.gitSupport(string)[i] != output[i]:
            return False


def tabComment():
    '''testing tab comment'''

    string="%your comment is here"
    assert analyzingFunc.commentFormat(string) == "%\tyour comment is here"




def blankLines():
    '''testing blank lines before a command'''

    text = "\subsection{first section}{subtitle}"
    list_user = ["\\section", "\\subsection", "2"]
    assert analyzingFunc.blankLines(list_user,"\t", 2, text) == 2*"\n"+2*"\t"+"\subsection{first section}{subtitle}", "blank lines test failed"


def beginBlocks():
    '''testing adding tab after begin blocks'''

    text = "\\begin{itemize}"
    list_ = []
    tab_counter = 2
    assert analyzingFunc.beginHandling(tab_counter,list_,"\t",text) == 4



def endBlocks():
    '''testing deleting tab after end blocks'''

    text = "\\end{itemize}"
    list_ = []
    tab_counter = 4
    assert analyzingFunc.endHandling(tab_counter,list_,"\t",text) == 2



def beginEndBlocks():
    '''testing begin and end blocks functions combined'''

    beginEndTestList = ["\\begin{document}", "\section{title}","\\begin{itemize}","\item{item1}","\item{item2}","\end{itemize}","\end{document}"]
    tab_counter = 0
    list_ = []
    list_to_be = ["\\begin{document}", "\\section{title}", "\t\\begin{itemize}", "\t\t\\begin{itemize}", "\t\t\\item{item1}", "\t\t\\item{item2}", "\t\\end{itemize}", "\\end{itemize}", "\\end{document}"]
    for i in range(len(beginEndTestList)):
        if beginEndTestList[i][1:6] == "begin" and "begin{document}" not in beginEndTestList[i]:
            tab_counter = analyzingFunc.beginHandling(tab_counter,list_,"\t",beginEndTestList[i])
            
        if beginEndTestList[i][1:4] == "end" and "end{document}" not in beginEndTestList[i]:
            tab_counter = analyzingFunc.endHandling(tab_counter,list_,"\t",beginEndTestList[i])
            
        list_.append("\t" * tab_counter + beginEndTestList[i])
    
    for i in range(len(list_)):
        if list_[i] != list_to_be[i]:
            return False

