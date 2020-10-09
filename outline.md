# Combinatorial Game Theory
Final Project
Garrett Van Beek
Intro to Experimental Math
Professor Diego Villamizar
May 1, 2020

### What is Game Theory

### What is Nim? Grundy-Sprague Theorem.

### How can we formulate theorems like the Grundy-Sprague Theorem Formulated?


#### Challenges
Search space grows exponentially. Symmetry breaking
##### Dynamic Programming
My evaluation function evaluates every action at every state. For my agents to evaluate states faster,
I stored the value of every state to avoid recalculating it.

##### Alph-Beta Pruning.

##### Symmetry Breaking
NIM has many identical states. For example [1,2,1] is the same as [2,1,1]. In other words,
they are symmetric. Symmetry breaking is the practice of reducing the search space of our
problem by avoiding symmetric states. In order to break the symmetries in NIM, I sorted the
list representing the game state in ascending order. This way, both states above will be viewed
as the same state: [1,1,2].

### MDP and Nim Demo!
