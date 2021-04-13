import global1
import function 
class bomb:
        def __init__(self, x, y):
                self.x = x
                self.y = y
                self.xinc = 1
                self.yinc = 0
                self.deploy = 1

        def collide(self):
                  for i in global1.objbrick:
                      if i.x == self.x and i.y == self.y:
                          self.x = self.x + self.xinc
                          self.y = self.y + self.yinc

                  if self.x == global1.objpaddle.x - 1 and (self.y in range(global1.objpaddle.y, global1.objpaddle.y + global1.paddlelength)):
                                self.deploy = 0
                                self.xinc = 0
                                self.yinc = 0
                                global1.lives = global1.lives - 1
                                if global1.lives == 0:
                                    global1.flag = 1
                                global1.newlife = 1
                                function.reset(global1.newlife)
                                global1.newlife = 0              
                  
                  elif self.x == global1.objpaddle.x - 1:
                                self.deploy = 0
                                self.xinc = 0
                                self.yinc = 0                                

