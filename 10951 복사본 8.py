#A+B - 4
import sys
while True:
    try :
        x , y = map(int, sys.stdin.readline().strip().split())
        print(x+y)
    except:
        break
