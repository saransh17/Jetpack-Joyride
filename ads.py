from colorama import Fore,Back
class stuff:
    def __init__(self):

        
        self._shape = [[' ']]
        self._uy = 0
        self._ay = 0
        self._ux = 0
        self._ax = 0
        self._x = 26
        self._y = 2

        self._minx = 0
        self._miny = 5

        self._height = 1
        self._width = 1

        self._maxy = 48
        self._maxx = 204
        

    def get_dim(self):
        return self._width,self._height

    def get_shape(self):
        return self._shape

    def get_posit(self,speedBoost):
        
        self._y += self._uy + self._ay/2
        self._x += self._ux + self._ax/2
        self._ux += self._ax

        
        if self._x < self._minx:
            self._x = self._minx

        if self._x > self._maxx:
            self._x = self._maxx

        if self._y == self._maxy and self._uy>0:
            self._uy = 0
        if self._y == self._miny and self._uy<0:
            self._uy = 0
        self._uy += self._ay
        if self._y < self._miny:
            self._y = self._miny

        if self._y > self._maxy:
            self._y = self._maxy 
        
        
        return self._x, self._y
         
class bullets(stuff):
    def __init__(self, x, y):
        super().__init__()

        self._maxx = 250
        self._y = y
        self._x = x

class shell(bullets):
    def __init__(self, x, y):
        super().__init__(x,y)
        
        self._shape = ['=>']
        self._width = 2
        self._ux = 2.5 