#X보다 작은 수
import sys
n , x = map(int, sys.stdin.readline().strip().split())
list = list(map(int, sys.stdin.readline().strip().split()))
for i in list:
    if i < x:
        print(i, end =' ')
