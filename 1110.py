#더하기 사이클
import sys
x = int(sys.stdin.readline().strip())
if x < 10:
    x = x*10
i = 0
z = x
while True:
    
    b = x%10
    a = x//10 + b
    x = b*10 + a%10
    i = 1+i
    if z == x:
        print(i)
        break
