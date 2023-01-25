#나머지
import sys
setn = set()
for i in range(10):
    n = int(sys.stdin.readline().strip()) % 42
    setn.add(n)
listn = list(setn)
print(len(listn))
