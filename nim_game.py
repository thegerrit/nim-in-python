import players
import random

def do_move(game_state, move):
    t_state = game_state.copy()
    t_state[move[0]] -= move[1]

    # remove the pile if it is empty
    if t_state[move[0]] <= 0:
        t_state.pop(move[0])

    t_state.sort()
    #print("After stone removal", t_state)
    # sort the game at every step to break symmetries
    return ( t_state )

class nim_game:
    # object that is a game of nim.
    # DATA STRUCTURE
    game_state = []
    #    playerA = nim_player()
    #   playerB = nim_player()
    ### ascending list representing current state of nim.
    # METHODS:
    ### Initialize
    def __init__(self, game_state):
        self.game_state = game_state

    ### Ask player A for move

    ### Compute Move
    def compute_move(self, move):
        self.game_state = do_move(self.game_state, move)

        print("Player removed %d stones from pile %d" % (move[1], move[0]))

        # sort the game at every step to break symmetries
        # self.game_state.sort()


    ### Play: while loop asking players for moves and then computing the move
    ###    and sorting the list representing the gamestate.
    def play(self, playerA, playerB):
        turn = 0
        while( len(self.game_state) > 0 ):
            if turn == 0:
                next_move = playerA.get_move(self.game_state)
            else:
                next_move = playerB.get_move(self.game_state)

            self.compute_move(next_move)
            turn = (turn + 1) % 2

        if turn == 0:
            print("Player 2 Wins")
        else:
            print("Player 1 Wins")
