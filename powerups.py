import global1
# from ball import ball1
class powerup:
    def __init__(self, x, y, xinc,yinc,state=1):
        self.x = x
        self.y = y
        self.xinc = xinc
        self.yinc = yinc
        self.state = state
        self.creatt = 0
        self.applicable = 0
        self.counter = 0

    def sidecollide(self):
        # self.xinc = -self.xinc
                self.yinc = -self.yinc

    def topcollide(self):
                self.xinc = -self.xinc

    def retcollide(self):
                self.yinc = -self.yinc
                self.xinc = -self.xinc

    def dec(self):
        self.x = self.x + self.xinc
        self.y = self.y + self.yinc
        for i in global1.objbrick:
            if self.x == i.x and self.y == i.y:
                self.x = self.x + self.xinc
                self.y = self.y + self.yinc    

    def collide(self):
                if self.xinc < 0 and self.yinc < 0 and (self.y * self.y + self.x * self.x < self.yinc * self.yinc + self.xinc * self.xinc):
                        self.retcollide()         
                elif self.y in range(0, abs(self.yinc)) or (self.y in range(119 - abs(self.yinc), 119)):
                        self.sidecollide()
                elif self.x in range(1,abs(self.xinc) + 1):
                        self.topcollide()    

class expandpaddle(powerup):
    def __init__(self,x,y, xinc,yinc,state):
        super().__init__(x,y, xinc,yinc,state)

    def change(self):
        if shoot==0:   
            global1.paddlelength = global1.paddlelength + 2
            global1.paddle = global1.paddle + "^^"
        else:
            global1.paddlelength = global1.paddlelength + 2
            str1 = ''
            str1 = str1 + 'i'
            for i in range(0,global1.paddlelength - 2):
                str1 = str1 + '^'    
            str1 = str1 + 'i'
            global1.paddle = str1
        
    def revert(self):
        self.creatt = 0
        if shoot==1:         
            global1.paddlelength = global1.paddlelength - 2
            str1 = ''
            str1 = str1 + 'i'
            for i in range(0,global1.paddlelength - 2):
                str1 = str1 + '^'    
            str1 = str1 + 'i'
            global1.paddle = str1
        else:
            global1.paddlelength = global1.paddlelength - 2
            global1.paddle = global1.paddle[:global1.paddlelength - 2]   


class shrinkpaddle(powerup):
    def __init__(self,x,y, xinc,yinc,state):
        super().__init__(x,y, xinc,yinc,state)
    def change(self):
        if shoot == 0:
            global1.paddle = global1.paddle[:global1.paddlelength - 2]
            global1.paddlelength = global1.paddlelength - 2
        else:
             global1.paddlelength = global1.paddlelength - 2
             str1 = ''
             str1 = str1 + 'i'
             for i in range(0,global1.paddlelength - 2):
                str1 = str1 + '^'    
             str1 = str1 + 'i'
             global1.paddle = str1   

    def revert(self):
        self.creatt = 0
        if shoot == 0:
            global1.paddlelength = global1.paddlelength + 2
            global1.paddle = global1.paddle + "^^"
        else:
            global1.paddlelength = global1.paddlelength + 2
            str1 = ''
            str1 = str1 + 'i'
            for i in range(0,global1.paddlelength - 2):
                str1 = str1 + '^'    
            str1 = str1 + 'i'
            global1.paddle = str1      

 
class fastball(powerup):
    def __init__(self,x,y, xinc,yinc,state):
        super().__init__(x,y, xinc,yinc,state)

    def change(self):
        for i in global1.objball:
            if i.deploy == 1:    
                i.yinc = i.yinc * 2
                i.xinc = i.xinc * 2

    def revert(self):
        self.creatt = 0
        for i in global1.objball:
            if i.deploy == 1:
                i.yinc = i.yinc // 2
                i.xinc = i.xinc // 2

class thruball(powerup):
    def __init__(self,x,y, xinc,yinc,state):
        super().__init__(x,y, xinc,yinc,state)

    def change(self):
        for i in global1.objball:
            if i.deploy == 1:
                i.power = 1

    def revert(self):
        self.creatt = 0
        for i in global1.objball:
            if i.deploy == 1:
                i.power = 0

class paddlegrab(powerup):
    def __init__(self,x,y, xinc,yinc,state):
        super().__init__(x,y, xinc,yinc,state)

    def change(self):
        for i in global1.objball:
            if i.deploy == 1:    
                i.grab = 1

    def revert(self):
        self.creatt = 0
        for i in global1.objball:
            if i.deploy == 1:
                i.grab = 0


class balls(powerup):
    def __init__(self,x,y, xinc,yinc,state):
        super().__init__(x,y, xinc,yinc,state)

class shoot(powerup):
    def __init__(self,x,y, xinc,yinc,state):
        super().__init__(x,y, xinc,yinc,state)

    def change(self):
        str1 = ''
        str1 = str1 + 'i'
        for i in range(0,global1.paddlelength - 2):
            str1 = str1 + '^'    
        str1 = str1 + 'i'
        global1.paddle = str1
        global1.shoot = 1

    def revert(self):
        str1 = ''
        for i in range(0,global1.paddlelength):
            str1 = str1 + '^'
        global1.paddle =  str1
        global1.shoot = 0    

   

    
            