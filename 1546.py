#평균
import sys
listf = list()
n = int(sys.stdin.readline().strip())
listnum = list(map(int, sys.stdin.readline().strip().split()))
listnum.sort()
for i in range(n):
    listf.append(float(listnum[i]/listnum[n-1]*100))
print(sum(listf) / len(listf))
