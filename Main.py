from utils.player import Player
from utils.player import Deck
from utils.game import Board
import sys
from utils.player import Deck
sys.stdout.reconfigure(encoding='utf-8')
board = Board([player("player 1"), player("player 2"), player("player 3"), player("player 4")])
board.start_game()
print("Game started with players:", board.players)