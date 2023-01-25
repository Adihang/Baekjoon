#OX퀴즈
import sys
n = int(sys.stdin.readline().strip())
for i in range(n):
    listStr = list(sys.stdin.readline().strip())
    score = 0
    scoren = 0
    for i in listStr:
        if i == "O":
            scoren += 1
        elif i == "X":
            scoren = 0
        score += scoren
    print(score)
