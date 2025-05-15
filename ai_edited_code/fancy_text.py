import os  # Importing os module, though it's not used in this function

# Function to return ANSI escape codes for text formatting based on input name
def text_edit(name):

    # List of color names supported
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white' ]
    
    # Corresponding ANSI color codes for the colors listed above
    color_codes = ['31', '32', '33', '34', '35', '36', '37']

    # If the input name matches a supported color, return the ANSI escape code for that color
    if name in colors:
        index = colors.index(name)  # Get the index of the color
        code = color_codes[index]   # Get the corresponding ANSI color code
        return f"\033[{code}m"      # Return the formatted ANSI escape sequence
        
    # Return ANSI escape code for italic text
    elif name == "italic":
        return "\x1B[3m"
    
    # Return ANSI escape code for bold text
    elif name == "bold":
        return "\033[1m"
    
    # Return ANSI escape code for bold and italic combined (used as a "title" style)
    elif name == "title":
        return "\033[1m\x1B[3m"
    
    # Return ANSI escape code to reset text formatting
    elif name == "reset":
        return "\033[0m"

    # COLORS-----------------------------------------------------------------------------
    # If the input name doesn't match any known option, return an empty string
    else:
        return ""
