#숫자의 개수
import sys
listn = list()
for i in range(3):
    n = int(sys.stdin.readline().strip())
    listn.append(n)
listn = list(map(int, list(str(listn[0] * listn[1] * listn[2]))))
for i in range(10):
    print(listn.count(i))
