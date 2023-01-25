#A+B - 5
import sys
while True:
    x , y = map(int, sys.stdin.readline().strip().split())
    if 0 == x+y:
        break
    print(x+y)
