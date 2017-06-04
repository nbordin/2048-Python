from random import randint
from numpy import zeros, array, apply_along_axis, nonzero, append, array_equal, copy
from math import log

class gameMatrix:
    
    m = None
    gameOver = False
    
    def __init__(t):
        t.startGame()
   
    # game initialisation
   
    def addTwo(t):
        while (True):
            x, y = randint(0,3), randint(0,3)
            if t.m[x][y] == 0:
                t.m[x][y] = 2
                break
        
    def startGame(t):
        t.m = zeros((4,4))
        t.addTwo()
        t.addTwo()
    
    # check if the game is not over
    
    def hasEqualNeighbours(t):
        for i in range(4):
            for j in range(4):
                neighbours = [y for y in [(i,j+1), (i,j-1), (i+1,j), (i-1,j)] if y[0] <=3 and y[0] >= 0 and y[1] <=3 and y[1] >= 0]
                for n in neighbours:
                    if t.m[i][j] == t.m[n[0]][n[1]]: return True
        return False
                
    def hasPossibilities(t):
        if len(t.m[t.m == 0]) >= 1:
            return True
        return t.hasEqualNeighbours()
    
    # movements
    
    def cleanRows(t, dir):
        for i, row in enumerate(t.m):
            nz = row[row > 0]
            t.m[i,:] = append(nz, (4-len(nz))*[0]) if dir == 'l' else append((4-len(nz))*[0],nz)
            
    def horizontalMovement(t, dir):
        while(True):
            for i in range(3):
                colLeft = [int(pow(2,log(x,2)+1)) if (x == y and x != 0 and y != 0) else x for x,y in zip(t.m[:,i],t.m[:,i+1])]
                colRight = [0 if (x == y) else y for x,y in zip(t.m[:,i],t.m[:,i+1])]
                t.m[:,i], t.m[:,i+1]= colLeft, colRight
            mm = copy(t.m)
            t.cleanRows(dir)
            if array_equal(mm,t.m):
                break
    
    def moveRight(t):
        t.horizontalMovement('r')
        t.gameOver = not (t.hasPossibilities())
        if not t.gameOver: t.addTwo()
        
    def moveLeft(t):
        t.horizontalMovement('l')
        t.gameOver = not (t.hasPossibilities())
        if not t.gameOver: t.addTwo()
    
    def cleanColumns(t, dir):
        for i, col in enumerate(t.m.T):
            nz = col[col > 0]
            t.m.T[i,:] = append(nz, (4-len(nz))*[0]) if dir == 'u' else append((4-len(nz))*[0],nz)

    def verticalMovement(t,dir):
        while (True):
            for i in range(3):
                rowUp = [int(pow(2,log(x,2)+1)) if (x == y and x != 0 and y != 0) else x for x,y in zip(t.m[i,:],t.m[i+1,:])]
                rowDown = [0 if (x == y) else y for x,y in zip(t.m[i,:],t.m[i+1,:])]
                t.m[i,:], t.m[i+1,:]= rowUp, rowDown
            mm = copy(t.m)
            t.cleanColumns(dir)
            if array_equal(mm,t.m):
                break
            
    def moveUp(t):
        t.verticalMovement('u')
        t.gameOver = not (t.hasPossibilities())
        if not t.gameOver: t.addTwo()
        
    def moveDown(t):
        t.verticalMovement('d')
        t.gameOver = not (t.hasPossibilities())
        if not t.gameOver: t.addTwo()
        
        
        
        