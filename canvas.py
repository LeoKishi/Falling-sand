import tkinter as tk


class Canvas():
    def __init__(self, height: int = 10, width: int = 8):
        '''
        Create a grid of specified height and width.\n
        Default size is 10x8.
        '''
        self.root = tk.Tk()
        self.root.resizable(0,0)
        self.height = height
        self.width = width
        self.array = [[0 for row in range(width)] for col in range(height)]
        self.frames = [[0 for row in range(width)] for col in range(height)]
        for row in range(height):
            for col in range(width):
                self.frames[row][col] = tk.Frame(self.root, 
                                       height=20, 
                                       width=20, 
                                       borderwidth=1,
                                       relief=tk.FLAT)
                self.frames[row][col].grid(row=row, column=col)
                self.frames[row][col].bind('<Button-1>', lambda event, x=row, y=col: self.draw(x,y))
                self.frames[row][col].bind('<Button-3>', lambda event, x=row, y=col: self.erase(x,y))
        self.root.bind('<space>', lambda event: self.clear())

    def clear(self):
        '''Erase everything on canvas'''
        self.array = [[0 for row in range(self.width)] for col in range(self.height)]
        self.update_canvas()
    
    def update_canvas(self):
        '''
        Draws and erases pixels on the canvas.\n
        Draws if the correspondent index on the array is 1 and erases if 0.
        '''
        for x in range(self.height):
            for y in range(self.width):
                if self.array[x][y] == 0:
                    # bg
                    self.frames[x][y]['bg'] = 'SystemButtonFace'
                else:
                    # sand
                    self.frames[x][y]['bg'] = 'Black'

    def draw(self, x, y):
        '''Draws a pixel on the clicked spot'''
        self.array[x][y] = 1
        self.frames[x][y]['bg'] = 'Black'

    def erase(self, x, y):
        '''Erases a pixel on the clicked spot'''
        self.array[x][y] = 0
        self.frames[x][y]['bg'] = 'SystemButtonFace'