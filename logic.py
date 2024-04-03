class Logic():
    def get_pixels(self, array: list[int]) -> list[tuple]:
        '''Returns a list of tuples with the position of every pixel in the canvas.'''
        height = len(array[0])
        width = len(array)
        pixels = [(x,y) for x in range(width) for y in range(height) if array[x][y] == 1]
        return pixels

    def under_is_empty(self, array: list[int], pos: tuple) -> bool:
        '''Returns True if the position under the pixel is empty, else returns False.'''
        x, y = pos[0], pos[1]
        if x+1 < len(array) and array[x+1][y] == 0:
            return True
        else:
            return False

    def right_is_empty(self, array: list[int], pos: tuple) -> bool:
        '''Returns True if the position under the pixel is occupied and there is an empty spot to the right, else returns False.'''
        x, y = pos[0], pos[1]
        if x+1 < len(array) and y+1 < len(array[0]) and array[x+1][y+1] == 0:
            return True
        else:
            return False

    def left_is_empty(self, array: list[int], pos: tuple) -> bool:
        '''Returns True if the position under the pixel is occupied and there is an empty spot to the left, else returns False.'''
        x, y = pos[0], pos[1]
        if x+1 < len(array) and y-1 >= 0 and array[x+1][y-1] == 0:
            return True
        else:
            return False

    def move_pixel(self, array: list[int], pos: tuple, direction: str = 'down'):
        '''Registers the new position and erases the previous position in the array.'''
        x, y = pos[0], pos[1]
        array[x][y] = 0
        if direction == 'down':
            array[x+1][y] = 1
        elif direction == 'right':
            array[x+1][y+1] = 1
        elif direction == 'left':
            array[x+1][y-1] = 1

    def next_frame(self, array: list[int]):
        '''Generates and registers the next frame in the array'''
        pixels = self.get_pixels(array)
        for pos in pixels:
            if self.under_is_empty(array, pos):
                self.move_pixel(array, pos)
                continue
            if self.right_is_empty(array, pos):
                self.move_pixel(array, pos, direction='right')
                continue
            if self.left_is_empty(array, pos):
                self.move_pixel(array, pos, direction='left')