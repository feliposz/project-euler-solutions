"""
Under The Rainbow
Problem 493
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).
"""

import random

TOLERANCE = 0.0000000001

got_all = 0
tries = 0

random.seed()

    
while True:
    previous_ratio = 0


    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
    balls = list(range(70))
    ball_picks = {}

    for i in range(20):
        random_pick = random.randint(0, len(balls)-1)
        ball_number = balls.pop(random_pick)
        ball_picks[colors[ball_number//10]] = 1

    if len(ball_picks) == 7:
        got_all += 1

    tries += 1

    ratio = got_all / tries

    if tries % 1000 == 0:
        print('Got all: %d Tries %d Ratio: %.10f' % (got_all, tries, ratio))

        if abs(ratio - previous_ratio) <= TOLERANCE:
            break
    
    previous_ratio = ratio

# TODO: Not working!!! Will take trillions of tries to get to the right ratio. Brute forcing won't cut it, need to think probabilities...
