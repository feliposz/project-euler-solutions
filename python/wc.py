import os

def countFile(fileName):
    countChars = 0
    countWords = 0
    countLines = 0
    countCodeLines = 0
    file = open(fileName, "r", encoding="utf8")
    while True:
        line = file.readline()
        if not line :
            break
        line = line.strip()
        countLines += 1
        if line != "" and line[0] != "#":
            countCodeLines += 1
        countWords += len(line.split(" "))
        countChars += len(line)
    print("File = %s Chars = %d Words = %d Lines = %d Code Lines = %d"
          % (fileName, countChars, countWords, countLines, countCodeLines))
    return (countChars, countWords, countLines, countCodeLines)

total = 0
for fileName in os.listdir():
    if fileName[-3:] == ".py":
        countChars, countWords, countLines, countCodeLines = countFile(fileName)
        total += countCodeLines
print(total)
