#셀프 넘버
def d(n):
    n = int(n)
    num = n + int(n/1000)%10 + int(n/100)%10 + int(n/10)%10 + int(n%10)
    return int(num)

selfNumSet = set(range(1, 10000))
setNum = set()

for i in range(1, 10000):
    if d(i) < 10000:
        setNum.add(d(i))
        
selfNumSet = selfNumSet - setNum
        
for i in sorted(selfNumSet):
    print(i)
