from rules_2048 import gameMatrix
import tkinter as tk
import random

colors = {  0:"#9e948a", 2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", \
            32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", \
            512:"#edc850", 1024:"#edc53f", 2048:"#edc22e" }
font = ('Verdana', 25, 'bold')

class App(tk.Frame):
    gMatrix     = None
    m           = None
    gameOver    = None
    
    def __init__(t, parent=None):
        t.gMatrix = gameMatrix()
        t.m = t.gMatrix.m
        tk.Frame.__init__(t, parent)
        tk.Frame.pack(t)
        t.createGrid()
                
        t.master.bind("w", t.up)
        t.master.bind("a", t.left)
        t.master.bind("s", t.down)
        t.master.bind("d", t.right)
        
    def up(t, event):
        t.gMatrix.moveUp()
        t.m = t.gMatrix.m
        t.updateGrid()
    
    def down(t, event):
        t.gMatrix.moveDown()
        t.m = t.gMatrix.m
        t.updateGrid()
    
    def left(t, event):
        t.gMatrix.moveLeft()
        t.m = t.gMatrix.m
        t.updateGrid()
    
    def right(t, event):
        t.gMatrix.moveRight()
        t.m = t.gMatrix.m
        t.updateGrid()
        
    def createGrid(t):
        t.canvas = tk.Canvas(t, width=400, height=400, borderwidth=0, highlightthickness=0)
        t.canvas.pack(side="top", fill="both", expand="true")
        t.rows = 100
        t.columns = 100
        t.cellwidth = 100
        t.cellheight = 100

        t.rect = {}
        t.text = {}
        for column in range(4):
            for row in range(4):
                x1 = column*t.cellwidth
                y1 = row * t.cellheight
                x2 = x1 + t.cellwidth
                y2 = y1 + t.cellheight
                x_text, y_text = 50+column*100, 50+row*100
                n = int(t.m[row, column])
                t.rect[row,column] = t.canvas.create_rectangle(x1,y1,x2,y2, fill=colors[n], tags="rect"+str(row)+str(column), outline='#776e65', width=5)
                tx = str(n) if t.m[row, column] > 0 else ''
                t.text[row,column] = t.canvas.create_text((x_text, y_text), text=tx, tags="text"+str(row)+str(column), font=font, fill='#ffffff' if n > 4 else "#776e65")
        
    def updateGrid(t):
        t.gameOver = t.gMatrix.gameOver
        if t.gameOver:
            print('Game Over!')
        for i in range(4):
            for j in range(4):
                t.canvas.itemconfig("rect"+str(i)+str(j), fill=colors[t.m[i,j]])
                n = int(t.m[i, j])
                tx = str(n) if t.m[i, j] > 0 else ''
                t.canvas.itemconfig("text"+str(i)+str(j), text=tx, fill='#ffffff' if n > 4 else "#776e65")
        

if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title('2048')
    app = App(root)
    app.mainloop()