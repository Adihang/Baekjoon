#별 찍기 - 2
x = int(input())
for i in range(x):
    ++i
    a = "*" * (i+1)
    b = " " * (x-i-1)
    print(b+a)
