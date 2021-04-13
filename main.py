import function
import global1
from bricks import *
from input import *
from startscreen import startscreen
from colorama import Fore, Back, Style
import time
from bomb import *
starttime = time.time()
# if __name == '__main__':
      
startscreen()

counter1 = 0
flag1 = 0
flag2 = 0
while(global1.flag==0):
    function.clrscr()
    function.update_board(starttime)
    function.move()

    if global1.level == 3:
        counter1 = counter1 + 1
        if counter1 % 30 == 0:
            global1.objbombs.append(bomb(2,global1.objboss.y + 2))
            global1.screen[2][global1.objboss.y+2] = 15
        if global1.health <= 2 and flag1==0:
            flag1 = 1 
            global1.objbrick.append(brick1(3,global1.objboss.y - 2))
            global1.objbrick.append(brick2(3,global1.objboss.y))
            global1.objbrick.append(brick2(3,global1.objboss.y + 2))
            global1.objbrick.append(brick3(3,global1.objboss.y + 4))
            global1.objbrick.append(brick1(3,global1.objboss.y + 6))
            global1.screen[3][global1.objboss.y - 2] = 1
            global1.screen[3][global1.objboss.y] = 2
            global1.screen[3][global1.objboss.y + 2] = 2
            global1.screen[3][global1.objboss.y + 4] = 3
            global1.screen[3][global1.objboss.y + 6] = 1
            for i in global1.objbrick:
                i.defense = 1

        elif global1.health <= 4 and flag2==0:
            flag2 = 1
            global1.objbrick.append(brick1(3,global1.objboss.y - 2))
            global1.objbrick.append(brick2(3,global1.objboss.y))
            global1.objbrick.append(brick2(3,global1.objboss.y + 2))
            global1.objbrick.append(brick3(3,global1.objboss.y + 4))
            global1.objbrick.append(brick1(3,global1.objboss.y + 6))
            global1.screen[3][global1.objboss.y - 2] = 1
            global1.screen[3][global1.objboss.y] = 2
            global1.screen[3][global1.objboss.y + 2] = 2
            global1.screen[3][global1.objboss.y + 4] = 3
            global1.screen[3][global1.objboss.y + 6] = 1
            for i in global1.objbrick:
                i.defense = 1


    for i in global1.objexppaddle:
        function.handle_powerup(i,6)
    for i in global1.objshrpaddle:
        function.handle_powerup(i,7)
    for i in global1.objfastball:
        function.handle_powerup(i,8)
    for i in global1.objthruball:
        function.handle_powerup(i,9)
    for i in global1.objpaddlegrab:
        function.handle_powerup(i,10)
    for i in global1.objballmultiply:
        function.handle_powerup(i,11)
    for i in global1.objshoot:
        function.handle_powerup(i,12)

    for i in global1.objbullet:
            if i.deploy == 1:
                global1.screen[i.x][i.y] = 0
                i.x = i.x + i.xinc
                i.collide()
                if i.deploy == 1:
                    global1.screen[i.x][i.y] = 13

    for i in global1.objbombs:
            if i.deploy == 1:
                global1.screen[i.x][i.y] = 0
                i.x = i.x + i.xinc
                i.collide()
                if i.deploy == 1:
                    global1.screen[i.x][i.y] = 15
    if global1.lives == 0:
        break                    

    if global1.relball == 0:    
        global1.screen[global1.objball[0].x][global1.objball[0].y] = 0
        global1.objball[0].x = global1.objpaddle.x - 1
        global1.objball[0].y = global1.objpaddle.y 
        global1.screen[global1.objball[0].x][global1.objball[0].y] = 5
    else:
        check = 0
        for i in global1.objball:  
            if i.deploy == 1:
                global1.screen[i.x][i.y] = 0 
                i.x = i.x + i.xinc
                i.y = i.y + i.yinc
                for j in global1.objbrick:
                    if i.x == j.x and i.y == j.y:
                         i.x = i.x + i.xinc
                         i.y = i.y + i.yinc
                i.collide()
                if i.deploy == 1:
                    global1.screen[i.x][i.y] = 5
                    check = 1
        if global1.health == 0:
            break
        if check == 0:
            global1.lives = global1.lives - 1
            if global1.lives == 0:
                break
            global1.newlife = 1
            function.reset(global1.newlife)
            global1.newlife = 0 
            # global1.objball[0].deploy = 1
            # global1.relball = 0
            # global1.objball[0].x = global1.objpaddle.x - 1
            # global1.objball[0].y = global1.objpaddle.y         

print("Game Over")
print("Final Score:" + str(global1.score))


