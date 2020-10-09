import random
import nim_game
import os

# calculate the nim_sum (cummulative XOR) for a given state
def nim_sum(game_state):
    acc_sum = 0
    for i in game_state:
        acc_sum = acc_sum ^ i
    return acc_sum

#return the minimal excludant from a list of acion, state_value pairs
def mex(succ_states):
    curr_mex = 0
    while curr_mex in succ_states:
        curr_mex += 1
    return curr_mex

# search for an action that makes the nim_sum zero
def binary_policy(game_state):
    if nim_sum(game_state) == 0:
        print("BINARY: I can't win if you play optimally :P")
        return (0,1)
    else:
        for i in range(0, len(game_state)):
            for j in range(1,4):
                action = (i,j)
                temp_state = game_state.copy()
                temp_state[i] -= j
                if nim_sum(temp_state) == 0:
                    print("BINARY: There is nothing you can do to beat me LOSER!")
                    return action
        print("BINARY: I can't find an optimal move, its anybody's game!")
        return (0,1)

# Abstract class with methods for nim players
class nim_player:
    # a player in the game of nim.
    # METHODS:
    name = "no name"
    def __init__(self):
        pass

    ### Compute best Move
    def get_move(self, game_state):
        # override
        pass

class random_player(nim_player):
    def get_move(self, game_state):
        take = -1
        pile = random.randrange(0,len(game_state), 1)
        #randomly select a number of stones to remove
        take = random.choice([1,2,3])

        # return an action, precisely the pile, take pair
        print("random player removed " + str(take) + " stones from pile " +str(pile))
        return (pile, take)

class human_player(nim_player):
    def __init__(self):
        print("Enter player name")
        self.name = input()
    #print a visual of the nim game
    def vis_game(self, game_state):
        print("\nPILE # |   STONES")
        for i in range(0, len(game_state)):
            print("  " + str(i) + "    | ", end="")

            for j in range(game_state[i]):
                print("0 ", end="")
            print("")

        print("AS LIST ", game_state)
        print("")

    '''Ask the human player to input a move'''
    def get_move(self, game_state):
        #print(game_state)
        print("PLAYER " + self.name)
        self.vis_game(game_state)
        while True:
            pile = int(input("Enter a pile to take from: "))
            take = int(input("Enter the amount of stones to take (between 1 and 3): "))
            # input validation
            if (pile < len(game_state)) and (pile >= 0) and (take > 0) and (take <= 3):
                break
            print("Invalid input, try again")

        return (pile, take)

class binary_player(nim_player):
    def get_move(self, game_state):
        return binary_policy(game_state)

'''Player that dynaimcally evalutes game states of nim'''
class dynamic_player(nim_player):
    cache = {}
    def get_move(self, game_state):
        eval = self.dynamic_eval(game_state)
        return eval[0]
    def __init__(self, cache_file):
        # open the cache file to read
        f = open(cache_file, "r")
        # write every line in the cache file to the dictionary
        for line in f:
            key_val_pair = line.split(":")
            self.cache[key_val_pair[0]] = eval(key_val_pair[1])
    '''Save cache to a text file'''
    def save_cache(self, cache_file):
        # delete old cache file
        if os.path.exists(cache_file):
            os.remove(cache_file)
        f = open(cache_file, "a")
        sol_counter = 0
        # write each entry of the dictionary to the cache_file
        for i in self.cache:
            line = ( i + ":" + str(self.cache[i]) +"\n" )
            f.write(line)
            sol_counter += 1

        print(str(sol_counter) + " solutions cached!")
        f.close()

    '''recursive, dynamic programming algorithm that calculates the optimal action in a game of NIM'''
    def dynamic_eval(self, game_state):
        # Check cache for game state
        #### if gamestate in cache, return evaluation
        if str(game_state) in self.cache:
            # return evaluation
            return self.cache[str(game_state)]
        #### gamestate not in cache, evaluate it recursively
        else:
            ## recursively call dynamic_eval to evaluate legal actions,
            action_to_return = ( (0,0), 99999999)
            succ_nimbers = []

            ## calculate the nimber = minimal excludant of all nimbers of successor states.
            #iterate over pile indices
            for i in range(len(game_state)):
                # iterate over number of stones to take
                for j in range(1,4):
                    action = (i, j)
                    # generate transition state
                    next_state = nim_game.do_move(game_state, action)
                    # evaluate transition state
                    next_state_eval = self.dynamic_eval(next_state)

                    #add the nimber to the current list of succ_nimbers
                    succ_nimbers.append(next_state_eval[1])

                    #return the action that maxes the nimber 0
                    if next_state_eval[1] == 0:
                        action_to_return = (action, 0)
                    else:
                        # return action that minimizes successor state nimbers
                        if action_to_return[1] >= next_state_eval[1]:
                            action_to_return = (action, next_state_eval[1])
        #pair the best action and the mex nimber
        action_tuple = (action_to_return[0], mex(succ_nimbers))

        # add to cache
        self.cache[str(game_state)] = action_tuple
        return action_tuple
