CONTENTS OF THIS FILE
---------------------
 * Introduction
 * commands
 * restriction 
 * limitation


INTRODUCTION
------------

TrustLinter is cli application that reformats LaTex Texts so it become more organized
and follow a specific pattern.

Even though the app has pre defined rules to follow, it also offers the user a space
of customization to define his very own rules.

For now the app is only available on windows and you have to make sure that you have python
installed to run properly.



*COMMANDS
---------


POSITIONAL ARGUMENTS:
---------------------

*   the name of mainFile(main.py) and followed by the name of file.


OPTIONAL ARGUMENTS:
------------------

*   --h to show all commands.

*   --g to get a better git_support.

*   --n to add blank lines between section, chapters...etc
        this command must be followed by at least tow arguments as showed below,
        the first one the the command, second one is the command you want to add blank
        lines before and the number of blank lines as last argument.
        --n \\sections 2


RESTRICTION 
-----------

There are some restriction to you have to follow as a user to make sure the app works in a
proper way.

*   The file to be lintered must be of a specific type [bib, tex]

*   The file must be in the same path as (main.py) file.

*   The file should not include tow commands in the same line 
        ex: \begin{document}\begin{itemize}

*   NO spaces is allowed between comment command(%) and the comment.

*   If no optional commands have given then the app will be running using default setting.


LIMITATION 
----------


*   The app resets all the lines of the file to be lintered and even gets rid of all blank
    lines before the reformatting process begins. this means that all spaces and tabs before
    lines will be deleted, that applies also on blank lines.

*   The app will be create the linterd file with the name(TrustLinter.tex). 