class WupmusWorld:
    def __init__(self, board_size = 5, wumpus = 1, pits = 5, gold = 1, arrows = 1):
        self.board_size = board_size
        self.wumpus = wumpus
        self.pits = pits
        self.gold = gold
        self.board = [;]
        self.agent = None
        self.wumpus = None
        self.pits = []
        self.gold = None
        self.score = 0
        self.arrows = arrows
        self.game_over = False
        self.won = False
        self.setup()