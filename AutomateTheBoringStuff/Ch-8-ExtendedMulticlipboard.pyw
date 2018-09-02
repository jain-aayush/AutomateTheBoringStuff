"""
Extend the multiclipboard program in this chapter so that it has a delete <keyword> 
command line argument that will delete a keyword from the shelf. Then add a delete 
command line argument that will delete all keywords.
"""

# Usage: python <file_name>.pyw save <keyword> - Saves clipboard to keyword.
#        python <file_name> <keyword> - Loads keyword to clipboard.
#        python <file_name> list - Loads all keywords to clipboard.
#        python <file_name> delete <keyword> - Deletes a keyword.
#        python <file_name> delete - Deletes all Keywords.

import shelve, pyperclip, sys

mcbShelve = shelve.open('mcb')

if(len(sys.argv) == 3 ):
    if(sys.argv[1].lower() == 'save'):
        mcbShelve[sys.argv[2]] = pyperclip.paste()
        print("Keyword saved")
    elif(sys.argv[1].lower() == 'delete'):
        del mcbShelve[sys.argv[2]]
        print("The Given Key is deleted")

elif(len(sys.argv) == 2):
    if(sys.argv[1].lower() == 'list'):
        pyperclip.copy(str(list(mcbShelve.keys())))
        print("The Keywords are :")
        print(list(mcbShelve.keys()))

    elif(sys.argv[1].lower() == 'delete'):
        for keyword in mcbShelve.keys():
            del mcbShelve[keyword]
        print("All Keywords Deleted!")

    elif(sys.argv[1] in mcbShelve):
        pyperclip.copy(mcbShelve[sys.argv[1]])
        print(str(mcbShelve[sys.argv[1]]))
    
    else:
        print("No Such Keyword")
    
mcbShelve.close()