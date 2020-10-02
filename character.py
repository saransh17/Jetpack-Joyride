import random
from ads import stuff

class character(stuff):
    def __init__(self):
        super().__init__()
        self._lives = random.randint(1,5)
    

class mandalorian(character):
    def __init__(self):
        super().__init__()
        
        self._height = 3
        self._width = 5
        
        self._maxy = 49 # 52 - height
        self._maxx = 199 # 204 - width
        
        self._shieldActive = 0
        self._shieldRemaining = 0
        self._reshield = 0
        
        self._shape=[
                      "X X  ",
                      " X==>",
                      "X X  "]

    def get_com(self):
        return self._x + 0.5*self._width, self._y + 0.5*self._height

    def get_input(self, input):
        
        if self._y != self._maxx and input != 'w':#initial fall and stuff
          self._ay = .3
        else:
          self.ay = 0
        
        if input=='w':
          if self._y != self._miny:
            self._ay = -1
              
        if input=='d':
          if self._x != self._maxx:
            self._ux = 3
        elif input=='a':
          if self._x != self._minx:
            self._ux = -3
        else:
            self._ux = 0

        if self._reshield >= 1:
            self._reshield-=1
        
        if self._shieldActive == True:
            self._shieldRemaining-=1
            if self._shieldRemaining <= 0:
                self._shieldActive = False
               

        #if input==" " and not self._shieldActive and self._reshield==0:
        if input == " ":
          if self._reshield == 0 and self._shieldActive == False :            
            self._shieldActive=True
            self._shieldRemaining = 10
            self._reshield = 60

    def get_posi(self):
        return self._x,self._y,self._width     

    def current_get_posi(self):
        return self._x, self._y, self._width     

    def activate_shield(self, time):
        if self._shieldActive == False:
            self._shieldRemaining = time
            self._shieldActive=True

    def haveShield(self):
        return self._shieldActive

    def update_posi(self,x,y):
        #self._height+=1
        self._x += x
        self._y += y