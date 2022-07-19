from shutil import get_terminal_size as size
from textwrap import wrap

class Center:
    def get_win_size(self):
        cols, _ = size()
        self.tsize = cols

    def center_text(self, text:str):
        self.get_win_size()
        for line in wrap(text, self.tsize):
            print(line.center(self.tsize))
    
    def div(self):
        self.get_win_size()
        p = 0
        mydiv=""
        while p < (self.tsize)/2:
            mydiv+="-+"
            p+=1
        while len(mydiv) > self.tsize:
            mydiv = mydiv[0:-1]
        print(mydiv)

    def colored_text(self, text:str, color:str):
        '''
        Colorize any text given\n
        Colors:\n
        Black | Red | Green | Yellow | Blue | Magenta | Cyan | White

        '''
        try:
            color = color.lower()
            if color == "black":
                text=f"\033[30m {text}\033[00m"    
            elif color == "red":
                text=f"\033[31m {text}\033[00m"
            elif color == "green":
                text=f"\033[32m{text}\033[00m"
            elif color == "yellow":
                text=f"\033[33m{text}\033[00m"
            elif color == "blue":
                text=f"\033[34m{text}\033[00m"
            elif color == "magenta":
                text=f"\033[35m{text}\033[00m"
            elif color == "cyan":
                text=f"\033[36m{text}\033[00m"
            elif color == "white":
                text=f"\033[37m{text}\033[00m"
            else:
                raise InvalidColor
            return text

        except InvalidColor:
            print("Invalid Color Value")
        

class InvalidColor(Exception):
    pass

_inst = Center()
center = _inst.center_text
div = _inst.div
colorize = _inst.colored_text