"""Problem 54
10 October 2003

In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of
fives (see example 1 below). But if two ranks tie, for example, both
players have a pair of queens, then highest cards in each hand are
compared (see example 4 below); if the highest cards tie then the next
highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand Player 1          Player 2            Winner
1    5H 5C 6S 7S KD    2C 3S 8S 8D TD      Player 2
     Pair of Fives     Pair of Eights

2    5D 8C 9S JS AC    2C 5C 7D 8S QH      Player 1
     Highest card Ace  Highest card Queen
     
3    2D 9C AS AH AC    3D 6D 7D TD QD      Player 2
     Three Aces        Flush with Diamonds

4    4D 6S 9H QH QC    3D 6D 7H QD QS      Player 1
     Pair of Queens    Pair of Queens
     Highest card Nine Highest card Seven

5    2H 2D 4C 4D 4S    3C 3D 3S 9S 9D      Player 1
     Full House        Full House
     With Three Fours  with Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two
players. Each line of the file contains ten cards (separated by a
single space): the first five are Player 1's cards and the last five
are Player 2's cards. You can assume that all hands are valid (no
invalid characters or repeated cards), each player's hand is in no
specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

"""

# Type of hand constants
HIGH_CARD = 1
ONE_PAIR = 2
TWO_PAIRS = 3
THREE_OF_A_KIND = 4
STRAIGHT = 5
FLUSH = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
STRAIGHT_FLUSH = 9
ROYAL_FLUSH = 10

#TODO: Properly comment the code and give description for functions!!!
    
def euler54():
    """Solve problem 54 from Project Euler."""
    games = readGames()
    wins = countWins(games)
    print(wins)

def readGames():
    """Returns a list of poker games read from file."""
    file = open("poker.txt")
    games = []
    while True:
        line = file.readline().strip()
        if not line:
            break
        values = line.split(" ")
        player1 = values[0:5]
        player2 = values[5:]
        games.append([player1, player2])
    file.close()
    return games

def countWins(games):
    """Count how many games were win by each player."""
    scorePlayer1 = 0
    scorePlayer2 = 0
    for game in games:
        hand1 = game[0]
        hand2 = game[1]
        winner = getWinner(hand1, hand2)
        if winner == 1:
            scorePlayer1 += 1
        elif winner == 2:
            scorePlayer2 += 1
        else:
            # In this problem, all cases have clear winners
            print("There should be a clear winner for game:", hand1, hand2)
            print(typeHand(hand1), typeHand(hand2))
            print(getHandWithHigherCards(hand1, hand2))
            print(getWinner(hand1, hand2))
            break
    return (scorePlayer1, scorePlayer2)

def getWinner(hand1, hand2):
    """Returns the winner for a pair of hands."""
    typeHand1 = typeHand(hand1)
    typeHand2 = typeHand(hand2)
    if typeHand1 > typeHand2:
        winner = 1
    elif typeHand1 < typeHand2:
        winner = 2
    else: # Both hands are the same type, check highest card
        if typeHand1 == ROYAL_FLUSH:
            winner = 0
        elif typeHand1 in (HIGH_CARD, STRAIGHT, FLUSH, STRAIGHT_FLUSH):
            winner = getHandWithHigherCards(hand1, hand2)
        elif typeHand1 in (ONE_PAIR, TWO_PAIRS, THREE_OF_A_KIND, FULL_HOUSE, FOUR_OF_A_KIND):
            repeatedCards1 = getRepeatedCards(hand1)
            repeatedCards2 = getRepeatedCards(hand2)
            winner = getHandWithHigherCards(repeatedCards1, repeatedCards2)
            if winner == 0:
                winner = getHandWithHigherCards(hand1, hand2)
    return winner
    
def typeHand(hand):
    """Returns the type of hand in a poker game."""
    # Sort to make other tests easier
    hand = sortHand(hand)

    # Test for flush (all cards have the same suit)
    s = suit(hand[0])
    flush = True
    for card in hand[1:]:
        if s != suit(card):
            flush = False
            break

    # Test for straight (all cards in a sequence)
    first = cardValue(hand[0])
    expected = first + 1
    straight = True
    for card in hand[1:]:
        if cardValue(card) != expected:
            straight = False
            break
        expected = cardValue(card) + 1

    # Count cards with repeated values
    count = {}
    for card in hand:
        v = cardValue(card)
        count[v] = count.get(v, 0) + 1

    # Repeated cards tests
    pair = False
    twoPairs = False
    three = False
    four = False
    for v in count.keys():
        if count[v] == 2:
            if pair: # Found another pair
                twoPairs = True
            else:
                pair = True
        elif count[v] == 3:
            three = True
        elif count[v] == 4:
            four = True
    fullHouse = pair and three

    # Returns the type of hand. Since one hand could fit in more than
    # one type, test for higher types first.
    if straight and flush and first == 10:
        return ROYAL_FLUSH
    elif straight and flush:
        return STRAIGHT_FLUSH
    elif four:
        return FOUR_OF_A_KIND
    elif fullHouse:
        return FULL_HOUSE
    elif flush:
        return FLUSH
    elif straight:
        return STRAIGHT
    elif three:
        return THREE_OF_A_KIND
    elif twoPairs:
        return TWO_PAIRS
    elif pair:
        return ONE_PAIR
    else:
        return HIGH_CARD

def getHandWithHigherCards(hand1, hand2):
    """Returns the hand which has the higher cards."""
    assert len(hand1) == len(hand2), "Both hands should have same amount of cards"
    hand1 = list(reversed(sortHand(hand1)))
    hand2 = list(reversed(sortHand(hand2)))
    winner = 0
    for i in range(len(hand1)):
        if cardValue(hand1[i]) > cardValue(hand2[i]):
            winner = 1
            break
        elif cardValue(hand1[i]) < cardValue(hand2[i]):
            winner = 2
            break
    return winner

def getRepeatedCards(hand):
    """Returns only the cards with repeated values in the hand."""
    # Count repeated cards
    count = {}
    for card in hand:
        v = cardValue(card)
        count[v] = count.get(v, 0) + 1
    repeatedCards = []
    for card in hand:
        v = cardValue(card)
        if count[v] > 1:
            repeatedCards.append(card)
    return repeatedCards
        
def sortHand(hand):
    """Returns the hand sorted by card value."""
    return sorted(hand, key=cardValue)

def suit(card):
    """Returns the suit of a card."""
    return card[1]

def cardValue(card):
    """Returns the value of a given card."""
    if card[0] >= '2' and card[0] <= '9':
        return int(card[0])
    elif card[0] == 'T':
        return 10
    elif card[0] == 'J':
        return 11
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'K':
        return 13
    elif card[0] == 'A':
        return 14

##games = readGames()
##print(len(games))
##print(len(games[0]), games[0])
##print(len(games[0][0]), games[0][0])
##print(games[0][1])
##print(sortHand(games[0][1]))

##assert typeHand(['AS', '3D', '5C', '7H', '9S']) == HIGH_CARD, "HIGH_CARD"
##assert typeHand(['AS', 'AD', '5C', '7H', '9S']) == ONE_PAIR, "ONE_PAIR"
##assert typeHand(['AS', 'AD', '5C', '5H', '9S']) == TWO_PAIRS, "TWO_PAIRS"
##assert typeHand(['AS', 'AD', 'AC', '7H', '9S']) == THREE_OF_A_KIND, "THREE_OF_A_KIND"
##assert typeHand(['2S', '3D', '4C', '5H', '6S']) == STRAIGHT, "STRAIGHT"
##assert typeHand(['2S', '3S', '5S', '7S', '9S']) == FLUSH, "FLUSH"
##assert typeHand(['AS', 'AD', '5C', '5H', '5S']) == FULL_HOUSE, "FULL_HOUSE"
##assert typeHand(['AS', 'AD', 'AC', 'AH', '9S']) == FOUR_OF_A_KIND, "FOUR_OF_A_KIND"
##assert typeHand(['5S', '6S', '7S', '8S', '9S']) == STRAIGHT_FLUSH, "STRAIGHT_FLUSH"
##assert typeHand(['TS', 'JS', 'QS', 'KS', 'AS']) == ROYAL_FLUSH, "ROYAL_FLUSH"
##
##print(getRepeatedCards(['AS', '3D', '5C', '7H', '9S']))
##print(getRepeatedCards(['AS', 'AD', '5C', '7H', '9S']))
##print(getRepeatedCards(['AS', 'AD', '5C', '5H', '9S']))
##print(getRepeatedCards(['AS', 'AD', 'AC', '7H', '9S']))
##print(getRepeatedCards(['2S', '3D', '4C', '5H', '6S']))
##print(getRepeatedCards(['2S', '3S', '5S', '7S', '9S']))
##print(getRepeatedCards(['AS', 'AD', '5C', '5H', '5S']))
##print(getRepeatedCards(['AS', 'AD', 'AC', 'AH', '9S']))
##print(getRepeatedCards(['5S', '6S', '7S', '8S', '9S']))
##print(getRepeatedCards(['TS', 'JS', 'QS', 'KS', 'AS']))

if __name__ == "__main__":
    euler54()
    
