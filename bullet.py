
import global1
import random
from powerups import *
class bullet:
        def __init__(self, x, y, xinc):
                self.x = x
                self.y = y
                self.xinc = -1
                self.yinc = 0
                self.deploy = 1

        def colourchange(self,index):
                        if type(global1.objbrick[index]).__name__ == "rbrick":
                                global1.objbrick[index].contact = 0      
                        if global1.objbrick[index].strength != -1 and global1.objbrick[index].strength != 0:    
                                global1.objbrick[index].strength = global1.objbrick[index].strength - 1
                                if global1.objbrick[index].strength == 0 and global1.objbrick[index].defense == 0:
                                        global1.score = global1.score + 1
                                        seq = [6,7,8,9,10,11,12]
                                        seq1 = [12]
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
            for index,i in enumerate(global1.objbrick):
                if i.x + 1 == self.x and (i.y == self.y or i.y + 1 == self.y):
                    self.colourchange(index)
                    self.deploy = 0
                elif self.x == 1:
                    self.deploy = 0