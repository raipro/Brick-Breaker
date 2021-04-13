import global1

class brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.contact = 1
        self.defense = 0

class brick1(brick):
    def __init__(self,x,y):
        self.strength = 1
        super().__init__(x,y)  

class brick2(brick):
    def __init__(self,x,y):
        self.strength = 2
        super().__init__(x,y)  
        
class brick3(brick):
    def __init__(self,x,y):
        self.strength = 3
        super().__init__(x,y)   
    
class ubrick(brick):
    def __init__(self,x,y):
        self.strength = -1 
        super().__init__(x,y)

class rbrick(brick):
    def __init__(self,x,y):
        self.strength = 3 
        super().__init__(x,y)