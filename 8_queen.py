# A Simple Solution for 8 Queen Problem

import random

def random_queen():
    return random.randint(0, 7)

def random_board():
    return [random_queen() for i in range(8)]

def is_safe(board):
    for i in range(8):
        for j in range(i+1, 8):
            if board[i] == board[j]:
                return False
            if abs(i-j) == abs(board[i]-board[j]):
                return False
    return True

def print_board(board):
    for i in range(8):
        for j in range(8):
            if board[i] == j:
                print('Q', end='')
            else:
                print('.', end='')
        print()

def heuristic(board):
    '''
    Calculate Heuristic of the current board.
    It is number of pairs of queens that are attacking each other.
    '''
    h = 0
    for i in range(8):
        for j in range(i+1, 8):
            if board[i] == board[j]:
                h += 1
            if abs(i-j) == abs(board[i]-board[j]):
                h += 1
    return h
    
def backtracking(board, col):
    if col >= 8:
        return True
    print(heuristic(board))
    for i in range(8):
        board[col] = i
        if is_safe(board):
            if backtracking(board, col+1):
                return True
    return False    


def generate_neighbours_with_heuristic(board):
    neighbours_heuristics = []
    for i in range(8):
        for j in range(8):
            if board[i] != j:
                new_board = board[:]
                new_board[i] = j
                neighbours_heuristics.append((new_board, heuristic(new_board)))
    neighbours_heuristics.sort(key=lambda x: x[1])
    return neighbours_heuristics

def main():
    board = random_board()
    
    while not is_safe(board):
        print(heuristic(board))
        print("Generating Neighbours")
        neighbours = generate_neighbours_with_heuristic(board)
        print("Neighbours Generated")
        print("Choosing Neighbour")
        if neighbours[0][1] >= heuristic(board):
            print("Got stuck in Shoulder, Generating Board")
            board = random_board()
        else:
            board = neighbours[0][0]
    if is_safe(board):
        print("Solution Found")
        print_board(board)
    else:
        print("No Solution Found")
        print("Stuck in Local Maxima")
if __name__ == '__main__':
    main()