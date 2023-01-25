#빠른 A+B
import sys
x = int(input())
for i in range(x):
    ++i
    x,y = map(int, sys.stdin.readline().strip().split())
    print(x+y)
