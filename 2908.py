#상수
x, y = map(str, input().split())
x = int(x[::-1])
y = int(y[::-1])
if x >= y:
    print(x)
else:
    print(y)
