
ARTIFICIAL INTELLIGENCE - Mini Project: Backgammon Game


Attached files :


Features :

# Depth2.py is a simple version of our strategy going down upto 2 levels.
# Depth3.py is a much more advanced version going down upto 3 levels.

P.S. : Depth3.py requires a good machine to be run upon, might harm delicate machines.
----------------------------------------------------------------------------------------------

Strategies :

Its a mixed strategy where our focus is on the following points :

-> Fortification is good, can also be explained as you make your doors(more than one checker) stand next to each other and it acts like a wall preventing oponent's checker to cross. The longer the strech of the wall(<=6), good it is. Also be said to be "Prime" technique.

-> Forming Doors is a good thing, especially when built in home block. Although doors of size greater than 4 are a little undesired.
   Whereas doors of opponent are not desired to be formed. However their doors exceeding size 4 are in a way considered good.   
   Implemented using a cumulative frequency.

-> Hitting a loner blot, is considered a good move. As it gives the control of whole board to us untill opponent returns.

-> Randomization, to introduce a little surprise elements for moves once 70% of checkers have reached home block.

-> Priority given to bearing off, less the number of checkers left on the board better are the chances of winning.

===============================================================================================

Input Format :
The program takes the following as input :

C1 C2 C3...C24
Z1 Z2
R1 R2

Where C(i) is the number of checkers on i point, Z1 is the number of checkers on bar for Alice and Z2 is for Bob.
R1 and R2 are the 2 numbers on dice for this move.


===================================================================================================

Output Format:
The program prints the following:

C(i) C(j)

where C(i) is the initial position of the checker and C(j) is the final one.

In case of bearing off,

C(i) 0
where C(i) is the initial position and 0 denotes bearing off

For every move that's passed, "pass" is printed. If both moves are passed, the following is the o/p:

pass
pass


===================================================================================================
Flow :

Depth2 :
----------------------------------------
All the possible moves of Alex are generated given the initial board config. , dices and bar values.
For each move we compute all the 36 dice combinations and the moves the opponent would make based on each dice configuration.
Then we apply evaluation function with the above mentioned strategies on the resulting moves by opponent.
We take the expectimax*** [ average ] of the evaluation values of the opponent moves and store it in OUR's each configuration.
Then we simply take the max out of OUR's resulting board configs based on the eval. value.

***The expected value because its Stochastic because of dice configs
----------------------------------------

Depth3 < A little tough, stay calm >: 
----------------------------------------
All the possible moves of Alex are generated given the initial board config. , dices and bar values.
For each move say Ai we compute all the 36 dice combinations and then the moves the opponent would make based on each dice configuration.
Say the move made by opponent is Bi, then we go further DOWN one level.
For each move Bi we compute dice configs `d and for each `di the possible board configs which will result when Alex shall play.
Say these board configs are `Ai.
We apply evaluation function on `Ai s to see where we stand after we make one move, oppponent makes his and then again we make ours.
Then we store the MAX of these `Ai s corresponding to a particular DICE config. `di.
Then we calculate the expectimax*** [ average ] of all the `di values for a particular opponent move Bi.
Then for all Bi corresponding to a particular Ai we calculate expectimax*** [ average ] and store it in each Ai.
Then we choose the Ai with maximum eval. value.
And that is our move .....

***The expected value because its Stochastic because of dice configs
---------------------------------------- 
===================================================================================================
