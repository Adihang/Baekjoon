#최댓값
import sys
list = list()
for i in range(9):
    n = int(sys.stdin.readline().strip())
    list.append(n)
print(max(list))
print(list.index(max(list))+1)
