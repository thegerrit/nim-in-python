import nim_game
import players
import random

def instructions():
    print(
        "       INSTRUCTIONS       \n" +
        "--------------------------\n" +
        "1. About\n" +
        "    This is an educational program for studying game theory. Particularly\n" +
        "it is an encoding of the game NIM. The Grundy-Spague Theorem is used to\n" +
        "determine optimal play for NIM as well as any other perfect, impartial games.\n" +
        "Try playing NIM with a friend, or even better, challenge yourself to beat an \n" +
        "agent that plays optimally!\n"
        "2. Nim Rules:\n" +
        "  - Players take turns removing stones from piles.\n" +
        "  - A player may only take from one pile per turn.\n" +
        "  - A player must take 1-3 stone(s) every turn.\n" +
        "  - The player who takes the last stone(s) wins.")

def user_interface():
    # user inputs characters as options and different functions are called
    # under the hood.
    print(" ** MENU ** ")
    print("Input a letter corresponding to the following options\n")
    print("i ---- instructions")
    print("r ---- play against random player")
    print("t ---- 2 player human game")
    print("g ---- play against an agent that uses Binary XOR Evaluation")
    print("b ---- CHALLENGE! Can you beat the binary XOR evaluation Agent")
    print("d ---- Play human vs dynamic agent")
    print("m ---- Mine Solutions")
    print("a ---- Play versus a winning state")
    print("q ---- exit\n")
    p = input()
    #initialize the players
    if (p == 'r'):
        playerA = players.human_player()
        playerB = players.random_player()

    elif (p == 't'):
        playerA = players.human_player()
        playerB = players.human_player()
    elif (p == 'g'):
        playerA = players.human_player()
        playerB = players.binary_player()
    elif (p == 'i'):
        instructions()
        exit()
    elif (p == 'b'):
        binary_challenge()
        exit()
    elif (p == 'd'):
        dynamic_game()
        exit()
    elif (p == "m"):
        mine_solutions()
        exit()
    elif (p == "a"):
        playerA = players.dynamic_player("init_cache.txt")
        playerB = players.human_player()
        d_game = nim_game.nim_game([1, 1, 1, 2, 3, 3, 6, 8, 8, 12, 14, 14, 14])
        d_game.play(playerA, playerB)
        exit()
    else:
        print("Error: Invalid Input")
        exit()
        pass


    #initialize game
    my_game = nim_game.nim_game(random_board(6,9))

    #play the game
    my_game.play(playerA, playerB)

    return
challenge_boards1 = [
    [3,4,4,4],
    [2,5,8],
    [4,5,6,8],
    [1,2,24,10,11],
    [1,4,5,5,7],
    [3,4,7,8]
]
challenge_boards2 = [
    [4,4,4,4],
    [4,4,6,6],
    [1,1,2,2],
    [1,1,4,4,5,5],
    [2,5,7],
    [1,8,9]
]
def binary_challenge():
    print("BINARY: Finally a worthy opponent!")
    print("BINARY: Would you like to move first or second? [1/2]")
    while True:
        t = int(input())
        if t==1 or t==2:
            break
        print("Invalid input, try again")

    board = random.choice([0,1,2,3,4,5])
    #player moves first
    if t==1:
        playerA = players.human_player()
        playerB = players.binary_player()
        game = nim_game.nim_game( challenge_boards1[board] )


    #grundy moves first
    else:
        playerA = players.binary_player()
        playerB = players.human_player()
        game = nim_game.nim_game( challenge_boards2[board] )

    game.play(playerA, playerB)
    exit()

# generate a random configuration of nim
def random_board(num_piles, max_stones):
    l = []
    for i in range(num_piles):
        t = random.choice(range(1, max_stones+1))
        l.append(t)
    l.sort()
    return l

def dynamic_game():
    playerA = players.human_player()
    playerB = players.dynamic_player("init_cache.txt")

    game = nim_game.nim_game([1,2,3,4,5,6])

    game.play(playerA, playerB)

    playerB.save_cache("dynamic_game_cache.txt")

def mine_solutions():
    num_games = 0
    max_stones = 5
    max_piles = 5
    while True:
        print(num_games, " games played")

        num_piles = random.randint(1, max_piles)
        playerA = players.dynamic_player("mine_cache.txt")
        board = random_board(max_piles, max_stones)
        game = nim_game.nim_game(board)
        #dynamic player plays against itself!
        game.play(playerA, playerA)
        playerA.save_cache(input("Enter a filepath with a .txt extension to save our cache to."))

        #increase complexity as we continue mining
        max_stones += 1
        max_piles += 1
        num_games += 1



def main():
    user_interface()

main()
