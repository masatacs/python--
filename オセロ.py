from msvcrt import getch
import os

field = [
    [2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2],
    [2,2,2,0,1,2,2,2],
    [2,2,2,1,0,2,2,2],
    [2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2],
]

direction = [
    [-1,-1],
    [-1,0],
    [-1,1],
    [0,-1],
    [0,0],
    [0,1],
    [1,-1],
    [1,0],
    [1,1]
]

colt = [
    "● ","○ ","・"
]

color = [
    "white turn","black turn"
]

def allChack( arrSize, turn ):
    for i in range( arrSize ):
        for n in range( arrSize ):
            if chackCanPut( False, turn, n, i ):
                return True

    return False


def draw( arrSize, playerx, playery, turn ):
	os.system( "cls" )
	for i in range( arrSize ):
		for n in range( arrSize ):
			if i == playery and n == playerx:
				print( "◎ ", end="" )
				continue
				
			print( colt[field[i][n]], end="" )
			
		print( "" )
		
	print( color[turn] )

def chackCanPut( put, turn, playerx, playery ):
    if field[playery][playerx] != 2:
        return False

    nturn = turn ^ 1

    for i in range( 9 ):
        dx = playerx
        dy = playery

        dx += direction[i][1]
        dy += direction[i][0]

        if dx < 0 or dy < 0 or dx >= 8 or dy >= 8:
            continue

        if field[dy][dx] == nturn:
            while True:
                dx += direction[i][1]
                dy += direction[i][0]

                if dx < 0 or dy < 0 or dx >= 8 or dy >= 8:
                    break
            
                if field[dy][dx] == 2:
                    break

                if field[dy][dx] == turn:
                    if not put:
                        return True

                    x2 = playerx
                    y2 = playery

                    while True:
                        x2 += direction[i][1]
                        y2 += direction[i][0]

                        field[y2][x2] = turn

                        if x2 == dx and y2 == dy:
                            break

                    break

    return False
        

def loop():
    passturn = False
    playerx = 0
    playery = 0
    turn = 0

    while True:
        draw( 8, playerx, playery, turn )

        if not allChack( 8, 1 ) and not allChack( 8, 0 ):
            print( "Game Set" )
            break        

        key = ord( getch() )

        if key == 224:
            key = ord( getch() )

            if key == 77:   playerx += 1   #右
            if key == 72:   playery -= 1   #上
            if key == 75:   playerx -= 1   #左
            if key == 80:   playery += 1   #下

            continue

        if key == 13:
            if chackCanPut( False, turn, playerx, playery ) or passturn:
                chackCanPut( True, turn, playerx, playery )

                field[playery][playerx] = turn
                turn ^= 1

                passturn = False

                if not allChack( 8, turn ):
                    passturn = True

                continue

            else:
                print( "can put" )
                continue
            
        break

loop()
