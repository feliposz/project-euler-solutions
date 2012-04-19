"""Problem 205
06 September 2008

Peter has nine four-sided (pyramidal) dice, each with faces numbered
1, 2, 3, 4.

Colin has six six-sided (cubic) dice, each with faces numbered 1, 2,
3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total
wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give
your answer rounded to seven decimal places in the form 0.abcdefg
"""

# Find and count the combinations of cubic dice that result in a
# certain sum. For example:
# 1, 1, 1, 1, 1, 1 is the only possible combination for getting 6
# 6, 6, 6, 6, 6, 6 is the only possible combination for getting 36
# But there are 4332 ways of getting 21

d6_count = {}
d6_combinations = 0
for d1 in range(1, 7):
    for d2 in range(1, 7):
        for d3 in range(1, 7):
            for d4 in range(1, 7):
                for d5 in range(1, 7):
                    for d6 in range(1, 7):
                        d6_sum = d1 + d2 + d3 + d4 + d5 + d6
                        if d6_sum in d6_count:
                            d6_count[d6_sum] += 1
                        else:
                            d6_count[d6_sum] = 1
                        d6_combinations += 1

# Use the same logic to find out how many possible outcomes for a
# combination of 9 pyramidal dice 

d4_count = {}
d4_combinations = 0
for d1 in range(1, 5):
    for d2 in range(1, 5):
        for d3 in range(1, 5):
            for d4 in range(1, 5):
                for d5 in range(1, 5):
                    for d6 in range(1, 5):
                        for d7 in range(1, 5):
                            for d8 in range(1, 5):
                                for d9 in range(1, 5):
                                    d4_sum = d1+d2+d3+d4+d5+d6+d7+d8+d9
                                    if d4_sum in d4_count:
                                        d4_count[d4_sum] += 1
                                    else:
                                        d4_count[d4_sum] = 1
                                    d4_combinations += 1

print("D6 possible combinations =", d6_combinations)
print("D4 possible combinations =", d4_combinations)

possible_games = d6_combinations * d4_combinations
print("Possible games =", possible_games)

# Count in how many possible games d4 would beat d6 and vice-versa
d4_wins = 0
d6_wins = 0
game_draws = 0
for d4_play in d4_count:
    for d6_play in d6_count:
        play_count = d4_count[d4_play] * d6_count[d6_play]
        if d4_play > d6_play:
            d4_wins += play_count
        elif d4_play < d6_play:
            d6_wins += play_count
        else:
            game_draws += play_count

total_games = d4_wins + d6_wins + game_draws
prob_d4 = d4_wins / total_games
prob_d6 = d6_wins / total_games
prob_draws = game_draws / total_games

print("Times D4 wins:", d4_wins)
print("Times D6 wins:", d6_wins)
print("Times game draws:", game_draws)
print("Total games:", total_games)
print("Probability that d4 wins:", prob_d4)
print("Probability that d6 wins:", prob_d6)
print("Probability that game draws:", prob_draws)

print("Answer = ", round(prob_d4, 7))
