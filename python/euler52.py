x = 1
while True:
    l2 = list(str(2*x))
    l3 = list(str(3*x))
    l4 = list(str(4*x))
    l5 = list(str(5*x))
    l6 = list(str(6*x))
    if len(l2) == len(l3) == len(l4) == len(l5) == len(l6):
        l2.sort();
        l3.sort();
        l4.sort();
        l5.sort();
        l6.sort();
        if l2 == l3 == l4 == l5 == l6:
            print(x)
            break
    x += 1
