#최소, 최대
import sys
n = int(sys.stdin.readline().strip())
list = list(map(int, sys.stdin.readline().strip().split()))
list.sort()
print(f"{list[0]} {list[n-1]}")
