import os

def text_edit(name):
    
    if name == "italic":
        return "\x1B[3m"
    
    elif name == "bold":
        return "\033[1m"
    
    elif name == "title":
        return "\033[1m\x1B[3m"


    else:
        return ""