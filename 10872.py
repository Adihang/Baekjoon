#팩토리얼
num = int(input())
fac = 1
if num > 0:
    for i in range(1,num+1):
        fac *= i
        
print(fac)
