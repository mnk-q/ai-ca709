import random
class Board:
    def __init__(self, random_value = True):
        self.board = self.generate_board(random_value)
        
    def generate_board(self,random_value, size = (3, 3)):
        board = []
        nums = [str(i) for i in range(1, size[0]*size[1])]
        nums.append(' ')
        if random_value:
            random.shuffle(nums)
        rows, cols = size
        for i in range(rows):
            board.append([])
            for j in range(cols):
                board[i].append(nums.pop())
        return board
    
    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-'*(len(row)*2-1))