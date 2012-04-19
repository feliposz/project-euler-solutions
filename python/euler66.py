"""Problem 66
26 March 2004

Consider quadratic Diophantine equations of the form:

x² – Dy² = 1

For example, when D=13, the minimal solution in x is 649² – 13*180² = 1.

It can be assumed that there are no solutions in positive integers
when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain
the following:

3² – 2*2² = 1
2² – 3*1² = 1
9² – 5*4² = 1
5² – 6*2² = 1
8² – 7*3² = 1

Hence, by considering minimal solutions in x for D <= 7, the largest x
is obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the
largest value of x is obtained.
"""

#TODO: FInish this!


# check here for help:
#http://mathworld.wolfram.com/PellEquation.html

# also, check euler64.py for continuedFractions

# A few correlations here:

#x² - D*y² = 1
#x² = 1 + D*y²
#x = sqrt(1 + D*y²)

#x² - D*y² = 1
#x² - 1 = D*y²
#(x² - 1)/D = y²
#sqrt((x² - 1)/D) = y

import math

def isSquare(num):
    assert num >= 0, "Can't calculate the square root of negatives."
    sq = math.sqrt(num)
    return sq == math.floor(sq)

#D = list(filter(lambda x: not isSquare(x), range(1, 1001)))
#D = list(filter(lambda x: not isSquare(x), range(1, 8)))
#D = [1000]

#x = 1
# to continue from where program stopped...
D = [61, 97, 106, 109, 116, 117, 124, 127, 128, 137, 139, 149, 151, 153, 157, 162, 163, 164, 166, 171, 172, 175, 180, 181, 184, 191, 192, 193, 198, 199, 200, 202, 208, 211, 212, 214, 216, 229, 232, 233, 234, 239, 241, 242, 244, 245, 249, 250, 252, 253, 261, 262, 265, 268, 271, 275, 276, 277, 279, 281, 283, 284, 288, 292, 293, 294, 296, 298, 300, 301, 304, 307, 309, 311, 313, 317, 319, 320, 325, 331, 334, 336, 337, 340, 341, 343, 344, 349, 350, 352, 353, 356, 358, 360, 364, 365, 367, 368, 369, 372, 373, 376, 379, 382, 384, 387, 388, 391, 392, 393, 394, 396, 397, 405, 406, 409, 412, 414, 415, 416, 417, 419, 421, 422, 423, 424, 425, 431, 432, 433, 436, 445, 446, 448, 449, 450, 451, 452, 454, 457, 461, 463, 464, 466, 468, 471, 472, 475, 477, 478, 481, 486, 487, 489, 490, 491, 493, 496, 500, 501, 502, 504, 507, 508, 509, 511, 512, 513, 516, 517, 519, 520, 521, 522, 523, 524, 525, 526, 531, 532, 533, 536, 537, 538, 539, 541, 544, 547, 548, 549, 550, 553, 554, 556, 558, 559, 562, 565, 566, 567, 569, 571, 578, 581, 583, 585, 586, 588, 589, 592, 593, 596, 597, 599, 600, 601, 603, 604, 605, 606, 607, 608, 610, 612, 613, 614, 616, 617, 619, 621, 622, 628, 629, 630, 631, 632, 633, 634, 637, 639, 640, 641, 643, 644, 647, 648, 649, 652, 653, 654, 655, 656, 657, 661, 662, 664, 666, 667, 669, 670, 673, 675, 679, 681, 683, 684, 685, 686, 688, 691, 692, 693, 694, 698, 700, 701, 704, 708, 709, 712, 713, 716, 717, 718, 719, 720, 721, 722, 724, 725, 726, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 744, 745, 746, 748, 749, 751, 752, 753, 754, 756, 757, 758, 760, 763, 764, 765, 766, 768, 769, 771, 772, 773, 774, 775, 778, 779, 781, 787, 789, 790, 792, 794, 796, 797, 800, 801, 802, 804, 805, 806, 807, 808, 809, 810, 811, 814, 816, 819, 820, 821, 823, 824, 825, 826, 828, 829, 831, 832, 833, 834, 835, 836, 837, 838, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 855, 856, 857, 859, 861, 862, 863, 864, 865, 867, 868, 869, 871, 872, 873, 877, 878, 879, 880, 881, 882, 883, 884, 886, 889, 891, 893, 896, 907, 909, 911, 912, 913, 914, 916, 917, 919, 921, 922, 925, 926, 927, 928, 929, 931, 932, 936, 937, 941, 944, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 958, 960, 963, 964, 965, 967, 968, 969, 970, 971, 972, 974, 975, 976, 977, 980, 981, 984, 988, 989, 991, 995, 996, 997, 998, 999, 1000]
x = 4293183

while len(D) > 1:
    for d in D:
        y = math.sqrt((x*x - 1) / d)
        if y > 0 and y == math.floor(y):
            print("%d² - %d * %d² = 1 [ D left: %d ]" % (x, d, y, len(D) - 1))
            D.remove(d)
            break
    x += 1

print(D)
