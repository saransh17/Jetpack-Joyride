from ads import stuff,bullets,shell
import colorama 
from character import mandalorian as mand
import os
from obstacles import coins,beam,magnet,speed_boost
import random
import time
import math
from colorama import Back,Fore,Style
import sys
colorama.init()
def pos(x, y):
	return '\x1b[%d;%dH' % (y, x)

class session:
    
    def reset(self):
        self.__objectList = []

    def __init__(self):
        self.__framex = 204
        self.__framey = 53
        self.__check_col = 0
        self.__objectList = []
        self.__count = 0
        self.__lives = 100
        self.__magyo = 0
        self.__time = 75
        self.__stime=time.time()
        self.__rando = 0
        self.__mag = 0
        self.__boosttime = 10
        self.__boostcheck = 0
        self.__frame = [' ']*10865
        self.__mandoIndex = 0
        self.__frameCount = 0
        self.__shieldc = False
        self.__shieldt = 700
        self.__flag=0
        self.__fl=0
    	
        
        
    def addobject(self, obj):
        self.__objectList.append(obj)

    

    def next_frame(self):
        self.__make_frame()
        self.__init_obs()
        self.__frameCount += 1
        
        
        self.__checkboost()
        self.__magnetic()
        self.__rando += 1
        
        self.__print_obs()

    def __make_frame(self):
        self.__frame = [[' ' for i in range(0,self.__framex)] for j in range(0,self.__framey)]
        self.__frame[-1] = ['~']*self.__framex
        self.__frame[0] = ['x']*self.__framex
        self.__frame[1] = " "*100+"SCORE : "+str(self.__count)+" "*100
        self.__frame[2] = " "*100+"TIME : "+str(math.ceil(self.__time + self.__stime -time.time()))+" "*100
        self.__frame[3] = " "*100+"HEALTH : "+str(self.__lives)+" "*100
        self.__frame[4] = ['x']*int(self.__framex)
        

    def __init_obs(self):
        count=121

        if self.__rando % 20:
            self.__check_col+=1


        if self.__rando % count == 0:
            
            self.__objectList.append(magnet())
            self.__magyo+=1
            self.__mag = self.__objectList[-1]
            self.__flag=1

        if self.__rando % (count+51) == 0:
            self.__objectList.append(speed_boost())
            self.__flag=2

        count%=251
        count+=1
        
        if self.__rando % 5 == 0:
            self.__objectList.append(coins())
            self.__flag=3
            
        if self.__rando % 12 == 0:
            self.__objectList.append(beam())
            self.__flag=4
        
    def __print_obs(self):
        occupied = [[None for i in range(self.__framex)] for j in range(self.__framey)]
        visible=0

        for obj in self.__objectList:
            objx,objy = obj.get_posit(speed_boost) 
            
            objy = int(objy)
            objx = int(objx)
            visible = 0
            v_flag = False
            shape = obj.get_shape()
            width,height = obj.get_dim()
                        
            for x in range(0,width):
                for y in range(0,height):
                    if shape[y][x] != " " and (objx+x) in range(0,self.__framex):
                    	if (objy+y) in range(0,self.__framey):
                    		self.__frame[objy+y][objx+x] = (shape[y][x])
                    		if occupied[objy+y][objx+x]!=None:
                    			v_flag = True
                    			self.__collision(occupied[objy+y][objx+x], obj)
                    		if v_flag == True:
                    			v_flag = False
                    		occupied[objy+y][objx+x] = obj
                    		visible = 1
            if visible == 0:
            	self.remove_obs(obj)

    def __magnetic(self):
        if self.__mag in self.__objectList:
        	if isinstance(self.__mag, magnet):
        		x = -1
        		y = -0.2
        		mandox, mandoy = self.__objectList[0].get_com()
        		magx,magy = self.__mag.get_com()
        		
        		if mandox < magx:
        			x = 1
        		if mandoy < magy:
        			y = 0.2
        		
        		if mandoy == magy:
        			y = 0
        		if mandox == magx:
        			x = 0

        		self.__objectList[0].update_posi(x,y)
            
    def __checkboost(self):
        if self.__boostcheck and self.__boosttime > 0:
            self.__boosttime-=1
        elif self.__boostcheck and self.__boosttime ==0:
        	self.__boostcheck = False

    def retboost(self):
    	if self.__boostcheck:
    		return 1
    	else:
    		return 0

    def setInput(self, input):
        if input=='k':
            a,b,c = self.__objectList[0].get_posi()
            x = a + c/2
            y = b + 1
            self.__objectList.append(shell(x,y))
        self.__objectList[self.__mandoIndex].get_input(input)

    def ac_shield(self):
        if self.__shieldc == False and self.__shieldt>=600:
            self.__fl=1
            self.__shieldt = 100
            self.__shieldc = True


    def shieldinc(self):
        if self.__shieldt < 700:
            self.__shieldt +=1

    # def printFrame(self):
    #     print(pos(0,0),sep="", end='')
    #     print()
    #     for j in range(self.__framey):
    #     	if math.ceil(self.__time + self.__stime -time.time()) >= 0:
    #     		for i in range(self.__framex):
    #     			pixel = self.__frame[j][i]
    #     			char = pixel
    #     			print(Back.RED + Fore.BLUE + char + Style.RESET_ALL, end="",sep="")
    #     		print()

    def printFrame(self):
        print(pos(0,0),sep="",end='')
        print()

        for j in range(self.__framey):
            if math.ceil(self.__time + self.__stime - time.time()) >=0:
                for i in range(0,self.__framex):
                    pixel= self.__frame[j][i]
                    char=pixel
                    if(char=='$'):
                        print(Fore.YELLOW+Back.YELLOW+ char + Style.RESET_ALL,end="",sep="")
                    elif(char=='/'or char=='|' or char=='_' or char=='-'):
                        print(Fore.RED +Back.RED+ char +Style.RESET_ALL,end="",sep="")
                    elif(char=='='):
                        print(Fore.BLUE +char+Style.RESET_ALL,end="",sep="")
                    elif(char=='~'):
                        print(Fore.GREEN+Back.GREEN+char+Style.RESET_ALL,end="",sep="")
                    elif(char=='X'):
                        print(Fore.WHITE+char,end="",sep="")
                    elif(char=='x'):
                        print(Fore.WHITE+Back.BLUE+char+Style.BRIGHT+Style.RESET_ALL,end="",sep="")
                    elif(char=='>' or char=='(' or char==')' or char=='^'):
                        print(Fore.GREEN+char+Style.BRIGHT,end="",sep="")
                    elif(char=='U'):
                        print(Fore.MAGENTA+Back.MAGENTA+char+Style.RESET_ALL,end="",sep="")
                    elif(self.__fl==1):
                        print(Back.CYAN+char+Style.RESET_ALL,end="",sep="")
                    else:
                        print(char,end="",sep="")

                print()
    
    def remove_obs(self,obj):
        try:
            self.__objectList.remove(obj)
        except:
            pass

    def yeet_obstacle(self,obj):
        try:
            self.__objectList.remove(obj)
        except:
        	print("Not able to yeet!")
            pass

    def check_c(self):
        #print(self.__shieldt)
        if self.__shieldc== True:
            self.__shieldt -=1
            if self.__shieldt <= 0:
                self.__shieldc=False
                self.__fl=0

    def decshield(self):
        if self.__shieldc == True:
            self.__shieldt -=1

    def reduce_shield(self):
        if self.__shieldc:
            self.__shieldt -= 1

    def __collision(self, obj1, obj2):
        if self.__lives<-3:
            print(chr(27) + "[2J") #Escape Sequence
            print(Back.BLUE+"Lmao Loser"+Style.BRIGHT)
            time.sleep(1)
            sys.stderr.write("\x1b[2J\x1b[H")
            exit()

        if self.__isPairof(obj1,obj2,mand,coins):
            if obj2.coll() == False:
                self.remove_obs(obj2)
                self.__count+=1
                obj2.taken()
                
        if self.__isPairof(obj1,obj2,mand,beam):
            if self.__shieldc == False:
                self.remove_obs(obj2)
                self.__lives-=4
            else:
                self.remove_obs(obj2)
                self.__count+=2

                
            #if obj1.haveShield() == False:
            #    self.__lives-=1
                
        if self.__isPairof(obj1,obj2,mand,speed_boost):
            self.remove_obs(obj2)
            self.__boostcheck = True
            self.__boosttime = 190

        if self.__isPairof(obj1,obj2,shell,beam):
            self.__count += 2
            self.remove_obs(obj1)
            self.remove_obs(obj2)
        
    def __isPairof(self,obj1,obj2,class1,class2):
        return (isinstance(obj1,class1) and isinstance(obj2,class2)) or (isinstance(obj1,class2) and isinstance(obj2,class1))
    
