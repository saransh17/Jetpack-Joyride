import random
from ads import stuff
import numpy as np
class backgound_objects(stuff):
    def __init__(self):
        super().__init__()
        
        self._minx = -20
        self._ux = -2
        
class coins(backgound_objects):
    def __init__(self):
        super().__init__()
        
        self._shape = [
            "$$$",
            "$ $",
            "$$$"]
        
        self._colled = False
        self._x = self._maxx
        self._height = 3
        self._width = 3
        self._y = random.randint(self._miny+6, self._maxy-6)
        
    
    def taken(self):
        self._colled = 1

    def coll(self):
        return self._colled

class magnet(backgound_objects):
    def __init__(self):
        super().__init__()
        
        self._width = 1
        self._height = 1
        self._shape = [
            "U"]
        
        self._y = random.randint(self._miny+10, self._maxy-10)
        self._x = self._maxx

    def get_com(self):
        return self._x, self._y

class speed_boost(backgound_objects):
    def __init__(self):
        super().__init__()
        
        self._shape = [
            " ^^ ",
            "(  )",
            " ^^ "
        ]
        
        self._width = 4
        self._height = 3

        self._x = self._maxx
        self._y = random.randint(self._miny+8, self._maxy-8)

class beam(backgound_objects):
    def __init__(self):
        super().__init__()
        
        
        self._type = random.randint(1,4) - 1
        
        if self._type == 1:
            self._shape = [
                    "         ///",
                    "        /// ",
                    "       ///  ",
                    "      ///   ",
                    "     ///    ",
                    "    ///     ",
                    "   ///      ",
                    "  ///       ",
                    " ///        ",
                    "///         "]

            self._height = 10
            self._width = 12
        
        elif self._type == 2:
            self._shape = [
                    "---",
                    "|||",
                    "|||",
                    "|||",
                    "|||",
                    "|||",
                    "|||",
                    "|||",
                    "|||",
                    "---"]
            
            self._height = 10
            self._width = 3
                
        elif self._type == 3:
            self._shape = [
                    "|------------------|",
                    "|------------------|"]
            
            self._height = 2
            self._width = 20

        self._y = random.randint(self._miny+10, self._maxy-10)
        self._x = self._maxx


        
