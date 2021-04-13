import global1
import function
import random
from powerups import *
import numpy
import os
class ball1:
        def __init__(self, x, y):
                self.x = x
                self.y = y
                self.xinc = 0
                self.yinc = 0
                self.power = 0
                self.grab = 0
                self.deploy = 1
        def sidecollide(self):
        # self.xinc = -self.xinc
                self.yinc = -self.yinc

        def topcollide(self):
                self.xinc = -self.xinc

        def retcollide(self):
                self.yinc = -self.yinc
                self.xinc = -self.xinc

        def paddlecollide(self,v):
                self.xinc = -self.xinc
                if self.y + v > global1.objpaddle.y + global1.paddlelength // 2:
                        self.yinc = self.yinc * (self.y + v - global1.objpaddle.y - (global1.paddlelength // 2))
                        if self.yinc < 0:
                                self.yinc = -self.yinc
                elif self.y + v < global1.objpaddle.y + global1.paddlelength // 2:
                        self.yinc = -self.yinc * (self.y + v - global1.objpaddle.y - (global1.paddlelength // 2))
                        if self.yinc > 0:
                                self.yinc = -self.yinc

        def colourchange(self,index):
                if type(global1.objbrick[index]).__name__ == "rbrick":
                        global1.objbrick[index].contact = 0
                if self.power == 1:
                        global1.objbrick[index].strength = 0
                else:        
                        if global1.objbrick[index].strength != -1 and global1.objbrick[index].strength != 0:    
                                global1.objbrick[index].strength = global1.objbrick[index].strength - 1
                                if global1.objbrick[index].strength == 0 and global1.objbrick[index].defense == 0:
                                        global1.score = global1.score + 1
                                        seq = [6,7,8,9,10,11,12]
                                        # seq1 = [12]
                                        a = random.choice(seq)
                                        if a==6:
                                                global1.objexppaddle.append(expandpaddle(global1.objbrick[index].x,global1.objbrick[index].y,self.xinc,self.yinc,1))
                                                global1.screen[global1.objbrick[index].x][global1.objbrick[index].y] = 6
                                        elif a==7:
                                                global1.objshrpaddle.append(shrinkpaddle(global1.objbrick[index].x,global1.objbrick[index].y,self.xinc,self.yinc,1))
                                                global1.screen[global1.objbrick[index].x][global1.objbrick[index].y] = 7
                                        elif a==8:
                                                global1.objfastball.append(fastball(global1.objbrick[index].x,global1.objbrick[index].y,self.xinc,self.yinc,1))
                                                global1.screen[global1.objbrick[index].x][global1.objbrick[index].y] = 8
                                        elif a==9:
                                                global1.objthruball.append(thruball(global1.objbrick[index].x,global1.objbrick[index].y,self.xinc,self.yinc,1))
                                                global1.screen[global1.objbrick[index].x][global1.objbrick[index].y] = 9
                                        elif a==10:
                                                global1.objpaddlegrab.append(paddlegrab(global1.objbrick[index].x,global1.objbrick[index].y,self.xinc,self.yinc,1))
                                                global1.screen[global1.objbrick[index].x][global1.objbrick[index].y] = 10
                                        elif a==11:
                                                global1.objballmultiply.append(balls(global1.objbrick[index].x,global1.objbrick[index].y,self.xinc,self.yinc,1))
                                                global1.screen[global1.objbrick[index].x][global1.objbrick[index].y] = 11

                                        elif a==12:
                                                global1.objshoot.append(shoot(global1.objbrick[index].x,global1.objbrick[index].y,self.xinc,self.yinc,1))
                                                global1.screen[global1.objbrick[index].x][global1.objbrick[index].y] = 12
                                                                                    
                                global1.screen[global1.objbrick[index].x][global1.objbrick[index].y] = global1.screen[global1.objbrick[index].x][global1.objbrick[index].y] - 1                         

        def collide(self):
                if self.xinc < 0 and self.yinc < 0 and (self.y * self.y + self.x * self.x < self.yinc * self.yinc + self.xinc * self.xinc):
                        self.retcollide()         
                elif self.y in range(0, abs(self.yinc)) or (self.y in range(119 - abs(self.yinc), 119)):
                        self.sidecollide()
                elif global1.level==3 and self.x in range(2,abs(self.xinc)+2) and (self.y + self.yinc)  in range(global1.objboss.y,global1.objboss.y + 4):
                        self.topcollide()
                        global1.health = global1.health - 1
                # elif global1.level==3 and self.x in range(2,abs(self.xinc)+2) and ((self.y + self.yinc) == (global1.objboss.y - 1) or (self.y + self.yinc) == global1.objboss.y + 1):
                #         self.retcollide()
                #         global1.health = global1.health - 1       
                elif self.x in range(1,abs(self.xinc) + 1):
                        self.topcollide()                
                else: 
                        for index,i in enumerate(global1.objbrick):
                                if i.strength != 0:
                                        if (self.x in range(i.x - abs(self.xinc),i.x) or self.x in range(i.x + 1,i.x + abs(self.xinc) + 1)) and self.y == i.y:
                                                os.system("aplay Explosion.wav > /dev/null 2>&1 &")
                                                self.colourchange(index)
                                                self.topcollide()
                                        elif (self.y in range(i.y - abs(self.yinc),i.y) or self.y in range(i.y + 1,i.y + abs(self.yinc) + 1)) and self.x == i.x:
                                                os.system("aplay Explosion.wav > /dev/null 2>&1 &")
                                                self.colourchange(index)
                                                self.sidecollide()
                                        elif (self.yinc > 0) and (self.xinc > 0) and (self.y in range(i.y - self.yinc,i.y) and self.x in range(i.x - self.xinc,i.x)):
                                                os.system("aplay Explosion.wav > /dev/null 2>&1 &")
                                                self.colourchange(index) 
                                                self.retcollide()
                                        elif (self.yinc > 0) and (self.xinc < 0) and (self.y in range(i.y - self.yinc,i.y) and self.x in range(i.x + 1,i.x + self.xinc + 1)):
                                                os.system("aplay Explosion.wav > /dev/null 2>&1 &")
                                                self.colourchange(index)
                                                self.retcollide()
                                        elif (self.xinc > 0) and (self.yinc < 0)and (self.y in range(i.y + 1,i.y + abs(self.yinc) + 1) and self.x in range(i.x - abs(self.xinc),i.x)):
                                                os.system("aplay Explosion.wav > /dev/null 2>&1 &")
                                                self.colourchange(index)
                                                self.retcollide()
                                        elif (self.xinc<0) and (self.yinc<0) and (self.y in range (i.y + 1,i.y + abs(self.yinc) + 1) and self.x in range(i.x + 1,i.x + abs(self.xinc) + 1) ):
                                                os.system("aplay Explosion.wav > /dev/null 2>&1 &")
                                                self.colourchange(index)
                                                self.retcollide()                                                          
                        if self.x in range(global1.objpaddle.x - abs(self.xinc),global1.objpaddle.x) and ( self.y in range(global1.objpaddle.y, global1.objpaddle.y + global1.paddlelength)):
                                screen1 = [[0]*120]*40
                                screen1 = numpy.array(screen1)
                                for i in range(0,40):
                                                for j in range(0,120):
                                                        screen1[i][j] = global1.screen[i][j]
                                if global1.decrease == 1:
                                        for i in range(0,40):
                                                for j in range(0,120):
                                                        if global1.screen[i][j] == -1 or global1.screen[i][j] == 1 or global1.screen[i][j] == 2 or global1.screen[i][j] == 3:
                                                               if i != 38:
                                                                        global1.screen[i+1][j] = screen1[i][j]
                                                               else:
                                                                        global1.flag = 1                                        
                                                                
                                        for i in range(0,40):
                                                for j in range(0,120):
                                                         if screen1[i][j] == -1 or screen1[i][j] == 1 or screen1[i][j] == 2 or screen1[i][j] == 3:
                                                                 global1.screen[i][j] = 0

                                        for i in global1.objbrick:
                                                i.x = i.x + 1
                                                i.y = i.y                                  

                                if self.grab == 1:
                                        global1.relball = 0
                                        self.yinc = -1
                                        self.xinc = -1
                                else:        
                                        self.paddlecollide(0)
                        elif self.x in range(global1.objpaddle.x - abs(self.xinc),global1.objpaddle.x + 1) and ((self.y + self.yinc) in range(global1.objpaddle.y, global1.objpaddle.y + global1.paddlelength)):
                                if self.grab == 1:
                                        global1.relball = 0
                                        self.yinc = -1
                                        self.xinc = -1
                                else:        
                                        self.paddlecollide(self.yinc)                
                        elif self.x in range(global1.objpaddle.x - abs(self.xinc),global1.objpaddle.x +1):
                                self.deploy = 0
                                self.xinc = 0
                                self.yinc = 0            
