anagrams = {}

for i in range(32000):
    sq = i * i
    if sq > 1000000000:
        break
    k = "".join(sorted(str(sq)))
    if k in anagrams:
        anagrams[k].append(sq)
    else:
        anagrams[k] = [sq]

for k in list(anagrams.keys()):
    if len(anagrams[k]) == 1:
        anagrams.pop(k)

