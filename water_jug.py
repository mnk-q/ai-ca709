'''
You are on the side of the river. You are given a m liter jug and a n liter jug where 0 < m < n. Both the jugs are initially empty. The jugs don’t have markings to allow measuring smaller quantities. You have to use the jugs to measure d liters of water where d < n. Determine the minimum no of operations to be performed to obtain d liters of water in one of jug. 
The operations you can perform are: 

Empty a Jug
Fill a Jug
Pour water from one jug to the other until one of the jugs is either empty or full.

'''

'''
Possible Approaches
 - Breadth First Search
 - Dynamic Programming
 - Diophantine Equation

'''

from collections import deque
import os
from time import sleep
def intro(m,n, d):
    print('''
    

 /$$      /$$             /$$                                  /$$$$$                           /$$$$$$$                     /$$       /$$                        
| $$  /$ | $$            | $$                                 |__  $$                          | $$__  $$                   | $$      | $$                        
| $$ /$$$| $$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$             | $$ /$$   /$$  /$$$$$$       | $$  \ $$ /$$$$$$   /$$$$$$ | $$$$$$$ | $$  /$$$$$$  /$$$$$$/$$$$ 
| $$/$$ $$ $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$            | $$| $$  | $$ /$$__  $$      | $$$$$$$//$$__  $$ /$$__  $$| $$__  $$| $$ /$$__  $$| $$_  $$_  $$
| $$$$_  $$$$  /$$$$$$$  | $$    | $$$$$$$$| $$  \__/       /$$  | $$| $$  | $$| $$  \ $$      | $$____/| $$  \__/| $$  \ $$| $$  \ $$| $$| $$$$$$$$| $$ \ $$ \ $$
| $$$/ \  $$$ /$$__  $$  | $$ /$$| $$_____/| $$            | $$  | $$| $$  | $$| $$  | $$      | $$     | $$      | $$  | $$| $$  | $$| $$| $$_____/| $$ | $$ | $$
| $$/   \  $$|  $$$$$$$  |  $$$$/|  $$$$$$$| $$            |  $$$$$$/|  $$$$$$/|  $$$$$$$      | $$     | $$      |  $$$$$$/| $$$$$$$/| $$|  $$$$$$$| $$ | $$ | $$
|__/     \__/ \_______/   \___/   \_______/|__/             \______/  \______/  \____  $$      |__/     |__/       \______/ |_______/ |__/ \_______/|__/ |__/ |__/
                                                                                /$$  \ $$                                                                         
                                                                               |  $$$$$$/                                                                         
                                                                                \______/                                                                          

    ''')
    print(f'''
You are on the side of the river. You are given a {m} liter jug and a {n} liter jug. Both the jugs are initially empty. The jugs do not have markings to allow measuring smaller quantities. \nYou have to use the jugs to measure {d} liters of water. Determine if it is Possible and then Find the minimum no of operations to be performed to obtain {d} liters of water in one of jug. 
The operations you can perform are: 

Empty a Jug
Fill a Jug
Pour water from one jug to the other until one of the jugs is either empty or full.


type help to see more information.
    ''')

    print('\n\n')

def help():
    print("!!!  INSTRUCTIONS  !!!")
    print('''Following Commands are available :
    fill [i]         :  Fills the Bucket [i].")
    empty [i]        :  Empties the Bucket [i]")
    pour [i] to [j]  :  Pours all Water from Bucket [i] to [j]. ")
    list             :  Allows you to write multiple instructions, each instruction on one line. End with 0 in last line. ")
    
    Example
    fill 1       -> Will fill the bucket 1
    empty 2      -> Will empty the bucket 2
    pour 1 to 2  -> Will Fill Bucket 2 as much as it can with water of Bucket 1.
    list         -> Can write Multiple Instructions. Executes in a transaction-fashion. Will abort whole transaction if any one statement is invalid. End the list with 0 in last line.
    -> fill 1 
    -> pour 1 to 2
    -> empty 2
    -> fill 1
    -> 0
    ''')

def print_jugs(m, n, M, N):
    print('''
       ___                                         ___
    .-'   `-.                                   .-'   `-.
   /         \\                                 /         \\
  /   _____   \\                               /   _____   \\
 /.-'"     "`-.\\                             /.-'"     "`-.\\
d(             )b                           d(             )b
 |`-.._____..-'|                             |`-.._____..-'|
 |             |                             |             |
 |             |                             |             |
 |             |                             |             |
 |             |                             |             |
 |             |                             |             |
 |             |                             |             |
 |             |                             |             |
 \             /                             \             /
  `-.._____..-'                               `-.._____..-'   
    ''')
    print(f"Capacity {M} , Current {m}                    Capacity {N} , Current {n}")






class Bot:
    def __init__(self, depth = 3):
        self.depth = depth
        self.transition_states = [
            {'action': 'fill', 'jug': '1'},
            {'action': 'fill', 'jug': '2'},
            {'action': 'empty', 'jug': '1'},
            {'action': 'empty', 'jug': '2'},
            {'action': 'pour', 'jug': '1', 'other_jug': '2'},
            {'action': 'pour', 'jug': '2', 'other_jug': '1'}
        ]
    
    
    def get_action(self, queue:deque, M, N, D):
        q = self.bfs(M, N, D)
        queue.extend(q)
        return

    

    def bfs(self,M,N,d):
        ''' This BFS + DP Approach is optimal. It will give the minimum steps to reach the goal state. '''
        INF = int(1e5)
        dp = [[INF for i in range(N+1)] for j in range(M+1)]
        dp[0][0] = 0
        queue = deque([(0,0,0)])
        parent = [[(-1, -1) for i in range(N+1)] for j in range(M+1)]
        tm, tn = 0, 0
        while queue:
            m, n, c = queue.popleft()
            if m == d or n == d:
                break
            for index, action in enumerate(self.transition_states):
                tm, tn = state_changer(action, m, n, M, N)
                if tm==m and tn==n:
                    continue
                if 0<=tm<=M and 0<=tn<=N and dp[tm][tn] > c+1:
                    dp[tm][tn] = c+1
                    parent[tm][tn] = (m,n,index)
                    queue.append((tm,tn,c+1))
        else:
            return -1
        path = [] # Should return the list of actions to reach the goal state.
        while not (m==n==0):
            path.append(self.transition_states[parent[m][n][2]])
            m,n = parent[m][n][0], parent[m][n][1]
        
        path.reverse()
        return path

def suitable_print_msg(action):
    '''Return a Suitable print Message for the action'''

    if action['action'] == 'fill':
        return f"Filled {action['jug']}"
    elif action['action'] == 'empty':
        return f"Emptied {action['jug']}"
    elif action['action'] == 'pour':
        return f"Poured {action['jug']} to {action['other_jug']}"
    else:
        return "Invalid Action"



class Player:

    def __init__(self):
        pass

    def get_action(self,queue, M, N, D):

        ip = input("-> ")
        if ip == "help":
            help()
            return
        if ip == "list":
            while True:
                ip = input("-> ")
                if ip == "0":
                    break
                if not validate_input(ip):
                    print("Invalid Input")
                    return
                queue.append(action_maker(ip))
        if not validate_input(ip):
            print("Invalid Input")
        else:
            queue.append(action_maker(ip))
    

def state_changer(action, m, n, M, N):
        if action["action"] == "fill":
            if action["jug"] == "1":
                m = M
            else:
                n = N
        elif action["action"] == "empty":
            if action["jug"] == "2":
                m = 0
            else:
                n = 0
        elif action["action"] == "pour":
            if action["jug"] == "1":
                n,m = min(N, n + m), max(0, m - (N - n))
            else:
                m,n = min(M, m + n), max(0, n - (M - m))
        return m, n

def validate_input(input_str):
    if input_str == "help":
        help()
        return True
    elif input_str == "list":
        return True
    else:
        ip = input_str.split()
        if ip[0].lower() in {"fill", "empty"}:
            if len(ip) == 2 and ip[1].isdigit() :
                return True
        elif ip[0].lower() == "pour":
            if len(ip) == 4 and ip[1].isdigit() and ip[3].isdigit() and ip[1]!=ip[3] and ip[2].lower() == "to":
                return True
        return False


def action_maker(ip):
    action = {}
    ip = ip.split()
    action["action"] = ip[0]
    action["jug"] = ip[1]
    if len(ip) == 4:
        action["other_jug"] = ip[3]
    return action

def engine(M,N,D):
    assert(M>N)
    assert(M>D)
    # intro(M,N,D)
    m,n = 0, 0 
    # print_jugs(m,n,M,N)
    if input("Enable AI Gameplay ?(Y/N)  : ").lower() == 'y':
        player = Bot()
    else:
        player = Player()

    def game_loop():
        nonlocal m, n
        action_queue = deque()
        while True:
            sleep(1)
            os.system("CLS")
            print_jugs(m, n, M, N)
            if m == D or n == D:
                
                print(f"Game Completed ! Bucket {1+(m!=D)} has {D} Litres")
                return
            if action_queue:
                action = action_queue.popleft()
                m,n = state_changer(action, m, n, M, N)
                action_msg = suitable_print_msg(action)
                print(action_msg)
                
            else:
                player.get_action(action_queue, M, N, D)                
            
    
    game_loop()

engine(5,3,4)