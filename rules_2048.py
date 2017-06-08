from random import randint
from numpy import zeros, array, append, flip
from math import log

class gameMatrix:
    
    m = None
    gameOver = False
    
    def __init__(t):
        t.startGame()
   
    # game initialisation
   
    def addTwo(t):
        if len(t.m[t.m == 0]) > 0:
            while (True):
                x, y = randint(0,3), randint(0,3)
                if t.m[x][y] == 0:
                    t.m[x][y] = 2
                    break
        
    def startGame(t):
        t.m = zeros((4,4))
        t.addTwo()
        t.addTwo()
    
    # check if the game is over
    
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
    
    def moveLeft(t, b=False):
        m = flip(t.m,1) if b else t.m

        for i in range(4):
            col = m[i, :][m[i, :]> 0]
            l = len(col)
            if l > 1:
                tmp_col = array([])
                for cell in range(0,l-1):
                    if col[cell] == col[cell+1]:
                        tmp_col = append(tmp_col, [int(pow(2,log(col[cell],2)+1))]) 
                        col[cell+1] = 0 
                    elif col[cell] == 0: 
                        pass
                    else:
                        tmp_col = append(tmp_col, col[cell])
                tmp_col = append(tmp_col, col[len(col)-1])
            elif l == 1: tmp_col = [col[0]]
            else: tmp_col = array([])
            t.m[i,:] = flip(append(tmp_col, [0]*(4-len(tmp_col))),0) if b else append(tmp_col, [0]*(4-len(tmp_col)))
        t.gameOver = not (t.hasPossibilities())
        if not t.gameOver: t.addTwo()
        
    def moveRight(t):
        t.moveLeft(True)
    

    def moveUp(t, b=False):
        m = flip(t.m,0) if b else t.m

        for i in range(4):
            col = m[:, i][m[:, i]> 0]
            l = len(col)
            if l > 1:
                tmp_col = array([])
                for cell in range(0,l-1):
                    if col[cell] == col[cell+1]:
                        tmp_col = append(tmp_col, [int(pow(2,log(col[cell],2)+1))]) 
                        col[cell+1] = 0 
                    elif col[cell] == 0: 
                        pass
                    else:
                        tmp_col = append(tmp_col, col[cell])
                tmp_col = append(tmp_col, col[len(col)-1])
            elif l == 1: tmp_col = [col[0]]
            else: tmp_col = array([])
            t.m[:,i] = flip(append(tmp_col, [0]*(4-len(tmp_col))),0) if b else append(tmp_col, [0]*(4-len(tmp_col)))
        t.gameOver = not (t.hasPossibilities())
        if not t.gameOver: t.addTwo()
        
    def moveDown(t):
        t.moveUp(True)
        
        
        
        
        