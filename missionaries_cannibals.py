import sys
from time import sleep
import os
sys.setrecursionlimit(10**5)

def clear():
    os.system('CLS')


class Bot:
    def __init__(self, depth = 5):
        self.depth = depth
        self.possible_moves = [(1,0),(0,1),(1,1),(2,0),(0,2)]
        self.prev_visited = set()

    def find_best_move(self, left_port, right_port, boat, n):
        
        # Find the best move up into the rooted tree
        # Then perform the best move
        # We have 5 possible moves
        # We are going to check each move and see if it is the best move
        # We will go to at least 5 levels of the tree,
        # But there is still issue of Cycle in the tree

        def minimax(left, right, boat, depth, vis):

            if game_failed(left, right, boat):
                return -1
            if game_incomplete(left, right, boat, n)!=True:
                return 1+depth
            if depth == 0:
                return 0
            high_score = -1
            for m, c in self.possible_moves:
                temp_left, temp_right, temp_boat = left[:], right[:], boat
                if validate_move(temp_left, temp_right, temp_boat, m, c):
                    move_boat(temp_left, temp_right, temp_boat, m, c)
                    temp_boat = 1 - temp_boat
                    h = self.hash_it(temp_left, temp_right, temp_boat)
                    if h not in vis and h not in self.prev_visited:
                        vis.add(h)
                        score = minimax(temp_left, temp_right, temp_boat, depth-1, vis)
                        if score > high_score:
                            high_score = score
                   
            return high_score
        self.prev_visited.add(self.hash_it(left_port, right_port, boat))
        high_score = -1
        high_move = (0, 0)
        high_hash = None
        for m, c in self.possible_moves:
            temp_left, temp_right, temp_boat = left_port[:], right_port[:], boat
            if validate_move(temp_left, temp_right, temp_boat, m, c):
                move_boat(temp_left, temp_right, temp_boat, m, c)
                temp_boat = 1 - temp_boat
                if self.hash_it(temp_left, temp_right, temp_boat) not in self.prev_visited:
                    self.prev_visited.add(self.hash_it(temp_left, temp_right, temp_boat))
                    score = minimax(temp_left, temp_right, temp_boat, self.depth - 1, set())
                    if score > high_score:
                        high_score = score
                        high_move = (m, c)
                        high_hash = self.hash_it(temp_left, temp_right, temp_boat)
        
        if high_move == (0,0):
            print("Every Available Move will take me to a cycle")   
            return 0, 0
        self.prev_visited.add(high_hash)
        return high_move
        

                     


        
            
    def hash_it(self,left_port, right_port, boat):
        return str(left_port) + str(right_port) + str(boat)




class Player:
    def __init__(self, name = "Anon"):
        self.name = "Anon"
    
    def find_best_move(self, left_port, right_port, boat, n):
        ip = input("Enter the Missionaries and Cannibals to move the boat: ")
        m, c = map(int, ip.split())
        while validate_move(left_port, right_port, boat, m, c) == False:
            print("Invalid Move")
            ip = input("Enter the Missionaries and Cannibals to move the boat: ")
            m, c = map(int, ip.split())
        return m, c
        

    
    


def print_game(left_port, right_port, boat):
    '''
    print the game board
    '''
    clear()
    print("-"*25)
    print("M  -  C  |"+" "*26+"| M  -  C")
    print(f"{left_port[0]}  -  {left_port[1]}  |",end='')
    if boat == 0:
        print(" BOAT "+" "*20,end='')
    else:
        print(" "*20+" BOAT ",end='')
    print(f"| {right_port[0]}  -  {right_port[1]}")

def game_incomplete(left_port, right_port, boat, n):
    '''
    check if the game is incomplete
    '''
    if left_port[0] == 0 and left_port[1] == 0 and right_port[0] == n and right_port[1] == n and boat == 1:
        return False
    return True

def validate_move(left_port, right_port, boat, m, c):
    '''
    validate the move
    '''

    if m+c > 2 or m<0 or c<0:
        return False
    if boat == 0:
        if left_port[0] - m < 0 or left_port[1] - c < 0:
            return False
    else:
        if right_port[0] - m < 0 or right_port[1] - c < 0:
            return False
    return True

def move_boat(left_port, right_port, boat, m, c):
    '''
    Move the Boat
    '''
    if boat == 0:
        left_port[0] -= m
        left_port[1] -= c
        right_port[0] += m
        right_port[1] += c
        
    else:
        left_port[0] += m
        left_port[1] += c
        right_port[0] -= m
        right_port[1] -= c
    
    

def game_failed(left_port, right_port, boat):
    '''
    check if the game is failed
    '''
    if (0 < left_port[0] < left_port[1] and boat==1) or (0 < right_port[0] < right_port[1] and boat == 0):
        return True
    return False



def start(n, player):
    '''
    start the game with N Missionaries and N cannibals
    '''
    

    left_port = [n, n]
    right_port = [0, 0]
    boat = 0
    
    
    def game_loop():
        nonlocal boat
        while game_incomplete(left_port, right_port, boat,n):
            print_game(left_port, right_port, boat)
            m, c = player.find_best_move(left_port, right_port, boat, n)
            move_boat(left_port, right_port, boat, m, c)
            boat = 1-boat
            if game_failed(left_port, right_port, boat):
                print("Game Failed")
                break
            sleep(1)
        else:
            print_game(left_port, right_port, boat)
            print("Game Completed!!")
    
    game_loop()

def main():
    
    if input("Enable AI Play (Y/N) : ?").lower() == "y":
        player = Bot()
    else:
        player = Player()
    
    n = 3 # Able to take input
    start(3,player)

if __name__ == '__main__':
    main()