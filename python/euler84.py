##In the game, Monopoly, the standard board is set up in the following way:
##
##GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
##H2	 	                                C1
##T2	 	                                U1
##H1	 	                                C2
##CH3	 	                                C3
##R4	 	                                R2
##G3	 	                                D1
##CC3	 	                                CC2
##G2	 	                                D2
##G1	 	                                D3
##G2J	F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP
##A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.
##
##In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.
##
##At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.
##
##Community Chest (2/16 cards):
##Advance to GO
##Go to JAIL
##Chance (10/16 cards):
##Advance to GO
##Go to JAIL
##Go to C1
##Go to E3
##Go to H2
##Go to R1
##Go to next R (railway company)
##Go to next R
##Go to next U (utility company)
##Go back 3 squares.
##The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.
##
##By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.
##
##Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.
##
##If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

from random import shuffle, randint

board = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
         "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
         "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
         "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]

stats = [0] * 40

communityChestCards = [board.index("GO"), board.index("JAIL")] + [None] * 14
chanceCards = [board.index("GO"), board.index("JAIL"), board.index("C1"), board.index("E3"),
               board.index("H2"), board.index("R1"), "NEXT R", "NEXT R", "NEXT U", "BACK 3"] + [None] * 6

def playDie():
    #return randint(1, 6) -- original
    return randint(1, 4)

def playOneGame(movesPerGame):
    global board, communityChestCards, chanceCards, stats

    shuffle(communityChestCards)
    shuffle(chanceCards)

    equalDiceCount = 0
    position = 0

    for i in range(movesPerGame):

        action = None

        #TODO: refactor to makeMove
        die1 = playDie()
        die2 = playDie()

        if die1 == die2:
            equalDiceCount += 1
        else:
            equalDiceCount = 0

        if equalDiceCount == 3:
            action = board.index("JAIL")
            equalDiceCount = 0
        else:
            position = (position + die1 + die2) % 40

        #for special case (see below)
        while True:

            #TODO: Refactor to determineAction
            if board[position] == "G2J":
                action = board.index("JAIL")
            elif board[position] in ("CC1", "CC2", "CC3"):
                action = communityChestCards.pop()
                communityChestCards.insert(0, action)
            elif board[position] in ("CH1", "CH2", "CH3"):
                action = chanceCards.pop()
                chanceCards.insert(0, action)
            else:
                action = None

            #TODO: Refactor to applyAction
            if action == None:
                None #do nothing, already moved
            elif action == "BACK 3":
                position = (position - 3) % 40
                if board[position] == "G2J":
                    action = board.index("JAIL")
                    equalDiceCount = 0
                elif board[position] == "CC3":
                    #Special case!
                    #if ended on CH3, got the BACK 3 card and ended at CC3, need to take another card
                    continue
            elif action == "NEXT R":
                if position < board.index("R1"):
                    position = board.index("R1")
                elif position < board.index("R2"):
                    position = board.index("R2")
                elif position < board.index("R3"):
                    position = board.index("R3")
                elif position < board.index("R4"):
                    position = board.index("R4")
                else:
                    position = board.index("R1")
            elif action == "NEXT U":
                if position < board.index("U1"):
                    position = board.index("U1")
                elif position < board.index("U2"):
                    position = board.index("U2")
                else:
                    position = board.index("U1")
            else:
                position = action

            break

        assert position >= 0 and position <= 39, "position should be from 0 to 39"
        stats[position] += 1

def printStats():
    global board, stats
    total = sum(stats)
    print("POS NAME STATS PERC")
    for i in range(40):
        print("{0:3d} {1:4} {2:8d} {3:8f}".format(i, board[i], stats[i], stats[i]/total*100))

def calcStats(numGames, movesPerGame):
    for i in range(numGames):
        playOneGame(movesPerGame)

def answer():
    global stats
    statsClone = list(stats) #clone
    statsClone.sort()
    statsClone.reverse()
    first = stats.index(statsClone[0])
    second = stats.index(statsClone[1])
    third = stats.index(statsClone[2])
    total = sum(stats)
    print("answer:")
    for i in (first, second, third):
        print("{0:2d} {1:4} {2:8d} {3:8f}".format(i, board[i], stats[i], stats[i] / total * 100))

def euler84():
    calcStats(1000, 1000)
    printStats()
    answer()

euler84()

