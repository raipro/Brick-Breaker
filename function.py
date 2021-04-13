import os
import global1
from input import *
from colorama import Fore, Back, Style
import time
from powerups import *
from startscreen import * 
from ball import ball1
from bullet import *
def clrscr():
    os.system('clear')

def reset(a):
    global1.paddle = "^^^^^^"
    global1.flag = 0
    global1.paddlelength = 6
    global1.shoot = 0
    global1.timepowerup = 0
    global1.objballmultiply.clear()  
    global1.objball.clear()
    global1.objshoot.clear()
    global1.objbullet.clear()
    global1.objexppaddle.clear()
    global1.objshrpaddle.clear()
    global1.objthruball.clear()
    global1.objfastball.clear()
    global1.objpaddlegrab.clear()
    if a==0:
        global1.objbrick.clear()
        global1.tilvl = 0
        global1.relball = 0
        for i in range(0, 40):
            for j in range(0, 120):
                global1.screen[i][j] = 0
        if global1.level == 2:
            level2()
        if global1.level == 3:
            level3()    
        if global1.level == 4:
            global1.objball.append(ball1(39,63))
            global1.flag = 1

    elif a==1:
        global1.objball.append(ball1(global1.objpaddle.x - 1,global1.objpaddle.y))
        global1.relball = 0  
        for i in range(0, 40):
            for j in range(0, 120):
                if not(global1.screen[i][j] == -1 or global1.screen[i][j] == 1 or global1.screen[i][j] == 2 or global1.screen[i][j] == 3 or global1.screen[i][j] == 4):
                    global1.screen[i][j] = 0                           

def update_board(starttime):
        timetaken = int(time.time() - starttime)
        global1.time = timetaken
        global1.tilvl = global1.time - global1.tatlvl
        if global1.tilvl >= global1.timelimitlvl:
            global1.decrease = 1 


        for i in global1.objbrick:
            if type(i).__name__ == "rbrick" and i.contact==1:
                if i.strength == 3 or i.strength == 2:
                    i.strength = i.strength - 1
                elif i.strength == -1:
                    i.strength = 3
                else:
                    i.strength = -1
                global1.screen[i.x][i.y] = i.strength 
                   
        for i in range(0, 40):
            for j in range(0, 120): 
                if i==0 and j==0:
                    print("Score:" + str(global1.score),end ='')
                elif i==0 and j==30:
                    print("Poweruptime:" + str(global1.timepowerup),end='')
                elif i==0 and j==55:
                    print("Lives:" + str(global1.lives),end='')    
                elif i==0 and j==110:
                    print("Time:" + str(timetaken),end='')
                elif i==0 and j==80 and global1.level == 3:
                    print("Health:" + str(global1.health),end='')        
                if j==119 and i!=39 and i!=0:
                    print(Fore.WHITE + "|",end='')
                elif global1.screen[i][j] == 0:
                    print(" ", end='')
                elif global1.screen[i][j] == 1:
                    print(Fore.RED + global1.brick1, end='')
                elif global1.screen[i][j] == 2:
                    print(Fore.GREEN + global1.brick1, end='')
                elif global1.screen[i][j] == 3:
                    print(Fore.BLUE + global1.brick1, end='')
                elif global1.screen[i][j] == -1:
                    print(Fore.MAGENTA + global1.brick1, end='')
                elif global1.screen[i][j] == 4:
                    print(Fore.YELLOW + global1.paddle, end='')
                elif global1.screen[i][j] == 5:
                    print(Fore.WHITE + global1.ball, end='')
                elif global1.screen[i][j] == 6:
                    print(Fore.WHITE + global1.exppaddle, end='')
                elif global1.screen[i][j] == 7:
                    print(Fore.WHITE + global1.shrpaddle, end='')
                elif global1.screen[i][j] == 8:
                    print(Fore.WHITE + global1.fastball,end='')
                elif global1.screen[i][j] == 9:
                    print(Fore.WHITE + global1.thruball,end='')
                elif global1.screen[i][j] == 10:
                    print(Fore.WHITE + global1.paddlegrab,end='')
                elif global1.screen[i][j] == 11:
                    print(Fore.WHITE + global1.ballmultiply,end='')
                elif global1.screen[i][j] == 12:
                    print(Fore.WHITE + global1.shoot1,end='')
                elif global1.screen[i][j] == 13:
                    print(Fore.WHITE + global1.bullet,end='')
                elif global1.screen[i][j] == 14:
                    print(Fore.GREEN + global1.ufo,end ='' )
                elif global1.screen[i][j] == 15:
                    print(Fore.WHITE + global1.bomb, end ='')       
            print('\n', end='')

def move():
    getch = Get()
    ch = input_to(getch)
    if ch == 'a':
        global1.screen[global1.objpaddle.x][global1.objpaddle.y] = 0
        if global1.level == 3:
            global1.screen[1][global1.objpaddle.y] = 0
        if global1.objpaddle.y >= 4:
            global1.objpaddle.y = global1.objpaddle.y - 4
            if global1.level == 3:
                global1.objboss.y = global1.objboss.y - 4
        global1.screen[global1.objpaddle.x][global1.objpaddle.y] = 4
        if global1.level == 3:
            global1.screen[1][global1.objpaddle.y] = 14
    elif ch == 'd':
        global1.screen[global1.objpaddle.x][global1.objpaddle.y] = 0
        if global1.level == 3:
            global1.screen[1][global1.objpaddle.y] = 0
        if global1.objpaddle.y <= 115 - global1.paddlelength:   
            global1.objpaddle.y = global1.objpaddle.y + 4
            if global1.level == 3:
                global1.objboss.y = global1.objboss.y + 4
        global1.screen[global1.objpaddle.x][global1.objpaddle.y] = 4
        if global1.level == 3:
            global1.screen[1][global1.objpaddle.y] = 14
    elif ch == 'q':
        global1.flag = 1    
    elif ch == ' ':
        global1.relball = 1
        global1.objball[0].xinc = -1
        global1.objball[0].yinc = -1
    elif ch == 'e':
        global1.level += 1
        global1.tatlvl = global1.time
        reset(global1.newlife)
    if ch:
        time.sleep(0.05)    


def handle_powerup(i,a):
        if i.state == 1:
                    global1.screen[i.x][i.y] = 0        
                    i.dec()
                    i.counter = i.counter + 1
                    if (i.counter)%5 == 0:
                       i.xinc = i.xinc + 1
                    i.collide()
                    if i.x in range(global1.objpaddle.x - i.xinc,global1.objpaddle.x + 1) and ( i.y in range(global1.objpaddle.y, global1.objpaddle.y + global1.paddlelength + 1) ):
                        i.state = 0
                        i.creatt = global1.time
                        i.counter = 0
                        if a==7:
                            if global1.paddlelength > 2:    
                                i.change()
                                i.applicable = 1     
                        else:
                            if a!=11:
                                i.change()
                                i.applicable = 1
                            else:
                                temp = []
                                for j in global1.objball:
                                    if j.deploy == 1:    
                                        temp.append(ball1(j.x ,j.y))
                                        temp[-1].yinc = -j.yinc
                                        temp[-1].xinc = -j.xinc
                                for j in temp:
                                        global1.objball.append(j)             
                    elif i.x in range(global1.objpaddle.x - i.xinc,global1.objpaddle.x + 1):
                        i.state = 0
                    else:    
                        global1.screen[i.x][i.y] = a
                # else:
                #     i.state = 0
                #     i.creatt = 0        
        elif i.state == 0 and i.creatt != 0:
                    i.counter = i.counter + 1
                    if a == 12:
                                if (i.counter)%30 == 0:
                                    global1.objbullet.append(bullet(global1.objpaddle.x - 1,global1.objpaddle.y, -1))
                                    global1.objbullet.append(bullet(global1.objpaddle.x - 1,global1.objpaddle.y + global1.paddlelength, -1))
                                    global1.screen[global1.objpaddle.x - 1][global1.objpaddle.y] = 13
                                    global1.screen[global1.objpaddle.x - 1][global1.objpaddle.y + global1.paddlelength] = 13               
                                global1.timepowerup = (global1.timelimit - (global1.time - i.creatt))                
                    if ((global1.time - i.creatt >= global1.timelimit)) and i.applicable == 1 and a!=11:
                        i.revert()
                        global1.timepowerup = 0
                        i.counter = 0


# def topcollide():
# def rightcollide():
# def bottomcollide():            
