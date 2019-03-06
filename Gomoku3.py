#!/usr/bin/python3
#/usr/local/bin/python3
# Set the path to your python3 above

from gtp_connection import GtpConnection
from board_util import GoBoardUtil
from simple_board import SimpleGoBoard

class Gomoku():
    def __init__(self):
        """
        Gomoku player that selects moves randomly 
        from the set of legal moves.
        Passe/resigns only at the end of game.

        """
        self.name = "GomokuAssignment3"
        self.version = 1.0
        
    def get_move(self, board, color):
        return GoBoardUtil.generate_random_move_gomoku(board)

    # Generates a list of moves based on the current policies
    # Returns tuple: (MoveType, [moves])
    # MoveType = {Win, BlockWin, OpenFour, BlockOpenFour, Random}
    def get_policy_moves(self, board, useRules=True):
        if (useRules):
            MoveType, moves = GoBoardUtil.generate_rule_based_moves(board)
            if (MoveType != "Random"):
                return MoveType, moves
        # if we're not using rules
        # or generate_rule_based_moves(..) returned nothing
        moves = GoBoardUtil.generate_legal_moves_gomoku(board)
        if (len(moves) > 0):
            return "Random", moves
        return "", []
    
def run():
    """
    start the gtp connection and wait for commands.
    """
    board = SimpleGoBoard(7)
    con = GtpConnection(Gomoku(), board)
    con.start_connection()

if __name__=='__main__':
    run()
