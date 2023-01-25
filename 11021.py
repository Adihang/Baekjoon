#A+B - 7
import sys
x = int(input())
for i in range(x):
    ++i
    x,y = map(int, sys.stdin.readline().strip().split())
    print(f"Case #{str(i+1)}: {str(x+y)}")
