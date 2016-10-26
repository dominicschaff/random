BLACK  = 0
RED    = 1
GREEN  = 2
YELLOW = 3
BLUE   = 4
PURPLE = 5
CYAN   = 6
WHITE  = 7

NORMAL    = 0
BOLD      = 1
LIGHT     = 2
OTHER     = 3
UNDERLINE = 4
FLASH     = 5
OTHER2    = 6
INVERT    = 7

def rt(text, foreground, background=0, style=0):
    return "\x1b[%d;3%d;4%dm%s\x1b[0m"%(style, foreground, background, text)

def pt(text, foreground, background=0, style=0):
    print(rt(text, foreground, background, style))