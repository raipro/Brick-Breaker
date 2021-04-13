from bricks import *
import global1
from paddle import *
from ball import *
from boss import *

def startscreen():
    global1.screen[19][49] = 2
    global1.screen[17][40] = 1 
    global1.screen[17][50] = -1
    global1.screen[16][43] = 1
    global1.screen[19][54] = 3
    global1.screen[18][45] = 3
    global1.screen[10][30] = 2
    global1.screen[11][35] = 2
    global1.screen[12][45] = 2

    global1.screen[20][40] = 3
    global1.screen[20][45] = 1
    global1.screen[20][50] = 2
    global1.screen[20][55] = 3
    global1.screen[20][60] = 1
    global1.screen[20][65] = -1
    global1.screen[20][70] = 3

    global1.screen[21][49] = 1
    global1.screen[22][54] = 3
    global1.screen[23][58] = 2
    global1.screen[24][43] = 2
    global1.screen[21][39] = 2
    global1.screen[22][25] = 3
    global1.screen[23][30] = 3
    global1.screen[24][50] = 1
    global1.screen[25][55] = -1
    global1.screen[25][65] = -1

    global1.screen[38][63] = 5
    global1.screen[39][63] = 4

    global1.screen[21][30] = 3
    global1.screen[19][30] = 3

    global1.objbrick.append(brick2(19,49))
    global1.objbrick.append(brick1(17,40))
    global1.objbrick.append(ubrick(17,50))
    global1.objbrick.append(brick1(16,43))
    global1.objbrick.append(brick3(19,54))
    global1.objbrick.append(brick3(18,45))
    global1.objbrick.append(brick2(10,30))
    global1.objbrick.append(brick2(11,35))
    global1.objbrick.append(brick2(12,45))

    global1.objbrick.append(brick3(20,40))
    global1.objbrick.append(brick1(20,45))
    global1.objbrick.append(brick2(20,50))
    global1.objbrick.append(brick3(20,55))
    global1.objbrick.append(brick1(20,60))
    global1.objbrick.append(ubrick(20,65))
    global1.objbrick.append(brick3(20,70))

    global1.objbrick.append(brick1(21,49))
    global1.objbrick.append(brick3(22,54))
    global1.objbrick.append(brick2(23,58))
    global1.objbrick.append(brick2(24,43))
    global1.objbrick.append(brick2(21,39))
    global1.objbrick.append(brick3(22,25))
    global1.objbrick.append(brick3(23,30))
    global1.objbrick.append(brick1(24,50))
    global1.objbrick.append(ubrick(25,55))
    global1.objbrick.append(ubrick(25,65))
    global1.objbrick.append(rbrick(21,30))
    global1.objbrick.append(rbrick(19,30))

    global1.objpaddle = paddle1(39,63)
    global1.objball.append(ball1(38,63))

    
def level2():
    global1.screen[25][40] = 2
    global1.screen[25][35] = 1 
    global1.screen[25][45] = -1
    global1.screen[27][40] = 1
    global1.screen[28][54] = -1
    global1.screen[26][45] = 3
    global1.screen[26][30] = 2
    global1.screen[20][35] = 2
    global1.screen[22][45] = 2

    global1.screen[21][40] = 3
    global1.screen[19][45] = 1
    global1.screen[24][50] = -1
    global1.screen[24][55] = 3
    global1.screen[24][60] = 1
    global1.screen[24][65] = -1
    global1.screen[24][70] = 3

    global1.screen[19][49] = -1
    global1.screen[22][54] = 3
    global1.screen[22][58] = 2
    global1.screen[22][43] = 2
    global1.screen[22][39] = 2
    global1.screen[22][25] = 3
    global1.screen[29][30] = 3
    global1.screen[29][50] = 1
    global1.screen[29][55] = -1
    global1.screen[29][65] = -1
    global1.screen[21][30] = 3
    global1.screen[19][30] = 3

    global1.screen[38][63] = 5
    global1.screen[39][63] = 4

    global1.objbrick.append(brick2(25, 40))
    global1.objbrick.append(brick1(25, 35))
    global1.objbrick.append(ubrick(25, 45))
    global1.objbrick.append(brick1(27, 40))
    global1.objbrick.append(ubrick(28,54))
    global1.objbrick.append(brick3(26,45))
    global1.objbrick.append(brick2(26,30))
    global1.objbrick.append(brick2(20,35))
    global1.objbrick.append(brick2(22,45))

    global1.objbrick.append(brick3(21,40))
    global1.objbrick.append(brick1(19,45))
    global1.objbrick.append(ubrick(24,50))
    global1.objbrick.append(brick3(24,55))
    global1.objbrick.append(brick1(24,60))
    global1.objbrick.append(ubrick(24,65))
    global1.objbrick.append(brick3(24,70))

    global1.objbrick.append(ubrick(19,49))
    global1.objbrick.append(brick3(22,54))
    global1.objbrick.append(brick2(22,58))
    global1.objbrick.append(brick2(22,43))
    global1.objbrick.append(brick2(22,39))
    global1.objbrick.append(brick3(22,25))
    global1.objbrick.append(brick3(29,30))
    global1.objbrick.append(brick1(29,50))
    global1.objbrick.append(ubrick(29,55))
    global1.objbrick.append(ubrick(29,65))
    global1.objbrick.append(rbrick(21,30))
    global1.objbrick.append(rbrick(19,30))

    global1.objpaddle.x = 39
    global1.objpaddle.y = 63
    global1.objball.append(ball1(38,63))

def level3():
    global1.objboss = boss(1,63)
    global1.objpaddle.x = 39
    global1.objpaddle.y = 63
    global1.objball.append(ball1(38,63))
    global1.objbrick.append(ubrick(5,59))
    global1.objbrick.append(ubrick(7,61))
    global1.objbrick.append(ubrick(9,63))
    global1.objbrick.append(ubrick(7,65))
    global1.objbrick.append(ubrick(5,67))
    global1.objbrick.append(ubrick(10,40))
    global1.objbrick.append(ubrick(13,45))
    global1.objbrick.append(ubrick(17,50))
    global1.objbrick.append(ubrick(15,45))
    global1.objbrick.append(ubrick(10,86))
    global1.objbrick.append(ubrick(13,91))
    global1.objbrick.append(ubrick(17,96))
    global1.objbrick.append(ubrick(15,91))


    global1.screen[1][63] = 14
    global1.screen[38][63] = 5
    global1.screen[39][63] = 4

    global1.screen[5][59] = -1
    global1.screen[7][61] = -1
    global1.screen[9][63] = -1
    global1.screen[7][65] = -1
    global1.screen[5][67] = -1
    global1.screen[10][40] = -1
    global1.screen[13][45] = -1
    global1.screen[17][50] = -1
    global1.screen[15][45] = -1
    global1.screen[10][86] = -1
    global1.screen[13][91] = -1
    global1.screen[17][96] = -1
    global1.screen[15][91] = -1

   # print(global1.screen)
    # global1.objbrick.append(component)