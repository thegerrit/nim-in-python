# Nim for Python

### About
This repository contains a Python encoding of the game Nim. It showcases my ability as a programmer, specifically Object-Oriented Programming and Dynamic Programming with Symmetry Breaking.

### Play Nim
To get started `cd` into the repo and run the script `play_nim.py`. This runs with vanilla Python. You shouldn't need any dependencies. The script will generate a menu with a list of different options. Note that this is not a best programming practice. I chose the text-interface menu for ease of programming and demonstration. Best practice is to pass the different options as parameters of the function call.

#### Options
* i - Instructions: learn about the project and the rules of NIM.
* r - Play against a random player. This is an agent that makes a random move.
* t - Two player game: play against a friend. You will have to take turns inputting your moves.
* g - Play against an agent that uses BINARY XOR as a heuristic to find the best move.
* b - Challenge: The binary XOR agent can find winning moves most of the time. The challenge mode initializes the game such that the agent is at a losing position. See if you can beat it! (Also, the agent is not a very good sport. Don't let it bother you too much).
* d - Play against an agent that uses Dynamic Programming to find the best move. This agent ALWAYS finds the optimal move (if it exists). Beating it will be very difficult. This agent works by caching best moves of sub-games in memory. Then it uses these subgames to determine the best move.
* m - Mine Solutions: our Dynamic Programming agent learns by playing more games and expanding the number of cached sub-games. In order to train our agent, we set it against itself to play games of increasing complexity. Then we write the cache to a .txt file so we can analyze it. __Warning__: This command will mine indefinitely, you must terminate with `Ctrl+C`.
