import os

def text_edit(name):

    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white' ]
    color_codes = ['31', '32', '33', '34', '35', '36', '37']

    if name in colors:
        index = colors.index(name)
        code = color_codes[index]
        return f"\033[{code}m"
        
    elif name == "italic":
        return "\x1B[3m"
    
    elif name == "bold":
        return "\033[1m"
    
    elif name == "title":
        return "\033[1m\x1B[3m"
    
    elif name == "reset":
        return "\033[0m"

    #COLORS-----------------------------------------------------------------------------

    else:
        return ""